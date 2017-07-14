#!/usr/bin/env python2.7

import sys
import os
# Flask Import
from flask import Flask , request , redirect , render_template , url_for 
import MySQLdb
import config

app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('UTF-8')
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)

# MySQL configurations

host = config.host
user = config.user
passwrd = config.passwrd
db = config.db

print db
print host

# Rerouting funciton	

@app.route('/<short_url>')
def reroute(short_url):

	conn = MySQLdb.connect(host , user , passwrd, db)
	cursor = conn.cursor()
	platform = request.user_agent.platform
	browser =  request.user_agent.browser
	counter = 1

	print platform

	# Platform , Browser vars
	
	browser_dict = {'firefox': 0 , 'chrome':0 , 'safari':0 , 'other':0}
	platform_dict = {'windows':0 , 'iphone':0 , 'android':0 , 'linux':0 , 'macos':0 , 'other':0}

	# Analytics
	if browser in browser_dict:
		browser_dict[browser] += 1
	else:								
		browser_dict['other'] += 1
	
	if platform in platform_dict.iterkeys():
		platform_dict[platform] += 1
	else:
		platform_dict['other'] += 1
			
	cursor.execute("SELECT URL FROM WEB_URL WHERE S_URL = %s;" ,(short_url,) )

	try:
		new_url = cursor.fetchone()[0]
		print new_url
		# Update Counters 
		
		counter_sql = "\
				UPDATE {tn} SET COUNTER = COUNTER + {og_counter} , CHROME = CHROME + {og_chrome} , FIREFOX = FIREFOX+{og_firefox} ,\
				SAFARI = SAFARI+{og_safari} , OTHER_BROWSER =OTHER_BROWSER+ {og_oth_brow} , ANDROID = ANDROID +{og_andr} , IOS = IOS +{og_ios},\
				WINDOWS = WINDOWS+{og_windows} , LINUX = LINUX+{og_linux}  , MAC =MAC+ {og_mac} , OTHER_PLATFORM =OTHER_PLATFORM+ {og_plat_other} WHERE S_URL = '{surl}';".\
				format(tn = "WEB_URL" , og_counter = counter , og_chrome = browser_dict['chrome'] , og_firefox = browser_dict['firefox'],\
				og_safari = browser_dict['safari'] , og_oth_brow = browser_dict['other'] , og_andr = platform_dict['android'] , og_ios = platform_dict['iphone'] ,\
				og_windows = platform_dict['windows'] , og_linux = platform_dict['linux'] , og_mac = platform_dict['macos'] , og_plat_other = platform_dict['other'] ,\
				surl = short_url)
		res_update = cursor.execute(counter_sql)
		conn.commit()
		conn.close()

		return redirect(new_url)

	except Exception as e:
		e = "Something went wrong.Please try again."
		return e,404

if __name__ == "__main__" :
	app.run(host='0.0.0.0',port=8080)
table_name = "WEB_URL"

# WTF config

WTF_CSRF_ENABLED = True
SECRET_KEY = 'the_very_secure_secret_security_key_that_no_will_ever_guess'

# MySQL Config


host = "localhost"  
user = "root"
passwrd = "pass"
db = "shorty"

# Domain Host

'''
For now , use http as using https returns a bad error message , 
For https , use a SSL certificate. ( under works)
'''
domain = "http://localhost:5000/"

# Domain just for display , for r.g https://goo.gl/asdar will be goo.gl/asdar
domain_disp = "shorty.com/"

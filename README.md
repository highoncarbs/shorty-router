# :checkered_flag: Shorty-Router

Redirection service that can be publicaly hosted , while the dash **[Shorty](https://github.com/PadamSethia/shorty)** is hosted on private server.

## Getting Started

Setting the virtual environment

`pip install virtualenv`

Create the virtual environment inside the project directory

`virtualenv env`

Here env is our virtual environment , now change to project directory

`cd shorty-router`

Then install the requirements

`pip install -r requirements.txt`

Activate the virtual environment

`source env/bin/activate`

# Script for running the app

`shorty_router.ini` has the config for running the application

To run the app 

`uwsgi --ini shorty_router.ini &`

shorty-router runs on port 8080 , can be changed in shorty-router/app.py 

# :tada: done!

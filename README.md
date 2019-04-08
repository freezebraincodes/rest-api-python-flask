# README

REST-api-python-flask demonstrated examples on RESTful apis created with Python and Flask.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask.
Please note that the installation process works for mac or linux. Windows setup might be slightly different.

Flask:
```bash
pip3 install Flask
```

Virtualenv:
```bash
# install virtualenv, if not already installed
$ pip3 install virtualenv

# get into the sub directory and do following
# this will create the folder called venv, and in it will put a fresh python installation
$ virtualenv venv --python=python3.7

# this will activate and use the virtual environment
$ source venv/bin/activate

# when in venv environment
$ python --version

# install Flask-RESTful
pip install Flask-RESTful

# install Flask-JWT
pip install Flask-JWT

# to find out what was installed
pip freeze

# to deactivate the virtual environment
$ deactivate
```

## Sub Project Directories
- `first-rest-api`: A basic REST api for a store in demonstrating GET/POST  
- `item-list-rest-api`: Demonstrating the use of `virtualenv` and basic authentication with json web token (jwt)
- `item-list-with-sqlite-rest-api`: Demonstrating the api with sqlite database

## Usage

####  `first-rest-api`: 
Go to sub directory and run the program.

```bash
python3 app.py
```

####  `item-list-rest-api` and `item-list-with-sqlite-rest-api`: 
Go to sub directory and run the program.

```bash
# start the venv
$ source venv/bin/activate

# go to sub directory
$ cd code 

# start app
$ python app.py

# deactivate the venv
deactivate
```

## References
- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-JWT](https://pythonhosted.org/Flask-JWT/)
- [Udemy](https://www.udemy.com/rest-api-flask-and-python/)
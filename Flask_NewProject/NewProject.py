#!/usr/bin/env python

"""Used to create a new Flask project with some data already pre-created when starting a new project."""


# This is called to create a new Flask project taking an argument of project name
# This will create a simple as follows:
#
# in terminal run
# $ FlaskProject FlaskApp
#
# will create the structure:
# 
# FlaskApp/
# |
# --FlaskApp/
#   |
#   --app.py
#   |
#   tests/
#     |
#     --test_flask.py

# So this will make a direstory and subdirectory based on user input,
# the create a directory call tests, then create two files called
# app.py, as the main program to run, and test_flask.py in the tests
# directory to write your flask tests.

import os

def create_new_project():
    pwd = os.getcwd()

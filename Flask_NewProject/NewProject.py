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
from sys import argv

# mapped to command name flask-skeleton
def skeleton():
    # will create a skeleton project with blank files.
    skeleton = CreateDirs(argv[1])

# mapped to command name flask-simple
def simple_setup():
    # will create the skeleton project, but some information already pre-added
    simple = CreateDirs(argv[1])
    simple.add_to_files()

#########################


def create_dirs(path):
    directory = os.path.dirname(path)
    if not os.path.exists(path):
        os.mkdir(path)


class CreateDirs(object):
    """Used to create directries for Flask project."""

    def __init__(self, projectName):
        self.projectName = projectName

        self.pwd = os.getcwd()
        self._PROJECT_DIR = None
        self._PROJECT_PACKAGE_DIR = None
        self._TESTS_IN_PACKAGE = None

        self.set_dir_names()
        self.create_new_project()

    def set_dir_names(self):
        self._PROJECT_DIR = self.pwd+'/'+self.projectName
        self._PROJECT_PACKAGE_DIR = self._PROJECT_DIR+'/'+self.projectName
        self._TESTS_IN_PACKAGE = self._PROJECT_DIR+'/test'

    def create_new_project(self):
        # 1) create directories        
        create_dirs(self._PROJECT_DIR)
        create_dirs(self._PROJECT_PACKAGE_DIR)
        create_dirs(self._TESTS_IN_PACKAGE)

        # 2) crete files app.py and tests.py    
        open(self._PROJECT_PACKAGE_DIR+'/app.py', 'a').close()
        open(self._TESTS_IN_PACKAGE+'/tests.py', 'a').close()
        

    def add_to_files(self):
        app_content = """from flask import Flask


app = Flask(__name___)

@app.route('/')
def index_page():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)"""

        testing_content = """import {0}
import unittest

class FlaskAppTesting(unittest.TestCase):

    def setUp(self):
        self.{0}.app.config['TESTING'] = True
        self.app = {0}.app.test_client()

    def tearDown(self):
        pass

    def test_for_Hello_World(self):
        rv = self.app.get('/')
        assert b'Hello World!'in rv.data""".format(self.projectName)

        


#if __name__ == "__main__":
#    create_new_project()

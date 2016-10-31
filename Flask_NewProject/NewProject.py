#!/usr/bin/env python

"""Used to create a new Flask project with some data already pre-created when starting a new project."""


# This is called to create a new Flask project taking an argument of project name
# This will create a simple as follows:


import os
from sys import argv
from script_info import run
#import argparse


# mapped to command name flask-skeleton
def skeleton():
    # will create a skeleton project with blank files.
    skeleton = CreateDirs(argv[1])
    skeleton.create_project_directory()

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

        # in Project Dir is run.py, bin/ Project_Package/, docs/ tests/ and __init__.py
        self._PROJECT_DIR = None
        self._IN_PROJECT_DIR = ['/bin', '/docs', '/tests']

        # in Project Package is app.py for skeleton/simple and static/ templates/
        # and for blueprint(s) its __init__.py, home/
        self._PROJECT_PACKAGE_DIR = None

        # if it is blueprint, create in home/ __init__.py, controllers.py static/ templates/
        self._CREATE_BLUEPRINT = None

        
        #self.set_dir_names()
        #self.create_new_project()

    def create_project_directory(self):
        # will create parent directory and files in it
        self._PROJECT_DIR = self.pwd + '/' + self.projectName

        # Create folders in project folder
        create_dirs(self._PROJECT_DIR)
        create_dirs(self._PROJECT_DIR + '/'+self.projectName)
        for folder in self._IN_PROJECT_DIR:
            create_dirs(self._PROJECT_DIR + folder)

        # create files in project folder
        open(self._PROJECT_DIR + '/__init__.py', 'a').close()
        with open(self._PROJECT_DIR + '/run.py', 'w') as run_file:
            run_file.write(run(self.projectName))

    def create_project_package_directory(self):
        # will create folders and files in package directory
        pass

    def create_blueprint_directory(self):
        # will create a blueprint directory and files in it
        pass

    #def create_new_project(self):
        # 1) create directories        
        #create_dirs(self._PROJECT_DIR)
        #create_dirs(self._PROJECT_PACKAGE_DIR)
        #create_dirs(self._TESTS_IN_PACKAGE)

        # 2) crete files app.py and tests.py    
        #open(self._PROJECT_PACKAGE_DIR+'/app.py', 'a').close()
        #open(self._TESTS_IN_PACKAGE+'/tests.py', 'a').close()
        

    def add_to_files(self):
        app_content = """#!/usr/bin/env python2.7
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index_page():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)"""

        testing_content = """#!/usr/bin/env python3
import {0}
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

        with open(self._PROJECT_PACKAGE_DIR+'/app.py', 'w') as app:
            app.write(app_content)
        with open(self._TESTS_IN_PACKAGE+'/tests.py', 'w') as test:
            test.write(testing_content)

        


#if __name__ == "__main__":
#    create_new_project()

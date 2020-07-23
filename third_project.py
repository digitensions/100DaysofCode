#!/usr/bin/env python3

'''
Script that provides console printed outputs from classes.
test_third_project.py specifies best practises for testing console printed outputs.
'''

class Profile:
    def __init__(self, name, age, job, employer):
        self._name = name
        self._age = age
        self._job = job
        self._employer = employer
    def print_name(self):
        print(self._name)
    def print_job(self):
        print(self._job)
    def print_age(self):
        print(self._age)
    def print_employer(self):
        print(self._employer)

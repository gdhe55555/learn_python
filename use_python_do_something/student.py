#!/usr/bin/env python

class Student(object):
    """Student class"""
    def __init__(self, name, score):
        super(Student, self).__init__()
        self.name, self.score = name, score
        
    def print_score(self):
        print("%s:%s" %(self.name, self.score))

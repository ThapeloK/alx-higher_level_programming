#!/usr/bin/python3
""" Defines a function that attributes an object """


def add_attribute(ob, aname, attr):
    """ Adds new attribute to an attributes! """
    if hasattr(ob, aname):
        setattr(ob, aname, attr)
    else:
        raise TypeError

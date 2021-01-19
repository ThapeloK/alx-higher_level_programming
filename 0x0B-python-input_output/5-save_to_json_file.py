#!/usr/bin/python3

""" Defines a JSON file-writing function. """
import json


def save_to_json_file(my_obj, filename):
    """ saves object as a json dump """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))

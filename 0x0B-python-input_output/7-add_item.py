#!/usr/bin/python3
""" add_item script: script to save all arguments to a json file """
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if __name__ == "__main__":
    """ if it exists, pull the file. otherwise, make a new one """
    if os.path.exists(filename):
        try:
            olist = load_from_json_file(filename)
        except:
            olist = []
    else:
        olist = []
    for arg in range(1, len(sys.argv)):
        olist.append(sys.argv[arg])
    save_to_json_file(olist, filename)

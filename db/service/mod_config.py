#!/usr/bin/python
#name:mod_config.py

import ConfigParser
import os

def getConfig(conf_file, section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/conf/' + conf_file
    config.read(path)
    return config.get(section, key)
    

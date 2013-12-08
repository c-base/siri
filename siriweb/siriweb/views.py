#! /usr/bin/python
# -*- coding: utf-8 -*-

import random, re, os, sys, time, subprocess
import logging
import hashlib
from urllib2 import Request, urlopen

from jsonrpc import jsonrpc_method

from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.add_extension("r_kiosk-0.9.0-fx.xpi")
driver = webdriver.Firefox(firefox_profile=fp)
#driver = webdriver.Firefox()

logfile = 'siriweb.log'

logger = logging.getLogger('siriweb')
hdlr = logging.FileHandler(logfile)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

enabled = 1

@jsonrpc_method('home')
def home(request, foo):
    driver.get("http://www.c-base.org")
    return "aye"


@jsonrpc_method('github')
def github(request, foo):
    driver.get("http://www.github.com")
    return "aye"

@jsonrpc_method('open')
def github(request, url):
    driver.get(url)
    return "aye"


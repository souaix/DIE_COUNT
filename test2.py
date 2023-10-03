#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request
import json

import sys
import os
from ftplib import FTP
import datetime
import pandas as pd
from sqlalchemy import create_engine



app = Flask(__name__)

@app.route('/die_count/', methods=['POST'],strict_slashes=False)


def test2():
	result = [{'Message':'Not found data','Qty':'None'}]
	return result



@app.route('/die_count2/', methods=['POST'],strict_slashes=False)


def test3():
        result = [{'Message':'NNNNNNNNN','Qty':'None'}]
        return result


def server(server_):
	server_.serve_forever()
	pass

from threading import Thread

from gevent import pywsgi

server_ = pywsgi.WSGIServer(('10.21.98.21',9990),app)

if __name__ == '__main__':

	print('----')
	t2 = Thread(target=server(server_))
#	t3 = Thread(target=server3(server3_))
#	t2.start()
#	t3.start()

	

#	Thread(target=test1()).start()
#	Thread(target=test2()).start()

	

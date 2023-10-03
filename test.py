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



app_dc2 = Flask('app_dc2')

@app_dc2.route('/die_count/', methods=['POST'],strict_slashes=False)


def test2():
	result = [{'Message':'Not found data','Qty':'None'}]
	return result



app_dc3 = Flask('app_dc3')

@app_dc3.route('/die_count/', methods=['POST'],strict_slashes=False)


def test3():
        result = [{'Message':'NNNNNNNNN','Qty':'None'}]
        return result



def server2(server2):
	server2.serve_forever()
	pass
def server3(server3):
	server3.serve_forever()
	pass

from threading import Thread

from gevent import pywsgi

server2_ = pywsgi.WSGIServer(('10.21.98.21',9990),app_dc2)
server3_ = pywsgi.WSGIServer(('10.21.98.21',9991),app_dc3)



#       t2 = Thread(target=server2(server2_))
#t3 = Thread(target=server3(server3_))

if __name__ == '__main__':


	from threading import Thread

	from gevent import pywsgi

	server2_ = pywsgi.WSGIServer(('10.21.98.21',9990),app_dc2)
	server3_ = pywsgi.WSGIServer(('10.21.98.21',9991),app_dc3)


	print('----')

	t2 = Thread(target=server2(server2_))
	t3 = Thread(target=server3(server3_))
#	t2.start()
#	t3.start()

	

#	Thread(target=test1()).start()
#	Thread(target=test2()).start()

	

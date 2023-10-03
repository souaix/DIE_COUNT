#!/usr/bin/env python
# coding: utf-8
from flask import Flask, jsonify, request


from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count, Process
from bottle import Bottle

#app = Bottle()

app = Flask(__name__)

@app.route('/aaa/', methods=['POST'],strict_slashes=False)
#@app.POST("/die_count")

def test2():
	result = [{'Message':'Not found data','Qty':'None'}]
	return result


server2 = WSGIServer(('10.21.98.21',9990),app,log=None)
server2.start()

@app.route('/bbb/', methods=['POST'],strict_slashes=False)


def test3():
        result = [{'Message':'NNNNNNNNN','Qty':'None'}]
        return result


server3 = WSGIServer(('10.21.98.21',9991),app,log=None)
server3.start()


def server_forever():
	server2.start_accepting()
	server3.start_accepting()
	server2._stop_event.wait()
	server3._stop_event.wait()


if __name__ == '__main__':

	print('----')
	for i in range(cpu_count()):
		p = Process(target=server_forever)
		p.start()

	

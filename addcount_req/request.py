#!/usr/bin/env python
import httplib
import argparse
import time

def start_request(args,unknown_args):
    request_id = args.ip + ":"+ args.port
    count = 1
    while 1:
        url = "http://"+request_id+"/add/1"
        conn = httplib.HTTPConnection(request_id)
        print "Launch Request: time:"+repr(time.time()) + "\ncount:" + repr(count)
        conn.request(method="GET", url=url)

        response = conn.getresponse()
        if response.reason == "OK":
            res = response.read()
            count = count + 1
            print "response time:" + repr(time.time()) + "\ncontent: " + res
        else :
            print "request failed,time:" + repr(time.time()) 
            res = response.read()
            print "Failed Reason:"+res

parser = argparse.ArgumentParser("start request!")
parser.set_defaults(func = start_request)
parser.add_argument("--ip", help="IP to Request", type = str, default = "localhost" )
parser.add_argument("--port", help="port to Request", type = str, default = "5000" )

args , unknown_args = parser.parse_known_args()
try:
    args.func(args,unknown_args)
except KeyboardInterrupt:
    pass

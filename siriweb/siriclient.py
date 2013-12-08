#!/usr/bin/env python

import sys
import random
import jsonrpclib

#from jsonrpc.proxy import ServiceProxy

#server = ServiceProxy('http://127.0.0.1:8000/rpc/')


jsonrpclib.config.version = 1.0
server = jsonrpclib.Server('http://127.0.0.1:8000/rpc/')

#server.github("foo")
server.open(sys.argv[1])
#print server.rgb(255, 0, 0)
#print " ".join(sys.argv[1:])
#print server.tts('julia', " ".join(sys.argv[1:]))
#print server.voices()
#server.play(random.choice(server.sounds()))
#server.play("siri_looped")

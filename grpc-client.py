#!/usr/bin/env python3
from __future__ import print_function

from base64 import b64encode

import json
import time
import sys
import random

import grpc
import grpc_details_pb2
import grpc_details_pb2_grpc

def doRawImage(debug=False):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    req = grpc_details_pb2.rawImageReq(img=img)
    response = stub.doRawImage(req)

    if debug:
        # decode response
        print("Do raw Image Response is", response)
        print(json.loads(response.text))

def doAdd(debug=False):
    req = grpc_details_pb2.addNumbersReq(num1= 5, num2=10)
    response = stub.doAdd(req)
    if debug:
        # decode response
        print("Do Add Response is", response)
        print(json.loads(response.text))


def doDotProduct(debug=False):
    a = [random.random() for i in range(100)]
    b = [random.random() for i in range(100)]

    req = grpc_details_pb2.dotProductReq(num1 = a, num2= b)
    response = stub.doDotProduct(req)
    if debug:
        # decode response
        print("Do Dot Product Response is", response)
        print(json.loads(response.text))

def doJsonImage(debug=False):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    req = grpc_details_pb2.rawJsonReq(imgString= b64encode(img).decode('utf-8'))
    response = stub.doJsonImage(req)

    if debug:
        # decode response
        print("Do JSON Image Response is", response)
        print(json.loads(response.text))

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

channel = grpc.insecure_channel('{}:50051'.format(host))
stub = grpc_details_pb2_grpc.lab6serviceStub(channel)

addr = f"http://{host}:5000"
print(f"Running {reps} reps against {addr}")


if cmd == 'rawImage':
    start = time.perf_counter()
    for x in range(reps):
        doRawImage()
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'add':
    start = time.perf_counter()
    for x in range(reps):
        doAdd()
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'jsonImage':
    start = time.perf_counter()
    for x in range(reps):
        doJsonImage()
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'dotProduct':
    start = time.perf_counter()
    for x in range(reps):
        doDotProduct()
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
else:
    print("Unknown option", cmd)
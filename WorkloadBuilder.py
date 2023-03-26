import random
import PingClient
import PingServer
import Node
import PingApplication
import socket
import pickle
import time
import asyncio
import select
from _thread import *


def buildAndRunPingServerMultiple(n):

    pServer=PingServer.PingServer(8888)
    for i in range(0, n):
        msg, addr = pServer.s.recvfrom(1024)
        rec_msg = pickle.loads(msg)
        port = addr[1]+i
        pServer.handlePingRequest(rec_msg, (addr[0],port))
    time.sleep(1)
    pServer.s.close()

def buildAndRunPingServer():

    pServer=PingServer.PingServer(7777)
    msg, addr = pServer.s.recvfrom(1024)
    rec_msg = pickle.loads(msg)

    pServer.handlePingRequest(rec_msg, addr)
    pServer.s.close()
    time.sleep(2)



def buildAndRunClient():
    pClient= PingClient.PingClient(1111)
    pingCom=PingApplication.Ping("Hello World")

    pClient.sendCommand(pingCom,('127.0.0.1',7777))

    msg,addr = pClient.s.recvfrom(1024)
    rec_msg = pickle.loads(msg)

    pClient.handlePongReply(rec_msg)
    pClient.close()
    time.sleep(2)

    return pClient.hasResult()


def buildAndRunMultipleClients(n):

    startArr=[]
    resArr=[]

    for n in range (0,n):

        startMsg="Hello from "+str(n)
        startArr.append(startMsg)
        port = 2222+n

        pClient = PingClient.PingClient(port)
        pingCom = PingApplication.Ping(startMsg)
        pClient.sendCommand(pingCom,('127.0.0.1',8888))
        msg,addr = pClient.s.recvfrom(1024)

        rec_msg = pickle.loads(msg)
        pClient.handlePongReply(rec_msg)
        pClient.close()
        resArr.append(pClient.getResult().value)

    time.sleep(2)
    return startArr,resArr













import socket
import pickle
import time

class Node:



    def __init__(self,port):
        self.timerAdder = []
        self.serverAdress = "127.0.0.1"
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = port
        self.s.bind((self.serverAdress, self.port))
        self.runTimer=False ###Should be done with queue !!!!

    def send(self,message, reciver):
        if message is None or reciver is None:
            return
        sendCounter =0
        if self.timerAdder==[]:
            self.s.sendto(pickle.dumps(message),reciver)
        else:
            while self.runTimer:
                sendCounter+=1
                for t in self.timerAdder:
                    time.sleep((t.retryMsec/1000))
                    self.s.sendto(pickle.dumps(message), reciver)
                if sendCounter > 20: #timeout
                    self.runTimer = False
                    self.timerAdder = []
                    break



    def set(self,timer):
        if timer is None:
            return
        else:
            self.runTimer = True
            self.timerAdder.append(timer)

    def notify(self):
        self.runTimer = False
        self.timerAdder = []

    def close(self):
        self.s.close()





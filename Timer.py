import PingApplication

class Timer:
    def __init__(self,time):
        self.retryMsec=time
        self.active=True

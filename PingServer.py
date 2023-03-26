import Node
import PingApplication
import Timer

class PingServer(Node.Node):

    def __init__(self,port):
        super().__init__(port)

    def handlePingRequest(self, msg, sender):
        pass

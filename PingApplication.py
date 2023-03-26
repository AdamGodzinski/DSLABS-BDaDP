import Application
import Command
import Result


class Ping(Command.Command):
    def __init__(self, value):
        self.value = value


class Pong(Result.Result):

    def __init__(self, value):
        self.value = value

    def execute(self,command): #functionality taken from Application can stay here or be overrided in PingApplication
        if not isinstance(command,Ping):
            print("Wrong Argument")
        self.value = command.value
        return self


class PingApplication(Application.Application):
    def __init__(self):
        pass














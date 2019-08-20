import socket
import threading
import time

def testconn(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((host, port))
        return host + " Server " + str(port) + " is connect"
    except Exception:
        return host + " Server " + str(port) + " is not connect!!!"
    sk.close()


class Test(threading.Thread):
    def __init__(self):
        pass

    def run(self,host,port):
        while True:
            print(time.strftime('%Y-%m-%d %H:%M:%S'),testconn(host,port))
            time.sleep(1)

a = Test()
a.run('114.114.114.114',53)

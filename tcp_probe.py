import socket
import time

def tcp_probe(host, port=80, timeout=2):

    start = time.time()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        sock.connect((host, port))

        rtt = (time.time() - start) * 1000

        sock.close()

        return rtt

    except:
        return None
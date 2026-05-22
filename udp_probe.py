import socket
import time

def udp_probe(host, port=9999, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)

        start = time.time()
        sock.sendto(b"test", (host, port))

        sock.recvfrom(1024)   # may fail
        end = time.time()

        sock.close()

        return (end - start) * 1000

    except Exception:
        return None   # 🔥 IMPORTANT: ignore error safely
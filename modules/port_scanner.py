import socket
import threading

open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        open_ports.append(port)
        sock.close()
    except:
        pass

def run_port_scan(target):
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]
    threads = []

    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return {"open_ports": open_ports if open_ports else "None detected"}

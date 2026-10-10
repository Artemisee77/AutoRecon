import socket

ip_target = (input("masukkan ip target: "))
port_target= int(input("masukkan port target: "))

print(f"mencoba terhubung ke {ip_target}:{port_target}" )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5.0)

result = s.connect_ex((ip_target, int(port_target)))

if result == 0:
    print(f"port {port_target} terbuka")
else:
    print(f"port {port_target} tertutup")

s.close()
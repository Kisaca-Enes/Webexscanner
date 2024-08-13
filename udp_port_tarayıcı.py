import socket

def udp_port_tarama(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(1)
        try:
            s.sendto(b'', (host, port))
            return True
        except socket.error:
            return False

def main():
    host = input("Web sitesi veya IP adresi girin: ")
    port = int(input("Taramak istediğiniz UDP portunu girin: "))
    if udp_port_tarama(host, port):
        print(f'UDP Port {port} açık olabilir')
    else:
        print(f'UDP Port {port} kapalı veya yanıt alınamadı')

if __name__ == "__main__":
    main()

import socket
import ssl

def connect_plain(host, port=80):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            print(f"Povezan na {host}:{port} (nezaštićeno)")
            sock.sendall(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            response = sock.recv(1024)
            print("Primljeni odgovor (dio):")
            print(response.decode(errors='ignore'))
    except Exception as e:
        print(f"Greška pri povezivanju na {host}:{port} - {e}")

def connect_tls(host, port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"Povezan na {host}:{port} (TLS zaštićeno)")
                ssock.sendall(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                response = ssock.recv(1024)
                print("Primljeni odgovor (dio):")
                print(response.decode(errors='ignore'))
    except Exception as e:
        print(f"Greška pri povezivanju na {host}:{port} - {e}")

if __name__ == "__main__":
    host = "www.google.com"
    print("---- Povezivanje na port 80 (nezaštićeno) ----")
    connect_plain(host, 80)
    print("\n---- Povezivanje na port 443 (TLS) ----")
    connect_tls(host, 443)
#Port 443 — TLS (HTTPS) veza
#Prije slanja podataka uspostavlja se sigurna, enkriptirana veza pomoću TLS protokola.
#Podaci (HTTP zahtjev i odgovor) su šifrirani i ne vide se u običnom tekstu na mreži.


# Port 80 — nezaštićena HTTP veza
#Podaci se šalju i primaju nešifrirano, "u običnom tekstu".

#Odgovor koji se dobije je standardni HTTP odgovor (statusni redak, zaglavlja, eventualno sadržaj).


#Nema enkripcije, pa podaci mogu biti presretnuti ili izmijenjeni na put

import socket
import ssl

def get_ssl_cert_info(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

            subject = cert.get('subject', ())
            issuer = cert.get('issuer', ())
            not_before = cert.get('notBefore', 'N/A')
            not_after = cert.get('notAfter', 'N/A')

            print(f"Subject:")
            for item in subject:
                print(f"  {item}")

            print(f"\nIssuer:")
            for item in issuer:
                print(f"  {item}")

            print(f"\nValid From: {not_before}")
            print(f"Valid Until: {not_after}")

if __name__ == "__main__":
    get_ssl_cert_info("www.google.com")




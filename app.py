import socket

def get_service_name(port):
    try:
        service_name_tcp = socket.getservbyport(port, 'tcp')
    except OSError:
        service_name_tcp = None

    try:
        service_name_udp = socket.getservbyport(port, 'udp')
    except OSError:
        service_name_udp = None

    return service_name_tcp, service_name_udp

def main():
    while True:
        try:
            port = int(input("Enter a port number (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a valid port number.")
            continue

        service_name_tcp, service_name_udp = get_service_name(port)

        if service_name_tcp:
            print(f"Port {port} (TCP) is commonly used for: {service_name_tcp}")
        else:
            print(f"Port {port} (TCP) has no common service associated with it.")

        if service_name_udp:
            print(f"Port {port} (UDP) is commonly used for: {service_name_udp}")
        else:
            print(f"Port {port} (UDP) has no common service associated with it.")
            
        print()

if __name__ == "__main__":
    main()

import socket
import csv
import ipaddress
from pathlib import Path

target = input("Enter target IP address: ")

try:
    ipaddress.ip_address(target)
except ValueError:
    print("Error: Invalid IP address!")
    exit()

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alternative"
}

results = []

print(f"\nScanning target: {target}")
print("-" * 40)

for port, service in services.items():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)

    try:
        status = client.connect_ex((target, port))

        if status == 0:
            result = "OPEN"
        else:
            result = "CLOSED"

    except OSError as error:
        result = "ERROR"
        print(f"Connection error on port {port}: {error}")

    finally:
        client.close()

    print(f"Port {port} | {service} | {result}")
    results.append([port, service, result])

try:
    Path("reports").mkdir(exist_ok=True)

    with open("reports/scan_report.txt", "w") as file:
        file.write(f"Network Scan Report\nTarget: {target}\n\n")
        for port, service, status in results:
            file.write(f"{port} | {service} | {status}\n")

    with open("reports/scan_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Service", "Status"])
        writer.writerows(results)

    print("\nTXT and CSV reports generated successfully!")

except OSError as error:
    print(f"Report generation failed: {error}")

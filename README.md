# Network Port Scanner

A beginner-friendly Python-based TCP port scanner built on Ubuntu Linux. This project scans authorized targets, identifies common services, checks port connectivity, and generates TXT and CSV reports.

## Features

- Scan multiple TCP ports.
- Identify common services such as SSH, FTP, HTTP and MySQL.
- Detect open and closed ports.
- Validate IPv4 addresses.
- Handle connection errors.
- Generate TXT and CSV scan reports.
- Automated unit testing.

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking
- Linux (Ubuntu)
- CSV Module
- Unit Testing

## Project Structure

```text
network-port-scanner/
├── src/
│   └── scanner.py
├── tests/
│   └── test_scanner.py
├── reports/
│   ├── scan_report.txt
│   └── scan_report.csv
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/network-port-scanner.git
cd network-port-scanner
```

Run the scanner:

```bash
python3 src/scanner.py
```

Enter an authorized target IPv4 address when prompted.

## Run Tests

```bash
python3 -m unittest discover -s tests -v
```

## Sample Output

```text
Scanning target: 127.0.0.1

Port 21 | FTP | CLOSED
Port 22 | SSH | OPEN
Port 80 | HTTP | CLOSED
Port 443 | HTTPS | CLOSED

TXT and CSV reports generated successfully!
```

## Learning Outcomes

- Understanding IP addresses and TCP ports.
- Python socket programming.
- Network connectivity testing.
- Error handling and input validation.
- Automated testing and report generation.

## Disclaimer

This project is intended for educational purposes. Scan only your own systems or systems for which you have explicit authorization.

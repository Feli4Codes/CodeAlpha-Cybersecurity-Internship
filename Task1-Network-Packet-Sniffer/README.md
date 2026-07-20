# Network Packet Sniffer

## Project Overview

This project was developed as part of the CodeAlpha Cyber Security Internship.

The application is a network packet sniffer built using Python and Scapy. It captures network traffic in real time and displays key packet information, including source and destination IP addresses, protocols, ports, packet length, and payload data when available.

The project demonstrates the fundamentals of packet capture, network traffic analysis, and protocol inspection.

---

## Objectives

- Capture live network packets.
- Analyze packet structure and network protocols.
- Display packet information in a readable format.
- Support protocol-based packet filtering.
- Provide an option to save packet summaries to a file.
- List available network interfaces.

---

## Features

- Real-time packet capture
- Protocol filtering (TCP, UDP, ICMP)
- Source and destination IP address identification
- Source and destination port identification
- Packet length display
- Payload extraction (when available)
- Network interface listing
- Packet summary export

---

## Technologies Used

- Python 3
- Scapy
- argparse

---

## Project Structure

```
Task1-Network-Packet-Sniffer/
│
├── packet_sniffer.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/CodeAlpha-Cybersecurity-Internship.git
```

Navigate to the project directory:

```bash
cd CodeAlpha-Cybersecurity-Internship/Task1-Network-Packet-Sniffer
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## Usage

Start packet capture:

```bash
python packet_sniffer.py
```

Capture only TCP packets:

```bash
python packet_sniffer.py -p tcp
```

Capture a fixed number of packets:

```bash
python packet_sniffer.py -c 20
```

List available network interfaces:

```bash
python packet_sniffer.py --list-interfaces
```

Save packet summaries to a file:

```bash
python packet_sniffer.py -o packets.txt
```

---

## Requirements

- Python 3.8 or later
- Scapy
- Npcap (Windows only)

On Windows, run the application with Administrator privileges to allow packet capture. Npcap must be installed before running the application.

---

## Screenshots

The `screenshots` directory contains sample output demonstrating:

- Application startup
- Network interface listing
- Packet capture
- Protocol filtering
- Packet analysis

---

## Learning Outcomes

This project provided practical experience in:

- Network packet capture
- Network protocol analysis
- Traffic inspection using Scapy
- Python programming
- Basic network security concepts

---

## Future Improvements

Possible enhancements include:

- Graphical user interface
- Packet filtering by IP address or port
- Packet logging to CSV or JSON
- Live traffic statistics
- Packet search functionality

---

## Author

**Felicity Avor**

CodeAlpha Cyber Security Internship
"""Simple network packet sniffer built with Scapy.

This program captures network packets, analyzes their structure,
and displays useful details such as source/destination IP addresses,
protocol names, ports, and payload content. It is designed to help
learn how data flows through a network and how common protocols work.
"""

import argparse
from functools import partial
from pathlib import Path

from scapy.all import get_if_list, sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP


class SnifferError(Exception):
    """Raised when the packet sniffer cannot start correctly."""


def build_parser():
    parser = argparse.ArgumentParser(description="Basic network packet sniffer")
    parser.add_argument("-i", "--interface", default=None, help="Network interface to sniff on")
    parser.add_argument("-p", "--protocol", choices=["any", "tcp", "udp", "icmp"], default="any",
                        help="Protocol filter to apply")
    parser.add_argument("-c", "--count", type=int, default=20,
                        help="Number of packets to capture (default: 20, use 0 for unlimited)")
    parser.add_argument("-o", "--output", default=None, help="Optional file to save packet summaries")
    parser.add_argument("-l", "--list-interfaces", action="store_true",
                        help="List available network interfaces and exit")
    return parser


def clean_payload(raw_bytes, max_len=200):
    """Return a safe, printable preview of payload bytes.

    Non-printable/control bytes are replaced with '.' so binary
    protocols don't corrupt terminal output, and long payloads are
    truncated so the console stays readable.
    """
    if not raw_bytes:
        return ""

    truncated = raw_bytes[:max_len]
    printable = "".join(
        chr(b) if 32 <= b <= 126 else "." for b in truncated
    )
    suffix = "..." if len(raw_bytes) > max_len else ""
    return printable + suffix


def format_packet(packet):
    lines = ["\n" + "=" * 50]

    if packet.haslayer(IP):
        ip_layer = packet[IP]
        lines.append(f"Source IP       : {ip_layer.src}")
        lines.append(f"Destination IP  : {ip_layer.dst}")
        lines.append(f"Protocol Number : {ip_layer.proto}")
        lines.append(f"Packet Length   : {len(packet)} bytes")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            lines.append("Protocol Name   : TCP")
            lines.append(f"Source Port     : {tcp_layer.sport}")
            lines.append(f"Destination Port: {tcp_layer.dport}")
            payload = clean_payload(bytes(tcp_layer.payload))
            if payload:
                lines.append(f"Payload        : {payload}")
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            lines.append("Protocol Name   : UDP")
            lines.append(f"Source Port     : {udp_layer.sport}")
            lines.append(f"Destination Port: {udp_layer.dport}")
            payload = clean_payload(bytes(udp_layer.payload))
            if payload:
                lines.append(f"Payload        : {payload}")
        elif packet.haslayer(ICMP):
            lines.append("Protocol Name   : ICMP")
        else:
            lines.append("Protocol Name   : IP")
    else:
        lines.append("Protocol Name   : Non-IP packet")

    lines.append("=" * 50)
    return "\n".join(lines)


def packet_callback(packet, output_path=None):
    summary = format_packet(packet)
    print(summary)

    if output_path:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("a", encoding="utf-8") as handle:
            handle.write(summary + "\n")


def get_available_interfaces():
    try:
        return get_if_list()
    except Exception as exc:
        raise SnifferError(f"Unable to list network interfaces: {exc}") from exc


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.count < 0:
        raise SnifferError("Packet count cannot be negative.")

    if args.list_interfaces:
        for interface in get_available_interfaces():
            print(interface)
        return

    protocol_filter = None if args.protocol == "any" else args.protocol
    output_path = args.output

    print("Basic Network Sniffer Started...")
    print(f"Interface : {args.interface or 'default'}")
    print(f"Protocol  : {args.protocol}")
    print(f"Count     : {args.count if args.count > 0 else 'unlimited'}")
    if output_path:
        print(f"Output    : {output_path}")
    if args.count == 0:
        print("Capturing without a limit — press Ctrl + C to stop at any time.\n")
    else:
        print(f"Will stop automatically after {args.count} packets. Press Ctrl + C to stop early.\n")

    try:
        if args.interface:
            interfaces = get_available_interfaces()
            if args.interface not in interfaces:
                raise SnifferError(
                    f"Interface '{args.interface}' was not found. Available interfaces: {', '.join(interfaces) if interfaces else 'none'}"
                )

        sniff(
            iface=args.interface,
            filter=protocol_filter,
            prn=partial(packet_callback, output_path=output_path),
            store=False,
            count=args.count,
        )
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except PermissionError as exc:
        raise SnifferError(
            "Permission denied while starting the sniffer. Run the script as Administrator."
        ) from exc
    except OSError as exc:
        raise SnifferError(
            "Could not start the sniffer. Install Npcap/WinPCap and ensure the interface is available."
        ) from exc
    except SnifferError:
        raise
    except Exception as exc:
        raise SnifferError(f"Unexpected error while running the sniffer: {exc}") from exc


if __name__ == "__main__":
    try:
        main()
    except SnifferError as exc:
        print(f"Error: {exc}")
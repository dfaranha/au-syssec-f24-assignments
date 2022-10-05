# Attacking and defending networks

## Your Task(s)

The assignment has three parts, covering both constructive and destructive aspect of networks: (1) the first deals with implementing an encrypted covert channel; (2) the second with implementing a TCP throttling tool; and (3) the third with implementing a small VPN tunneling program. If you are doing the assignment individually, you can choose one out of the three. If you are in a group (2 or 3 people), the group should deliver two out of the three parts.

### 1. Encrypted covert channel

For this part, you will need to have some familiarity with the IP protocol to write low-level networking code using a library. Suggestions are the `libnet/libpcap` library in the C programming language or the equivalent `socket` package in Python.

The objective of this task is to to implement an one-way encrypted covert channel using the [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) (Internet Control Message Protocol) protocol.
Communication is one-way to follow the typical use case of covert channels for _exfiltration_ of sensitive data.
ICMP is an error-reporting protocol that network devices use to inform of error messages to the source IP address when network problems prevent an IP packet to be delivered.
The most familiar contact we have with the ICMP protocol is the `ping` tool using the `Echo Request` and `Echo Reply` messages. While these packets are typically small, it is not well-known that ICMP packets can carry much larger pieces of data.

You will implement client/server programs to exchange encrypted covert channel through the network. For this, use ICMP messages with type `47` (among the reserved numbers). The client program should receive a destination IP address from the command-line to transmit messages and wait for input from the keyboard at the client-side. The server program should listen to the network for such messages and print them in the console as they arrive. For encryption, you are free to use a preshared symmetric key to protect the transmitted payload. Choose algorithms and modes of operation wisely.

### 2. Throttling TCP connections

For this part, you will need to have some familiarity with the TCP protocol to write low-level networking code using a library. Suggestions again are the `libnet/libpcap` library in the C programming language or the equivalent `Scapy` package in Python.

The objective of this task is to slow down or interrupt TCP connections by forcing retransmission of packets. An illustrative example of such an approach is the `tcpnice` program in the `dsniff` package which reduces windows advertised to artificially decrease bandwidth. We will adopt two different approaches: send 3 ACK packets to simulate packet loss and force retransmission; send a TCP reset packet to drop the connection altogether.

You will implement a tool that receives a source and destination IP addresses to listen for TCP connections and what approach for throttling should be used. The tool should be executed in a third node with access to the traffic. Whenever such a packet is captured, RST or 3 ACK packets should be sent back to the origin and/or destination.
For the experimental setup, you can try using virtual machines, or leveraging the VM used for practical exercises as a malicious node to interfere with connections between the host machine and another device.
Collect experimental evidence of the malicious behavior through Wireshark, and screenshots of the time taken to transmit a file using a file transfer (FTP or SSH) to show that it is indeed slower or interrupted when under attack.

### 3. Mini TLS-based VPN tunneling

For this part, less familiarity with low-level networking programming details is necessary. In particular, this [SEED lab](https://seedsecuritylabs.org/Labs_20.04/Networking/VPN_Tunnel/) has starting code for reference.
The objective of this task is to implement a small VPN tunneling program that will allow hosts to communicate over an encrypted connection. Follow the tutorial from the SEED lab above up to Task 5 (while ignoring the instructions to write a report) until you have a functional implementation able to transmit unencrypted traffic.

Your task is then to finalize the implementation by replacing the UDP socket with a TLS/SSL connection. A simple certificate structure must be deployed, where a self-signed certificate will authenticate the server certificate and be available on the client side as well.
Collect evidence of the correct behavior through Wireshark and screenshots showing that traffic is correctly forwarded.
You are not supposed to write your own TLS/SSL implementation and a library should be used for that.

## Logistics:

Your source code and binaries should be submitted through Brightspace, in groups of at most 3 students. Please including compile and usage instructions. The software package should be followed by a single short report (up to 5 pages, free format) describing your design decisions for the multiple parts and documenting the experimental evidence requested above. Deadline is 1/11/2021.

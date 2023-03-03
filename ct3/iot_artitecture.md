# CT -3 Important topics

## Explain MQTT protocol architecture and its function in detail

MQTT stands for message queueing telemetry transport protocol.

- MQTT follows the PUB/SUB model.
- Publish mechanism is used to publish messages.
- Subscribe is used to receive messages.
- Any client can publish messages to any other client that has subscribed to the messages.
- Endpoints can be setup to publish and subscribe to specific messages. (device/temperature)
- The message itself is called payload.

## Write short notes UDP, TCP protocols

Whenever a computer wants to communicate with another computer, the communication between those two computers needs to be good and reliable so we can guarantee that the data is received correctly. For example, when you want to view a webpage or download a file, or look at an email, you'd expect to view the webpage intact and in order with nothing missing, or if you're downloading a file, you'd want the entire file and not just a part of the file, because if data is missing or out of order, then it wouldn't be of any benefit to you.

TCP stands for transmission protocol and is one of the main protocols used in a TCP/IP network. TCP is what is used to guarantee that all the data is received and in order, because without TCP, then some of the data could be missing or out of order. Because if you view a webpage without TCP, you're webpage could be all messed up. The images could be missing, or the text could be backwards or out of order. Or if you download a file, then you might not get the entire file or you could get the file out of order, which would render the file useless. TCP is a connection oriented protocol which basically means that it must first acknowledge a session between the two computers that are communicating, so the two computers verify a connection before any communication takes place. It does this by using a three-way handshake.

- A computer sends a SYN message.
- The receiving computer sends back an acknowledgement message SYN ACK, saying it received the message.
- The sender sends another SYN ACK acknowledgement back to the receiver.

Once this has taken place, data can be delivered. TCP guarantees the delivery of the data. If a data packet goes astray and doesn't arrive, TCP will resend it.

UDP is very similar to TCP. UDP is also for sending and receiving data. The main difference is that UDP is connectionless, which means that it does not establish a session and does not guarantee data delivery. When a computer sends their data, it doesn't care whether the data is received at the other end. It is known as fire-and-forget protocol, because it sends data and doesn't really care what happens to it. Another point to remember is because of the less overhead that's involved of not guaranteeing data delivery, UDP is faster than TCP.

## Explain the different types of attacks in IoT applications

- Distributed denial of service (DDoS): A DDoS attack occurs when a botnet - a network of computers - consistently and simultaneously requests services from a business. This extreme demand shuts the system down as it tries to serve the requests.
- Firmware exploits: Many cybercriminals use known vulnerabilities. Often, these vulnerabilities have patches available from the developer, but the user hasn't downloaded them, leaving them open to the hack.
- Man-in-the-middle: In this type of IoT attack, the hacker intercepts the communication between two connected systems. The victim may believe they're legitimately communicating with someone, but they're actually leaking information to the hacker.
- Data interception: Since many IoT devices are not encrypted, attackers can snag information, such as login credentials, without needing to decrypt it.
- Physical attacks: Simply plugging a USB into an IoT device can be enough to spread malware to a network or spy on the communications.
- Brute force attacks: Just as passwords can be brute-forced, many IoT devices can be hacked with a system that generates password guesses until it gets through.
- Unauthorized access: With so many interconnected IoT devices, intrusion can lead to serious physical breaches. An IoT-enabled door lock may sound incredibly convenient until it lacks sufficient security and leads to an office break-in.
- Ransomware: Ransomware blocks access to a system until the hacker is paid. IoT devices can grant access to the larger system or be locked themselves.
- Radio frequency jamming: By interfering with radio signals, hackers can prevent IoT devices from communicating.

## Explain Transport layer protocols in detail

- TCP - Transmission Control Protocol (TCP) is connection oriented and heavyweight protocol. It is suitable for reliable communication because in this protocol acknowledgment is received when the client sends the packet to the server via TCP protocol. The data must be guaranteed sent at the other end if the packet is sent via TCP protocol.
- MPTCP - MPTCP is an evolutionary step forward for the TCP protocol to enable redundancy for multiple network connections for any device. MPTCP can effectively use multiple paths within a single transport connection and keep a logical connection established when the endpoint's address changes. By bringing redundancy to user endpoint devices, MPTCP is feeding the thirst for users who want to be connected all the time and every time they pick up their device.
- UDP - User Datagram Protocol is a connection less protocol and is not reliable for guaranteed transmission of data. However, the UDP protocol is a best protocol to send data to the server when packet loss during transmission of the data can be afforded. UDP protocol is a lightweight protocol and is suitable for wireless sensor network communication. UDP is often used in applications specially tuned for real-time performance.
- DCCP - Datagram Congestion Control Protocol (DCCP) is a message-oriented transport layer protocol. This protocol is more secure than TCP protocol. Compared to TCP which has a single byte long ID for each packet, the packet ID is 48-bit long (6-bytes) in DCCP. This makes it hard for any attacker to hack data packets. This protocol is generally used for time critical data transfers like media streaming and VoIP.
- SCTP - Stream Control Transmission Protocol (SCTP) protocol is a message oriented transport layer protocol and it uses congestion control to reliably transfer data over a network. The data transferred along with a 12-byte header is secured using 4-way handshake. Due to multi-homing, data is reliably sent to the destination.
- TLS - Transport Layer Security (TLS) is a security protocol which uses symmetric cryptography to secure data. This protocol has been now prohibited from use due to security considerations.
- DTLS - Based on Transport Layer Security (TLS) protocol, Datagram Transport Layer Security (DTLS) is a stream oriented transport layer protocol. This is a security protocol designed against message forgery, tampering and eavesdropping. However, large packet size, packet reordering and loss of datagram are some of the major drawbacks of this protocol stack.

## Write Short notes XMPP, AMQP

### XMPP

XMPP is a short form for Extensible Messaging Presence Protocol. It's protocol for streaming XML elements over a network in order to exchange messages and presence information in close to real time. This protocol is mostly used by instant messaging applications like WhatsApp.

Let's dive into each character of word XMPP:

- X - Extensible : XMPP is a open source project which can be changed or extended according to the need.
- M - Messaging : XMPP is designed for sending messages in real time. It has very efficient push mechanism compared to other protocols.
- P - Presence : It determines whether you are online/offline/busy. It indicates the state.
- P - Protocol : XMPP is a protocol, that is, a set of standards that allow systems to communicate with each other.

These are the basic requirements of any Instant Messenger which are fulfilled by XMPP:

- Send and receive messages with other users.
- Check and share presence status
- Manage subscriptions to and from other users.
- Manage contact list
- Block communications(receive message, sharing presence status, etc) to specific users.

Decentralised: XMPP is based on client-server architecture, i.e. clients don't communicate directly, they do it with the help of server as intermediary. It is decentralised means there is no centralised XMPP server just like email, anyone can run their own XMPP server.

### AMQP

AMQP refers to Advanced Message Queuing Protocol. It is mainly used for developing unmatched communication operability between client and broker parties. The publisher bears the responsibility of message generation while clients collect and administer them. The role of brokers, in this whole process is to make a sure message, part of the exchange, goes directly from the publisher to the client.

While one plans to bring AMQP into action, getting to know some of its key terminologies is imperative.

- Broker (or server) plays a crucial role in AMQP protocol enablement. It is responsible for connection building that ensure better data routing and queuing at the client-side.
- The job of queues generation and message acknowledgement is taken care of by consumer.
- Redirection of data taken from exchanges and its placement in queues is taken care of by producer.

Components of AMQP:

- Exchanges: Exchange handles the responsibility of fetching messages and placing them carefully in the right queue. Its 4 categories are: Fanout, Headers, Topic, and Direct. To detail you on it further, it is an indispensable component of the broker.
- Channel: Channel refers to a multiplexed virtual connection among AMQP peers, which is built inside an existing connection.
- Message Queue: It is an identified entity that helps link messages with their resources or point of origin.
- Binding: Bindings denote a set of predefined instructions related to queues as well as exchanges. It administers the sending of message and their delivery.
- Virtual Hosts: vhost is a platform offering the segregation facility inside the broker. Based upon users and their access rights, there could be multiple vhost functional at a time.

## Discuss the Service layer security protocols in detail

The below protocols make use of IPv6 which is more secure than IPv4 by default. The protocols provide additional security features.

- MAC IEEE 802.15.4: The Media Access Control (MAC) layer, specified by IEEE 802.15.4, is located between the physical and network layers. The MAC layer performs the following functions:
  - Transfers data to the network layer and vice versa; transfers data to the physical layer and vice versa
  - End device association and disassociation
  - In the coordinator, offers optional guaranteed time slot (GTS) for each device accessing the network
  - Generates the beacon frame in a coordinator
  - Supports device security
  - Provides carrier-sense multiple access with collision avoidance (CSMA/CA) as the access method for the network
  - Provides a reliable connection between two MAC layers by using an acknowledgment
- 6LoWPAN: 6LoWPAN is an IPv6 protocol, and It's extended from is IPv6 over Low Power Personal Area Network. It comprises an Edge Router and Sensor Nodes. Even the smallest of the IoT devices can now be part of the network, and the information can be transmitted to the outside world as well. For example, LED Streetlights.

  Features of 6LoWPAN:

  - It is used with IEEE 802.15,.4 in the 2.4 GHz band.
  - Outdoor range: ~200 m (maximum)
  - Data rate: 200kbps (maximum)
  - Maximum number of nodes: ~100

  Advantages of 6LoWPAN:

  - 6LoWPAN security is ensured by the AES algorithm, which is a link layer security, and the transport layer security mechanisms are included as well.
  - 6LoWPAN is a mesh network that is robust, scalable, and can heal on its own.
  - It delivers low-cost and secure communication in IoT devices.
  - It uses IPv6 protocol and so it can be directly routed to cloud platforms.
  - It offers one-to-many and many-to-one routing.
  - In the network, leaf nodes can be in sleep mode for a longer duration of time.

- RPL: RPL stands for Routing Protocol for Low Power and Lossy Networks for heterogeneous traffic networks. It is a routing protocol for Wireless Networks. This protocol is based on the same standard as by Zigbee and 6 Lowpan is IEEE 802.15.4 It holds both many-to-one and one-to-one communication.

  In an RPL Network, each node acts as a router and becomes part of a mesh network. Routing is performed at the IP Layer. Each node examines every received IPv6 packet and determines the next-hop destination based on the information contained in the IPv6 header. No information from the MAC layer header is needed to perform the next determination.

## Explain the Application layer security protocols in detail

- [MQTT](https://github.com/DEEJ4Y/iot-archs---protocols/blob/main/CT-3.md#explain-mqtt-protocol-architecture-and-its-function-in-detail)
- HTTP - Token based authentication: With token-based authentication, the application validates a user's credentials on their first login, then provides the client with a signed token. The client stores the token and then must provide it with every login request, helping to prevent against CSRF(Cross Site Request Forgery) attacks (where unauthorized commands are transmitted from a user that the application trusts).

  Most protocols will have both a standard version and a secure version. While the standard version will be more lightweight and less secure, the secure version will be more complex, likely based on DLS, and offer more protection.

- Encryption: Due to the structure of all the layers, an attack at a given layer can affect all of the layers above it, though not the ones below. And while it's critical to secure the transport layer and those other deeper layers on their own, you shouldn't always rely on those layers to handle all your encryption. If for some reason an attacker exploits a vulnerability in the transport layer, data not encrypted at the application layer could be suddenly available.

  For this reason, it's always a good idea to follow best practices for encrypting your data at the application layer to avoid unplanned exposure.

- Firewalls: You can also use application firewalls to guard your application layer, plus other layers as well. Keep in mind that most firewalls are built with specific applications in mind, though many firewalls can be configured for multiple applications.

  The firewall can control all network traffic on any OSI layer up to the application layer. Basically, it makes sure that weird connections aren't happening in places you don't expect, and that all communications are following the desired protocols.

## Discuss the challenges faced by IoT systems

- Unpredictable conduct:
  There is a huge amount of deployed devices with enabling technologies. This means that their behaviour in any sector can be unpredictable. The system may have a proper design and structure with a reformed administration but one cannot predict its interaction with other systems.
- Similar devices:
  There are not many options for IoT devices and most of them are fairly similar. They make use of the same connection and network protocols. If one device gets a DDoS attack, it affects the rest of the devices too.
- Difficult deployment:
  Deployment is a difficult process in IoT devices considering the fact that there are too many devices with internet connection. IoT aims to advance to areas and networks where it was impossible to enter before. These devices produce data every second. This creates difficulties in deploying devices.
- Long device life and expired support:
  One of the major advantages of IoT devices is their extremely long life. However, this could mean that the working of IoT devices extends beyond their support and warranty periods. These devices lack security and are open sights for cybercriminals.
- No upgradation support:
  Upgrades and modifications are not possible in many IoT devices. Many times the upgrades are difficult to enforce or go unnoticed by the users.
- Poor or zero transparency:
  Iot devices have a reserved functionality, meaning there is no access to the inner working of IoT devices directly. Users can only assume the working of their devices as access to the inner components is not possible. They cannot control the data flow and information collection which leads to obtaining unnecessary information by the device.

## Discuss IoT security protocol 6LoWPAN in detail

6LoWPAN is an IPv6 protocol, and It's extended from is IPv6 over Low Power Personal Area Network. 6LoWPAN allows communication using the IPv6 protocol.

It comprises an Edge Router and Sensor Nodes. Even the smallest of the IoT devices can now be part of the network, and the information can be transmitted to the outside world as well. For example, LED Streetlights.

- It is a technology that makes the individual nodes IP enabled.
- 6LoWPAN can interact with 802.15.4 devices and also other types of devices on an IP Network. For example, Wi-Fi.
- It uses AES 128 link layer security, which AES is a block cipher having key size of 128/192/256 bits and encrypts data in blocks of 128 bits each. This is defined in IEEE 802.15.4 and provides link authentication and encryption.

Basic Requirements of 6LoWPAN:

- The device should be having sleep mode in order to support the battery saving.
- Minimal memory requirement.
- Routing overhead should be lowered.

Features of 6LoWPAN:

- It is used with IEEE 802.15,.4 in the 2.4 GHz band.
- Outdoor range: ~200 m (maximum)
- Data rate: 200kbps (maximum)
- Maximum number of nodes: ~100

Advantages of 6LoWPAN:

- 6LoWPAN is a mesh network that is robust, scalable, and can heal on its own.
- It delivers low-cost and secure communication in IoT devices.
- It uses IPv6 protocol and so it can be directly routed to cloud platforms.
- It offers one-to-many and many-to-one routing.
- In the network, leaf nodes can be in sleep mode for a longer duration of time.

Disadvantages of 6LoWPAN:

- It is comparatively less secure than Zigbee.
- It has lesser immunity to interference than that Wi-Fi and Bluetooth.
- Without the mesh topology, it supports a short range.

Applications of 6LoWPAN:

- It is a wireless sensor network.
- It is used in home-automation,
- It is used in smart agricultural techniques, and industrial monitoring.

Security and Interoperability with 6LoWPAN:

- Security: 6LoWPAN security is ensured by the AES algorithm, which is a link layer security, and the transport layer security mechanisms are included as well.
- Interoperability: 6LoWPAN is able to operate with other wireless devices as well which makes it interoperable in a network.

## Discuss the Security applications and issues in RPL

RPL standard offers three modes of security to
ensure control messages' confidentiality and integrity:

- UM: where only the link-layer security is applied, if available(default mode)
- PSM: which uses preinstalled symmetrical encryption keys to secure RPL control messages
- ASM: uses the preinstalled keys to let the nodes join the network, after that all routing-capable nodes must acquire new keys from an authentication authority.

In addition, RPL providesan optional replay protection mechanism that employs the use of Consistency Check (CC) messages, only available in the preinstalled (PSMrp) or authenticated mode (ASMrp). PSM is able to mitigate most of the external attacks, while it does not enhance RPL's security against the internal attacks. Furthermore, external adversaries still can launch replay attacks, even when PSMrp is used.

RPL standard only provides confidentiality and integrity of its control messages, without any verification of their authenticity. This opens the door wide open for attacks such as message-forging, identity-cloning, eavesdropping, and replay attacks to be launched regardless which RPL secure mode is running.

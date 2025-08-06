# 🔍 NetReconX

**NetReconX** is a modular Python-based network reconnaissance tool built for Termux and Linux. It automates the process of gathering intelligence about a domain or IP address — making it a valuable tool for ethical hackers, penetration testers, and cybersecurity researchers.

---

## 🚀 Features

- 🌐 WHOIS Lookup
- 🛰️ IP Geolocation
- 🛠️ Port Scanner
- 📡 DNS Records Fetcher
- 🕵️‍♂️ Subdomain Enumeration (brute-force based)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/NetReconX.git
cd NetReconX
pip install -r requirements.txt
```

---

## 🧠 Usage

```bash
python recon.py --target example.com
```

Result is saved in:

- output/report.json


---

## 📄 Sample Output (report.json)

{
  "whois": {
    "domain_name": "CLOUDFLARE.COM",
    "registrar": "Cloudflare, Inc.",
    "creation_date": "2009-02-17",
    ...
  },
  "ip_lookup": {
    "ip": "104.16.132.229",
    "country": "United States",
    ...
  },
  "port_scan": {
    "open_ports": [80, 443]
  },
  "dns_records": {
    "A": [...],
    "MX": [...],
    ...
  },
  "subdomains": {
    "discovered_subdomains": [
      "http://www.cloudflare.com",
      "http://mail.cloudflare.com"
    ]
  }
}


---

## 📂 Wordlist

You can modify the default wordlist in wordlists/subdomains.txt to include more subdomains.


---

## 🤝 Contribution

Pull requests and forks are welcome. Feel free to suggest or implement:

Directory/file brute-forcing

Shodan integration

Screenshot capture of found subdomains

Telegram bot notifications



---

## ⚠️ Legal Disclaimer

This tool is for educational and authorized security testing only. Usage on targets without permission is illegal and unethical.


---

## 💡 Credits

- Built with ❤️ in Termux.

---
# NetReconX

import argparse
import json
import os
from modules.whois_lookup import run_whois
from modules.ip_lookup import run_ip_lookup
from modules.port_scanner import run_port_scan
from modules.dns_scan import run_dns_scan
from modules.subdomain_finder import run_subdomain_finder

def save_output(data, filename="output/report.json"):
    os.makedirs("output", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="NetReconX - Network Reconnaissance Tool")
    parser.add_argument("--target", required=True, help="Target domain or IP address")
    args = parser.parse_args()

    print(f"[+] Running recon on: {args.target}")
    result = {}

    # WHOIS Lookup
    print("[*] Running WHOIS lookup...")
    result["whois"] = run_whois(args.target)

    # IP Lookup
    print("[*] Running IP geolocation lookup...")
    result["ip_lookup"] = run_ip_lookup(args.target)

    # Port Scanner
    print("[*] Scanning common ports...")
    result["port_scan"] = run_port_scan(args.target)

    # Dns Scan
    print("[*] Fetching DNS records...")
    result["dns_records"] = run_dns_scan(args.target)
   
    # Subdomain Finder
    print("[*] Running subdomain enumeration...")
    result["subdomains"] = run_subdomain_finder(args.target)


    # More modules will come here later

    save_output(result)

if __name__ == "__main__":
    main()

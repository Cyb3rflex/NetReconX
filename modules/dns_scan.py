import dns.resolver

def get_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]
    except:
        return []

def run_dns_scan(domain):
    return {
        "A": get_records(domain, "A"),
        "MX": get_records(domain, "MX"),
        "NS": get_records(domain, "NS"),
        "TXT": get_records(domain, "TXT"),
    }

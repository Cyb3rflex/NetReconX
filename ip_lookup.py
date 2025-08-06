import socket

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return domain

def run_ip_lookup(target):
    try:
        ip = resolve_ip(target)
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name"),
            "org": data.get("org"),
            "asn": data.get("asn"),
            "timezone": data.get("timezone"),
        }

    except Exception as e:
        return {"error": str(e)}

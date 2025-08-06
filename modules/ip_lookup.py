import requests

def run_ip_lookup(target):
    try:
        response = requests.get(f"https://ipapi.co/{target}/json/")
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

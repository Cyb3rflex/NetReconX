import requests

def run_subdomain_finder(domain, wordlist_path="wordlists/subdomains.txt"):
    found = []

    try:
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()

        for sub in subdomains:
            url = f"http://{sub}.{domain}"
            try:
                response = requests.get(url, timeout=2)
                if response.status_code < 400:
                    found.append(url)
            except:
                continue

    except FileNotFoundError:
        return {"error": "Wordlist not found"}

    return {"discovered_subdomains": found if found else "None found"}

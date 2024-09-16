pip install requests

import requests
import json

# Set Up Metasploit API Connection
METASPLOIT_URL = "http://localhost:55552/api/v1"
METASPLOIT_TOKEN = "your_metasploit_api_token"

def metasploit_request(endpoint, method="GET", data=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {METASPLOIT_TOKEN}"
    }
    url = f"{METASPLOIT_URL}/{endpoint}"
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Scanning Function
def scan_network(target):
    data = {
        "workspace": "default",
        "hosts": target,
        "port": "1-1024",
        "threads": 10
    }
    response = metasploit_request("modules/auxiliary/scanner/portscan/tcp", "POST", data)
    return response

# Reporting Function
def generate_report():
    response = metasploit_request("reports")
    return response

# Main Function to Run the Tool
if __name__ == "__main__":
    target = input("Enter the target IP address or range: ")
    print("Scanning network...")
    scan_result = scan_network(target)
    print(scan_result)

    exploit = input("Enter the exploit to use: ")
    payload = input("Enter the payload to use: ")
    print("Exploiting target...")
    exploit_result = exploit_target(target, exploit, payload)
    print(exploit_result)

    print("Generating report...")
    report = generate_report()
    print(report)

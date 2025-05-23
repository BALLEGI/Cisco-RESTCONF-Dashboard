import requests
import json
from requests.auth import HTTPBasicAuth

# Configuration RESTCONF
ROUTER_IP = "192.168.231.139"  # À adapter selon votre routeur
USERNAME = "admin"
PASSWORD = "cisco123"
BASE_URL = f"https://{ROUTER_IP}/restconf"
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
AUTH = HTTPBasicAuth(USERNAME, PASSWORD)

# Désactiver les avertissements SSL (à ne pas faire en production)
requests.packages.urllib3.disable_warnings()

# 1. Récupérer la configuration d'une interface
def get_interface_config(interface_name):
    url = f"{BASE_URL}/data/ietf-interfaces:interfaces/interface={interface_name}"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    return response.json()

# 2. Exporter la table de routage
def export_routing_table():
    url = f"{BASE_URL}/data/ietf-routing:routing-state"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    data = response.json()
    with open("routing_table.json", "w") as f:
        json.dump(data, f, indent=2)
    return data

# 3. Afficher les interfaces réseau
def show_ip_interface_brief():
    url = f"{BASE_URL}/data/ietf-interfaces:interfaces"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    return response.json()

# 4. État de marche d’une interface
def get_interface_status(interface_name):
    url = f"{BASE_URL}/data/ietf-interfaces:interfaces-state/interface={interface_name}"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    return response.json()

# 5. Récupérer l'utilisation CPU/mémoire
def get_cpu_memory_usage():
    url = f"{BASE_URL}/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    return response.json()

# 6. Récupérer l'état du STP
def get_stp_status():
    url = f"https://{ROUTER_IP}/restconf/data/Cisco-IOS-XE-native:native/spanning-tree"
    response = requests.get(url, headers=HEADERS, auth=AUTH, verify=False)
    return response.json()


from flask import Flask, render_template, request, send_file
from restconf_utils import (
    get_interface_config,
    export_routing_table,
    show_ip_interface_brief,
    get_interface_status,
    get_cpu_memory_usage,
    get_stp_status
)
import os
import json

app = Flask(__name__)

def get_interface_names():
    data = show_ip_interface_brief()
    interfaces = data.get("ietf-interfaces:interfaces", {}).get("interface", [])
    return [iface["name"] for iface in interfaces]

def save_json_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    interfaces = get_interface_names()
    return render_template('index.html', interfaces=interfaces)

@app.route('/interface-config', methods=['POST'])
def interface_config():
    interface = request.form['interface']
    config = get_interface_config(interface)
    interfaces = get_interface_names()
    filename = f"interface_config_{interface}.json"
    save_json_to_file(config, filename)
    return render_template('index.html', result=config, title=f"Configuration de {interface}", interfaces=interfaces, download_file=filename)

@app.route('/routing-table')
def routing_table():
    data = export_routing_table()
    interfaces = get_interface_names()
    filename = "routing_table.json"
    save_json_to_file(data, filename)
    return render_template('index.html', result=data, title="Table de routage exportée", interfaces=interfaces, download_file=filename)

@app.route('/interfaces')
def interfaces():
    data = show_ip_interface_brief()
    interfaces = get_interface_names()
    filename = "interfaces.json"
    save_json_to_file(data, filename)
    return render_template('index.html', result=data, title="Interfaces réseau", interfaces=interfaces, download_file=filename)

@app.route('/interface-status', methods=['POST'])
def interface_status():
    interface = request.form['interface']
    status = get_interface_status(interface)
    interfaces = get_interface_names()
    filename = f"interface_status_{interface}.json"
    save_json_to_file(status, filename)
    return render_template('index.html', result=status, title=f"État de {interface}", interfaces=interfaces, download_file=filename)

@app.route('/cpu-memory')
def cpu_memory():
    data = get_cpu_memory_usage()
    interfaces = get_interface_names()
    filename = "cpu_memory_usage.json"
    save_json_to_file(data, filename)
    return render_template('index.html', result=data, title="Utilisation CPU/Mémoire", interfaces=interfaces, download_file=filename)

@app.route('/stp-status')
def stp_status():
    data = get_stp_status()
    interfaces = get_interface_names()
    filename = "stp_status.json"
    save_json_to_file(data, filename)
    return render_template('index.html', result=data, title="État du STP", interfaces=interfaces, download_file=filename)

# Route générique pour télécharger les fichiers JSON
@app.route('/download-json/<filename>')
def download_json(filename):
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        return "Fichier non trouvé", 404

if __name__ == '__main__':
    app.run(debug=True)

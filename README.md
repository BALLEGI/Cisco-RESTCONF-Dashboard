# Cisco-RESTCONF-Dashboard

RAPPORT TECHNIQUE – APPLICATION FLASK RESTCONF

INTRODUCTION
Cette application web a été développée dans le cadre de la supervision et de l'administration réseau à distance à l’aide de l’API RESTCONF. Elle permet d’interagir avec un routeur Cisco IOS-XE afin d’effectuer différentes opérations telles que l’export de la table de routage, l’affichage des interfaces réseau, la récupération de la configuration d’une interface, l’état de fonctionnement, les statistiques CPU/Mémoire et le statut du protocole STP (Spanning Tree Protocol).

TECHNOLOGIES UTILISÉES
- Python 3
- Flask (micro-framework web)
- RESTCONF API (Cisco IOS-XE)
- HTTP Basic Auth
- Templates HTML avec Jinja2
- JSON pour les échanges de données
- HTTPS (non sécurisé en développement)

STRUCTURE DES FICHIERS

1. app.py
Ce fichier constitue le point d’entrée de l’application Flask. Il définit plusieurs routes permettant d’interagir avec les fonctionnalités RESTCONF exposées dans restconf_utils.py.

Principales routes :
- / : page d’accueil avec liste des interfaces.
- /interface-config : récupération de la configuration d’une interface.
- /routing-table : export de la table de routage.
- /interfaces : affichage des interfaces réseau.
- /interface-status : état opérationnel d’une interface.
- /cpu-memory : affichage de l'utilisation CPU/mémoire.
- /stp-status : état du STP.
- /download-json/<filename> : téléchargement des fichiers JSON générés.

2. restconf_utils.py
Ce fichier contient les fonctions de communication RESTCONF avec le routeur Cisco :

Fonctions disponibles :
- get_interface_config(interface_name)
- export_routing_table()
- show_ip_interface_brief()
- get_interface_status(interface_name)
- get_cpu_memory_usage()
- get_stp_status()

Les appels HTTP sont réalisés avec le module requests, avec authentification de base et désactivation des vérifications SSL (à ne pas faire en production).

FONCTIONNALITÉS PRINCIPALES

| Fonctionnalité              | Description |
|----------------------------|-------------|
| Liste des interfaces       | Récupère dynamiquement les interfaces disponibles via RESTCONF. |
| Config. d'une interface    | Affiche et télécharge la configuration d’une interface sélectionnée. |
| Table de routage           | Récupère et exporte la table de routage du routeur. |
| Interfaces réseau          | Liste toutes les interfaces avec leurs détails. |
| État interface             | Montre l’état opérationnel (up/down) d’une interface donnée. |
| CPU/Mémoire                | Affiche les statistiques CPU et mémoire du routeur. |
| STP                        | Récupère l’état du Spanning Tree Protocol. |

REMARQUES & RECOMMANDATIONS
- Le certificat SSL est désactivé (verify=False), ce qui est toléré en phase de test mais à sécuriser en production.
- Les identifiants sont en clair dans restconf_utils.py. Il est préférable d’utiliser des variables d’environnement ou un fichier .env.
- La persistance des fichiers JSON dans le répertoire courant est fonctionnelle mais devrait être sécurisée (accès restreint, nettoyage automatique, etc.).

CONCLUSION
Cette application démontre comment un administrateur peut superviser un équipement Cisco à distance via une interface web intuitive, en utilisant les capacités RESTCONF. Elle constitue un bon point de départ pour construire un tableau de bord plus avancé ou intégrer des systèmes d’automatisation réseau.

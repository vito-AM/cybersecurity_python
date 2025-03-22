# Mon Pack de Projets Cyber

Ce dépôt GitHub rassemble l’ensemble de mes projets liés à la cybersécurité, au développement web et à la gestion de mots de passe. Chaque projet est placé dans son propre répertoire pour faciliter l’exploration du code et la compréhension de sa finalité.

## Table des Matières
1. [Key Logger](#key-logger)  
2. [ARP Spoofing & DNS Spoofing](#arp-spoofing--dns-spoofing)  
3. [MAC Changer](#mac-changer)  
4. [Port Scanner](#port-scanner)  
5. [Casseur de Mots de Passe (MD5)](#casseur-de-mots-de-passe-md5)  
6. [Password Manager (Gestionnaire de Mots de Passe)](#password-manager)  
7. [Outil de Forensique (PDF/EXIF/Firefox)](#outil-de-forensique)  
8. [Scanner de Vulnérabilités Web (Interface Graphique)](#scanner-de-vulnérabilités-web)  

---

## Key Logger
- **Répertoire** : `key_logger`
- **Description** : Enregistre les frappes clavier en temps réel et les stocke dans un fichier log (horodatage inclus).
- **Technologies** : Python, `pynput`, `logging`
- **Usage** : 
  ```bash
  cd key_logger
  python3 key_logger.py
  ```
- **Disclaimer** : Usage **strictement réservé** à un cadre autorisé (démonstration, test de sécurité).

---

## ARP Spoofing & DNS Spoofing
- **Répertoire** : `arp_dns_spoofer`
- **Description** : Scripts illustrant des attaques de type Man-in-the-Middle via ARP poisoning et DNS spoofing.
- **Technologies** : Python, `scapy`, `netfilterqueue`
- **Usage** :
  - ARP Spoofer : `python3 arp_spoof.py`
  - DNS Spoofer : `python3 dns_spoof2.py`
- **Attention** : Nécessite souvent des **droits root** et la configuration de règles iptables sous Linux.

---

## MAC Changer
- **Répertoire** : `mac_changer`
- **Description** : Script permettant de modifier l’adresse MAC d’une interface réseau (pour des tests d’évasion ou de vie privée).
- **Technologies** : Python, `subprocess`, `re`
- **Usage** :
  ```bash
  cd mac_changer
  python3 mac_changer.py -i <interface> -m <nouvelle_mac>
  ```
- **Conditions** : Peut requérir des **droits administrateur** pour ifconfig.

---

## Port Scanner
- **Répertoire** : `port_scanner`
- **Description** : Scanne rapidement les premiers ports d’une machine donnée pour identifier ceux qui sont ouverts.
- **Technologies** : Python, `socket`
- **Usage** : 
  ```bash
  cd port_scanner
  python3 port_scanner.py
  ```
  (Saisir ensuite l’IP à scanner)
- **Note** : Se limite aux ports 1 à 1024, approche **basique** d’un scan TCP (connect_ex).

---

## Casseur de Mots de Passe (MD5)
- **Répertoire** : `md5_cracker`
- **Description** : Illustrations de différentes méthodes pour casser des hachages MD5 (dictionnaire, brute force, pattern matching, recherche en ligne).
- **Technologies** : Python, `hashlib`, `multiprocessing`, `argparse`
- **Usage** : 
  ```bash
  cd md5_cracker
  python3 crack.py -md5 <hash> -f <fichier_dictionnaire>
  ```
  (ou les autres options `-l`, `-o`, `-p` selon la méthode choisie)
- **Attention** : **Éthique & Légal** : seulement pour des tests en environnement autorisé.

---

## Password Manager
- **Répertoire** : `password_manager`
- **Description** : Gestionnaire de mots de passe local, utilisant un fichier chiffré (Fernet) et un `master.key`. Permet également de générer des mots de passe aléatoires.
- **Technologies** : Python, `cryptography.fernet`, `stdiomask`
- **Usage** : 
  ```bash
  cd password_manager
  python3 main.py
  ```
  - Au premier lancement, génère le `master.key` et `coffre.txt`.
  - Sauvegarde, lit et chiffre/déchiffre les mots de passe.

---

## Outil de Forensique (PDF/EXIF/Firefox)
- **Répertoire** : `pdf_meta`
- **Description** : Script d’analyse de métadonnées PDF (PyPDF2), extraction de chaînes de caractères, récupération de données EXIF/GPS, et lecture d’historiques/cookies Firefox.
- **Technologies** : Python, `PyPDF2`, `exifread`, `sqlite3`
- **Usage** : 
  ```bash
  cd pdf_meta
  python3 pdf_meta.py -pdf <fichier.pdf>
  ```
  (puis différentes options : `-exif`, `-gps`, `-fh` pour l’historique Firefox, etc.)

---

## Scanner de Vulnérabilités Web
- **Répertoire** : `web_scanner`
- **Description** : Crawler et recherche automatique de failles (XSS, SQLi) avec interface graphique générée par PAGE. Génération de rapports HTML.
- **Technologies** : Python, `requests`, `BeautifulSoup`, `tkinter`, `threading`, `multiprocessing`
- **Usage** :
  ```bash
  cd web_scanner
  python3 gui.py
  ```
  - Entrez l’URL cible, lancez le scan, visualisez les liens découverts et les vulnérabilités détectées.
  - Tests réalisés sur **Metasploitable** pour valider l’approche.

---

## Site E-Commerce Fictif
- **Répertoire** : `ecommerce_site`
- **Description** :  
  - Gestion des utilisateurs (inscription/connexion).  
  - Panier d’achat dynamique et intégration de **Stripe** pour les paiements sécurisés.  
  - Bonnes pratiques en cybersécurité (validation des entrées, prévention XSS/CSRF, protection des données sensibles).  
  - Chatbot avec filtrage contextuel (TF-IDF, Word2Vec, LSTM, clustering).  
- **Technologies** : PHP, HTML/CSS, JavaScript (AJAX, jQuery), MySQL, Flask, Keras
- **Notes** : Le code complet est très volumineux, mais illustre la **fusion** entre développement web, sécurité et intelligence artificielle.

---

# Installation & Usage

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/MonCompte/mon_pack_de_projets.git
   cd mon_pack_de_projets
   ```
2. **Naviguer** dans chaque sous-dossier pour découvrir les projets et lire le README/les instructions spécifiques.
3. **Environnements & dépendances** :  
   - Principalement du **Python 3.x**.  
   - Certaines bibliothèques (ex. `scapy`, `requests`, `cryptography`) peuvent nécessiter une installation via `pip install -r requirements.txt` (un fichier requirements global ou un par projet).  
   - Pour les projets web (PHP/MySQL), configure un serveur local (ex. XAMPP, LAMP, etc.).

---

# Avertissement Légal

La plupart de ces scripts sont des **outils de sécurité** (key logger, spoofing, scanner de vulnérabilités) et ne doivent être utilisés **que dans un environnement autorisé** (tests en labo, pentesting contractuel, formation). L’auteur décline toute responsabilité en cas d’utilisation illégale ou malveillante.

---

# Contributions

Ce dépôt a initialement été créé pour présenter ma **démarche d’apprentissage** et mes **compétences** en cybersécurité et développement. Toute suggestion ou contribution est la bienvenue via des **Issues** ou des **Pull Requests**.

---

# Contact

Pour plus d’informations, vous pouvez me joindre via [mon profil GitHub](https://github.com/vito-AM.com)

Merci pour votre intérêt et bonne exploration !

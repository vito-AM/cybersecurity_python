#!/usr/local/bin/python3

import os.path
import sys
import subprocess
import random
import string
import cryptography.fernet
import stdiomask

def generer_mdp_maitre():
    clef = cryptography.fernet.Fernet.generate_key()
    with open("./master.key", "wb") as masterPasswordWriter:
        masterPasswordWriter.write(clef)

def charger_mdp_maitre():
    return open("./master.key", "rb").read()

def creer_coffre():
    coffre = open("./coffre.txt", "wb")
    coffre.close()

def chiffrer_donnees(donnees):
    f = cryptography.fernet.Fernet(charger_mdp_maitre())
    with open("./coffre.txt", "rb") as lecteur_coffre:
        donnees_chiffre = lecteur_coffre.read()
    if donnees_chiffre.decode() == "" :
        return f.encrypt(donnees.encode())
    else:
        donnees_dechiffre = f.decrypt(donnees_chiffre)
        nouvelles_donnees = donnees_dechiffre.decode() + donnees
        return f.encrypt(nouvelles_donnees.encode())

def dechiffrer_donnees(donnees_chiffre):
    f = cryptography.fernet.Fernet(charger_mdp_maitre())
    return f.decrypt(donnees_chiffre)

def verification():
    if os.path.exists("coffre.txt"):
        pass
    else:
        file = open("coffre.txt", "w")
        file.close()

def ajout_nouveau_mdp():
    print()
    nom_utilisateur = input("Veuillez rentrer un nom d'utilisateur : ")
    mdp = stdiomask.getpass(prompt="Veuillez rentrer un mot de passe  : ", mask="*")
    site_web = input("Veuillez entrer l'adresse du site web : ")
    print()

    ligne_nom_utilisateur = "Nom d'utilisateur : " + nom_utilisateur + "\n"
    ligne_mdp = "Mot de passe : " + mdp + "\n"
    ligne_site_web = "Site web : " + site_web + "\n\n"

    donnees_chiffre = chiffrer_donnees(ligne_nom_utilisateur + ligne_mdp + ligne_site_web)
    with open("./coffre.txt", "wb") as coffre_writer :
        coffre_writer.write(donnees_chiffre)

def lire_mdp():
    contenu = ""
    with open("coffre.txt", "rb") as mdp_reader : 
        donnees_chiffre = mdp_reader. read()
    print()
    print(dechiffrer_donnees(donnees_chiffre).decode())


def generer_nouveau_mdp(taille_mdp):
    caractere_aleatoire = string.ascii_letters + string.digits + string.punctuation
    nouveau_mdp = ""
    for i in range(taille_mdp):
        nouveau_mdp += random.choice(caractere_aleatoire)
    print()
    print("Voici votre mot de passe : " + nouveau_mdp)


# Partie principale du programme
subprocess.call("clear", shell=True)

print("-" * 60)
print("Bienvenue dans le gestionnaire de mot de passe.")
print("-" * 60)

if os.path.exists("./coffre.txt") and os.path.exists("./master.key"):
    print("Selectionnez l'une des options suivantes : ")
    print("1 - Sauvegarder un nouveau mot de passe")
    print("2 - Générer un nouveau mot de passe aléatoire")
    print("3 - Obtenir la liste de vos mot de passe")

    choix = input("Que souhaitez-vous faire ? (1/2/3) : ")

    if choix == "1" :
        ajout_nouveau_mdp()
    elif choix == "2":
        taille_mdp = input("Quelle est la longueur souhaitée pour le mot de passe ? ")
        if not (string.ascii_letters in taille_mdp) : 
            generer_nouveau_mdp(int(taille_mdp))
        else :
            print("Merci de rentrer un nombre.")
            sys.exit()
    elif choix == "3" :
        lire_mdp()
    else : 
        print("Veuillez choisir une option vlaide (1/2/3)")
        sys.exit()
else:
    print("Génération d'un mot de passe maître et d'un coffre de mot de passe...")
    generer_mdp_maitre()
    creer_coffre()
    print("Génération terminée, veuillez relancez le programme.")

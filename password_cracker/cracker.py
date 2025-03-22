#!/usr/bin/env python3
# coding:utf8
import string
import sys
import hashlib
import urllib.request
import urllib.response
import urllib.error
from utils import *

class Cracker:

    @staticmethod
    def crack_dict(md5, file, order, done_queue):
        """
        Casse un hash MD5 (md5) via une liste de mots (file)
        :param done_queue:
        :param order:
        :param md5: Hash MD5 à casser
        :param file: Fichier de mots-clefs à utiliser
        :return:
        """
        try:
            ofile = open(file, "r")
            trouve = False
            if Order.ASCEND == order :
                contenu = reversed(list(ofile.readlines()))
            else :
                contenu = ofile.readlines()

            for mot in contenu :
                mot = mot.strip("\n")
                hash_md5 = hashlib.md5(mot.encode("utf8")).hexdigest()
                if hash_md5 == md5 :
                    print(Couleur.VERT + "[+] MOT DE PASSE TROUVÉ : " + str(mot) + " (" + hash_md5 + ")" + Couleur.FIN)
                    trouve = True
                    done_queue.put("TROUVE")
                    break
            if not trouve :
                print(Couleur.ROUGE + "[-] MOT DE PASSE NON TROUVÉ" + Couleur.FIN)
                done_queue.put("NON TROUVE")
            ofile.close()
        except FileNotFoundError:
            print(Couleur.ROUGE + "[-] ERREUR : NOM DE FICHIER OU DOSSIER INTROUVABLE" + Couleur.FIN)
            sys.exit(1)
        except Exception as err:
            print(Couleur.ROUGE +"[-] ERREUR : " + str(err) + Couleur.Fin)
            sys.exit(2)

    @staticmethod
    def crack_incr(md5, length, _currpass=[]):
        """
        Casse un mdp MD5 via une méthode incrémentale pour un mdp de longueur length
        :param md5: Hash md5 à casser
        :param length: La longueur du mdp à trouver
        :param currpass: liste temporaire automatiquement utilisée via récursion contenant l'essai de mdp actuel
        :return:
        """

        lettres = string.printable  # tous les caractères
        if length >= 1:
            if len(_currpass) == 0:
                currpass = ["a" for _ in range(length)]
                Cracker.crack_incr(md5, length, currpass)
            else:
                for c in lettres:
                    _currpass[length - 1] = c
                    currhash = hashlib.md5("".join(_currpass).encode("utf8")).hexdigest()
                    print("[*] TEST DE : " + "".join(_currpass))  # concatenation de la liste en s tring pour print
                    if currhash == md5:
                        print(Couleur.VERT + "[+] MDP TROUVÉ : " + "".join(_currpass) + Couleur.FIN)
                    else:
                        Cracker.crack_incr(md5, length - 1, _currpass)

    @staticmethod
    def crack_en_ligne(md5) :
        """
        Cherche un Hash MD5 via google.fr
        :param md5: Hash MD5 à utiliser pour la recherche en ligne
        :return:
        """

        try :
            agent_utilisateur = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
                                                                                    # se faire passer pour un navigateur
            headers = {"User-Agent" : agent_utilisateur}
            url = "https://www.google.fr/search?hl=fr&q=" + md5
            requete = urllib.request.Request(url, None, headers)
            reponse = urllib.request.urlopen(requete)
        except urllib.error.HTTPError as e :
            print(Couleur.ROUGE + "[-] ERREUR HTTP : " + e.code + Couleur.FIN)
        except urllib.error.URLError as e :
            print(Couleur.ROUGE + "[-] ERREUR URL : " + e.reason + Couleur.FIN)
        """
        if "Aucun document" in reponse.read().decode("utf8"):
            print(Couleur.ROUGE + "[-] HASH NON TROUVÉ VIA GOOGLE" + Couleur.FIN)
        else :
            print(Couleur.VERT + "[+] HASH TROUVÉ VIA GOOGLE : " + url + Couleur.FIN)
        """
        print("[*] Resultat GOOGLE : " + url)


    @staticmethod
    def crack_smart(md5, pattern, _index=0):
        """

        :param md5:
        :param pattern:
        :param _index:
        :return:
        """
        MAJ = string.ascii_uppercase # ^
        CHIFFRES = string.digits # $
        MIN = string.ascii_lowercase # _

        if _index < len(pattern):
            if pattern[_index] in MAJ + CHIFFRES + MIN :
               Cracker.crack_smart(md5, pattern, _index + 1)
            if "^" in pattern[_index]:
                for c in MAJ:
                    p = pattern.replace("^", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + p + Couleur.FIN)
                        sys.exit(0)
                    print("MAJ : " + p)
                    Cracker.crack_smart(md5, p, _index + 1)

            if "_" in pattern[_index]:
                for c in MIN:
                    p = pattern.replace("_", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + p + Couleur.FIN)
                        sys.exit(0)
                    print("MIN : " + p)
                    Cracker.crack_smart(md5, p, _index + 1)

            if "$" in pattern[_index]:
                for c in CHIFFRES:
                    p = pattern.replace("$", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + p + Couleur.FIN)
                        sys.exit(0)
                    print("CHIFFRE : " + p)
                    Cracker.crack_smart(md5, p, _index + 1)

        else:
            return



    @staticmethod
    def work(work_queue, done_queue, md5, file, order):
        """

        :param work_queue:
        :param done_queue:
        :param md5:
        :param file:
        :param order:
        :return:
        """
        o = work_queue.get()
        o.crack_dict(md5, file, order, done_queue)


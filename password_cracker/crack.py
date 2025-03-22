#!/usr/bin/env python3
# coding:utf8
import time
import argparse
import atexit
from cracker import *
import multiprocessing

def affiche_duree():
    """
    Affiche la durée d'execution du programme
    :return:
    """
    print("Durée : " + str(time.time() - debut) + " secondes")

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Casseur de mot de passe en Python")
    parser.add_argument("-f", "--file", dest="file", help="Chemin du fichier dictionnaire", required=False)
    parser.add_argument("-g", "--gen", dest="gen", help="Genere un hash MD5 du mot de passe donnée",
                        required=False)
    parser.add_argument("-md5", dest="md5", help="Mdp MD5 à casser", required=False)
    parser.add_argument("-l", dest="plength", help="longueur du mdp", required=False, type=int)
    parser.add_argument("-o", dest="online", help="Cherche le hash en ligne (google) ", required=False,
                        action = "store_true")
    parser.add_argument("-p", dest="pattern", help="Utilise le motif de mdp (^=MAJ, $=CHIFFRES, _=MIN)")

    args = parser.parse_args()

    work_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()
    cracker = Cracker()

    debut = time.time()
    atexit.register(affiche_duree)

    if args.gen:
        print("[*] HASH MD5 DE " + args.gen + " : " + hashlib.md5(args.gen.encode("utf8")).hexdigest())

    if args.md5:
        print("[*] CRACKING DU HASH : " + args.md5)
        if args.file :
            print("[*] UTILISANT LE FICHIER DE MOT-CLEFS : " + args.file)
            p1 = multiprocessing.Process(target=Cracker.work, args=(work_queue, done_queue, args.md5, args.file, False))
                                                                                    #Boolean False lecture descendante
            work_queue.put(cracker)
            p1.start()

            p2 = multiprocessing.Process(target=Cracker.work, args=(work_queue, done_queue, args.md5, args.file, True))
                                                                                    # Boolean True lecture ascendante
            work_queue.put(cracker)
            p2.start()

            while True:
                data = done_queue.get()
                if data == "TROUVE" or data == "NON TROUVE":
                    p1.kill()
                    p2.kill()
                    break

        elif args.plength :
            print("[*] UTILISANT LE MODE INCRÉMENTAL " + str(args.plength) + " LETTRES(S)" )
            Cracker.crack_incr(args.md5, args.plength)
        elif args.online :
            print("[*] UTILISANT LE MODE EN LIGNE ")
            Cracker.crack_en_ligne(args.md5)
        elif args.pattern:
            print("[*] UTILISANT LE MODELE DE MOT DE PASSE : " + args.pattern)
            Cracker.crack_smart(args.md5, args.pattern)
        else:
            print(Couleur.ROUGE + "[-] VEUILLEZ CHOISIR L'ARGUMENT -f OU -l AVEC -md5." + Couleur.FIN)
    else:
        print(Couleur.ROUGE + "[-] HASH MD5 NON FOURNI." + Couleur.FIN)



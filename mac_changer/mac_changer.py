#!/usr/bin/env python3
import re
import optparse
import subprocess

def search_mac_address(string):
    return re.search(r'([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})', str(string)).group(0)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface pour changer son adresse MAC")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="Nouvelle adresse MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[–] Veuillez spécifiez l'interface (--help).")
    if not options.new_mac_address:
        parser.error("[–] Veuillez spécifiez une nouvelle adresse MAC(--help)")
    return options


def set_new_mac_address(interface, new_mac_address):
    print("[+] Changement d'adresse MAC de " + interface + " pour " + new_mac_address)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def get_mac_address_from_interface(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = search_mac_address(ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result
    else:
        print("[-] Adresse MAC impossible à lire")

options = get_arguments()
current_mac_address = get_mac_address_from_interface(options.interface)
print("L'adresse MAC actuelle de l'interface " + options.interface + " est : " + current_mac_address)

set_new_mac_address(options.interface, options.new_mac_address)

new_mac_address = get_mac_address_from_interface(options.interface)
if new_mac_address == options.new_mac_address:
    print("[+] L'adresse MAC a été changé pour " + options.new_mac_address)
else:
    print("[-] L'adresse MAC n'a pas été changé")


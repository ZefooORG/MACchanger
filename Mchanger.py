import subprocess
import optparse
import re


def get_agruments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Mac adress uchun")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="Yangi mac")

    (options, argument) = parser.parse_args()

    if not options.interface:
        print("Interface nomini yoz")
    elif not options.new_mac:
        print("New mac kirit")
    return options


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]  Cloud not read Mac address.")


options = get_agruments()
current_mac = get_current_mac(options.interface)
print("[-] Current mac = " + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[-] Mac address was successfully change to " + current_mac)
else:
    print("[-] Mac address did not get changed")
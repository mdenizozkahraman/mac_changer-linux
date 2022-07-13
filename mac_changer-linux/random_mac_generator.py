









# created by Mehmet Deniz Ozkahraman

import subprocess
import optparse
import re
import random

hex_charlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
hex_charlist2 = [0, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
mac_list = []


def random_char_generator():
    for digit in range(12):
        a = random.choice(hex_charlist)
        mac_list.append(a)
    return mac_list


def random_mac_generator():
    def random_char_generator():
        for digit in range(12):
            a = random.choice(hex_charlist)
            mac_list.append(a)
        return mac_list

    random_char_generator()

    if (mac_list[1] == 1):
        mac_list[1] = random.choice(hex_charlist2)

    mac_address = str(mac_list[0]) + str(mac_list[1]) + ":" + str(mac_list[2]) + str(mac_list[3]) + ":" + str(
        mac_list[4]) + str(mac_list[5]) + ":" + str(mac_list[6]) + str(mac_list[7]) + ":" + str(mac_list[8]) + str(
        mac_list[9]) + ":" + str(mac_list[10]) + str(mac_list[11])

    print(mac_address)


random_mac_generator()

random_mac = random_mac_generator()


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

    return parse_object.parse_args()


def get_user_input_random():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-r", "--random", dest="random-mac_address", help="new random mac address")

    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(['ifconfig', user_interface, 'down'])
    subprocess.call(['ifconfig', user_interface, 'hw', 'ether', user_mac_address])
    subprocess.call(['ifconfig', user_interface, 'up'])


def change_random_mac_address(user_interface, random_mac):
    subprocess.call(['ifconfig', user_interface, 'down'])
    subprocess.call(['ifconfig', user_interface, 'hw', 'ether', random_mac])
    subprocess.call(['ifconfig', user_interface, 'up'])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("MAC CHANGER STARTED!")

choice = int(input("""

1-) Random MAC Address
2-) Manual MAC Address
Choice: 
"""))

if choice == 2:
    (user_input, arguments) = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address)

elif choice == 1:
    (user_input, arguments) = get_user_input_random()
    change_random_mac_address(user_input.interface, random_mac)
else:
    print("Please enter 1 or 2!!!")

finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Success!")
    print("Your new " + user_input.interface + "'s MAC Address: " + finalized_mac)
else:
    print("Error!!")
    print("MAC Address is NOT changed! : " + finalized_mac)









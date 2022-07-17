# created by Mehmet Deniz Ozkahraman

import subprocess
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

    mac_address = str(0) + str(0) + ":" + str(mac_list[2]) + str(mac_list[3]) + ":" + str(
        mac_list[4]) + str(mac_list[5]) + ":" + str(mac_list[6]) + str(mac_list[7]) + ":" + str(mac_list[8]) + str(
        mac_list[9]) + ":" + str(mac_list[10]) + str(mac_list[11])

    return mac_address


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(['ifconfig', user_interface, 'down'])
    subprocess.call(['ifconfig', user_interface, 'hw', 'ether', user_mac_address])
    subprocess.call(['ifconfig', user_interface, 'up'])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


def first_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    first_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if first_mac:
        return first_mac.group(0)
    else:
        return None


print("""
by mdo //-
                                        _                                              _  _                     
   _ __ ___    __ _   ___          ___ | |__    __ _  _ __    __ _   ___  _ __        | |(_) _ __   _   _ __  __
  | '_ ` _ \  / _` | / __|        / __|| '_ \  / _` || '_ \  / _` | / _ \| '__| _____ | || || '_ \ | | | |\ \/ /
  | | | | | || (_| || (__        | (__ | | | || (_| || | | || (_| ||  __/| |   |_____|| || || | | || |_| | >  < 
  |_| |_| |_| \__,_| \___| _____  \___||_| |_| \__,_||_| |_| \__, | \___||_|          |_||_||_| |_| \__,_|/_/\ \ 
                          |_____|                            |___/                                              
""")




while True:
    choice = str(input("""

1-)RANDOM MAC ADDRESS
2-)MANUEL MAC ADDRESS
3-)REAL MAC ADDRESS

Q-)EXIT THE MAC CHANGER

Choice: """))
    f = open("mac-addresses.txt", "r+")

    if choice == "Q":
        print("PROGRAM IS TERMINATING...")
        break
    elif ((choice != "1") and (choice != "2") and (choice != "3") and (choice != "Q")):
        print("")
        print("Please enter 1, 2, 3 or Q!")
        continue


    interface = str(input("Interface (eth0, wlan0 etc.): "))



    real_mac = str(first_mac(interface))

    f.write(real_mac)

    first_mac_address = str(f.read(17))

    if choice == "1":

        fixed_mac = str(random_mac_generator())

        change_mac_address(interface, fixed_mac)

        control_new_mac(interface)

        finalized_mac = control_new_mac(interface)

        if finalized_mac == random_mac_generator():
            print("Success!")
            print("Your new " + interface + "'s MAC Address: " + finalized_mac)
        else:
            print("Error!!")
            print("MAC Address is NOT changed! : " + finalized_mac)
        break

    elif choice == "2":

        print(
            "MAC Address must be include hexadecimal numbers (" + str(hex_charlist) + ") but 2nd digit must NOT be '1'")
        mac_address = str(input("MAC ADDRESS (XX:XX:XX:XX:XX:XX):"))

        change_mac_address(interface, mac_address)
        control_new_mac(interface)

        finalized_mac = control_new_mac(interface)

        if finalized_mac == mac_address:
            print("Success!")
            print("Your new " + interface + "'s MAC Address: " + finalized_mac)
        else:
            print("Error!!")
            print("MAC Address is NOT changed! : " + finalized_mac)
        break

    elif choice == "3":

        change_mac_address(interface, first_mac_address)

        control_new_mac(interface)

        finalized_mac = control_new_mac(interface)

        if finalized_mac == first_mac_address:
            print("Success!")
            print("Your new " + interface + "'s MAC Address: " + finalized_mac)
        else:
            print("Error!!")
            print("MAC Address is NOT changed! : " + finalized_mac)
        break



f.close()


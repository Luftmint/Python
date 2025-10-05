# Övning 9, IP-check
# If adress starts with 192.168, print "local network"

ip = input("Input your IP-address: ").strip()

if len(ip) > 0:
    oct1 = ip.split(".")[0]
    if oct1 == '192':
        print("Local network.")
    else:
        print("Oops.")
        
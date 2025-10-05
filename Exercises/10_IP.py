# Övning 10, IP-adress classification(?)
# 10.0.0 = A private
# 172.16-31 = B private
# 192.168 = C private
# If neither, print "public IP"

address = input("Input an IP-address: ").strip()

#if len(address) > 0:
 #   first_digits = address.split(".")[0]
 #   if first_digits == '10' or first_digits == '192' or first_digits == '172':
 #       print("Private IP address.")
 #   else:
 #       print("Public IP address.")
if len(address) > 0:
    first_digits = address.split(".")[0]
    if first_digits in {'10', '192', '172'}:
        print("Private IP address.")
        
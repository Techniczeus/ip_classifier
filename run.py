# Build a code that classifies IPs

from IPThreatment import IP # import IP class

# Opening files

check = 1

while check == 1:
    try:
        r_file = open(input("File name goes here(No Letters): "), "r")
        check = 0
    except FileNotFoundError:
        print("File not found, try again!")

w_file = open("Results.txt", "w")

ips = IP()  # Recieve IP class

for li in r_file.readlines():

    # removing "\n" from ips

    li = li.strip()
    raw = li
    raw = raw.strip()
    
    li = ips.converter(li)

    if ips.validate(li) == 1:
            ipclass = ips.csf(li)

    else:
        ipclass = "Unknown"

    try:
        if ipclass == "Unknown":
            print("Invalid IP")
            w_file.write(f"{raw} Classified as: {ipclass}\n")
        else:
            print("IP Verified")
            w_file.write(f"{raw} Classified as: {ipclass}\n")
    except ValueError:
        print("Not valid")
    


r_file.close()
w_file.close()
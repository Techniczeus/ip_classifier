# Build a code that classifies IPs

from IPThreatment import IP # import IP class

# Opening files

r_file = open(input("File name goes here: "), "r")

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
        ipclass = "unknown"

    print("IP Verified")
    w_file.write(f"{raw} Classified as: {ipclass}\n")


r_file.close()
w_file.close()
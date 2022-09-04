from IPThreatment import IP

r_file = open(input("File name goes here: "), "r")

w_file = open("Results.txt", "w")

def nolines():
    f = len(r_file.readlines())
    return f

for li in range(nolines()):

    ips = IP(li)

    raw = li

    li = li.strip()
    raw = raw.strip()

    li = ips.converter(li)

    if ips.validate(li) == 1:
            ipclass = ips.csf(li)

    else:
        ipclass = "unknown"

    print("IP Verified")
    w_file.write(f"IP was classified as {ipclass}")


r_file.close()
w_file.close()
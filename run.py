# make an application to classify IPS

from FileThreater import fthreater  # Importing class for file threatment
from IPThreatment import IP # Importing class for IP threatment

try:                                                
    ft1 = fthreater(input("File name goes here: "))
except Exception:
    print("Error, try again with a valid file! ")

def run(): # Function that runs the program
    ft1.reader()
    w_file = open("Results.txt", "w")   
    ipcount = 0

    n = ft1.nlines()

    for li in ft1.reader():
        rawip = li

run()
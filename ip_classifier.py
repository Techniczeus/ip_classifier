# make an application to classify IPS

reader = input("File name: ") 
r_file = open(reader, "r") # defines the input file to read
w_file = open("Results.txt", "w")

x = r_file.read()

for y in x:
    y = x.split(".")
#    if "\n" in y:
#        y[y] = 

#for i in y:
#    if iter(y[i]) > 254 or iter(y[i]) < 0:
#        print("INVALID IP!")
        
print(y)
w_file.writelines(y)


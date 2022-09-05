class IP:
    def __init__(self)->None:
        pass
    def csf(self,ip): # this function classifies received ips
        if(ip[0]>=1 and ip[0]<=126):
            return 'A'

        elif(ip[0]==127): 
            return "LocalHost"
        
        elif(ip[0]>=128 and ip[0]<=191):
            return 'B'
        
        elif(ip[0]>=192 and ip[0]<=223):
            return 'C'
        
        elif(ip[0]>=224 and ip[0]<=239):
            return 'D'
        
        else:
            return 'E'


    def converter(self,ip): # converting to int
        ip = ip.split(".")
        
        for num in range(0,len(ip)):
            ip[num] = int(ip[num])

        return ip


    def validate(self,ip):  # checks if current ip is valid
	
        for num in range(0, len(ip)):
            
            if (ip[num]<0 or ip[num]>255):
                return 0
                break
        
        return 1

class fthreater:  # Creating a class that will make the file threatment
    def __init__(self,fname):
        self.fname = fname

    def reader(self): # Get the file
        global r_file
        r_file = open(self.fname, "r")

    def nlines(self): # Counting amount of lines length
        self.reader()
        nl = len(r_file.readlines())
        return nl

    def read(self):
        self.reader()
        f = r_file.readlines()
        return f
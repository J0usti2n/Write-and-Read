""" *** NOT WORKING *** """
#_classes____________________________________________________
#-Write-&-Read-----------------------------------------------
class Write_and_Read():
    def __init__(self):
        self.file_write = open("test.txt", "w")             # open file in write mode
        self.file_read  = open("test.txt", "r")             # open file in read mode

        self.write      = self.file_write.write("Test")     # write "Test"
        self.new_line   = self.file_write.write("\n")       # new line

        self.read = print(self.file_read.read())            # print the written text

    #-write-method-------------------------------------------
    def write(self):
        self.file_write
        self.write
        self.new_line
        self.file_write.close()                             # close write mode file

    #-read-method--------------------------------------------
    def read(self):
        self.file_read
        self.read
        self.file_read.close()                              # close read mode file


x = Write_and_Read()
x.write
x.read
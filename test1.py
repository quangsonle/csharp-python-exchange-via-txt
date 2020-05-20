bien=0
file1 = open("test.txt","r") 
file2 = open("test2.txt","r+")
data="678991" 
#file2.write(data)

try:
    while True:
       
       d=file1.readline()
       if (d):
        print(d)
        file1.close()
        file1 = open("test.txt","r")
       
       #file2.truncate(0)
       file2.write(data)
       file2 .close()
       file2 = open("test2.txt","r+") 
except KeyboardInterrupt:
    pass
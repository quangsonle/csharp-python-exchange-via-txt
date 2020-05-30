bien=0
file1 = open("test.txt","r") 
file2 = open("test2.txt","r+")
data="678991" 
#file2.write(data)
e=""
try:
    while True:
       
       d=file1.readline()
       
       if (d):
        print('da gan')
        
        if (d=='r'):
         print ('rrrrrrrr')
         e=d
        if (d=='e'):
         print ('eeeeeeeee')
         e=d
        #file1.truncate(0)
        file1.close()
        file1 = open("test.txt","r+") 
        file1.truncate(0)
        file1.close()
        file1 = open("test.txt","r")
       else:
        print("ko co j")
       print(e)
       
       #file2.truncate(0)
       file2.write(data)
       file2 .close()
       file2 = open("test2.txt","r+") 
except KeyboardInterrupt:
    pass
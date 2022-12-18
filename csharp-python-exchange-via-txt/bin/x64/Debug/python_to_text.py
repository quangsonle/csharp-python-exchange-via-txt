bien=0
import pathlib
path_to_txt=str(pathlib.Path().absolute())+"\\"
print('path is',path_to_txt)
#path_to_txt="C:\\csharp-python-exchange-via-txt-master\\"
file1 = open(path_to_txt+"test.txt","r") 
file2 = open(path_to_txt+"test2.txt","r+")
data=0
#file2.write(data)
e=""
try:
    while True:
       
       d=file1.readline()
       
       if (d):
        #print('read ok')
        
        if (d=='r'):
         #print ('rrrrrrrr')
         e=d
         #data=data+1
        if (d=='e'):
         print ('eeeeeeeee')
         e=d
         #data=data+6
        #file1.truncate(0)
        file1.close()
        file1 = open(path_to_txt+"test.txt","r+") 
        file1.truncate(0)
        file1.close()
        file1 = open(path_to_txt+"test.txt","r")
       #else:
        #print("nothing")
       if (d):
        print("data from c# is",d,'data to send back is',data+1)
        data=data+1
       
       #file2.truncate(0)
       file2.write(str(data))
       file2 .close()
       file2 = open(path_to_txt+"test2.txt","r+") 
except KeyboardInterrupt:
    pass

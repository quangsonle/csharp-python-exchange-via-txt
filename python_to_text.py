bien=0
file1 = open("C:\\Users\\admin\\Desktop\\project\\github_working_place\\csharp-python-exchange-via-txt-master\\test.txt","r") 
file2 = open("C:\\Users\\admin\\Desktop\\project\\github_working_place\\csharp-python-exchange-via-txt-master\\test2.txt","r+")
data=678991
#file2.write(data)
e=""
try:
    while True:
       
       d=file1.readline()
       
       if (d):
        print('read ok')
        
        if (d=='r'):
         print ('rrrrrrrr')
         e=d
         data=data+1
        if (d=='e'):
         print ('eeeeeeeee')
         e=d
         data=data+6
        #file1.truncate(0)
        file1.close()
        file1 = open("C:\\Users\\admin\\Desktop\\project\\github_working_place\\csharp-python-exchange-via-txt-master\\test.txt","r+") 
        file1.truncate(0)
        file1.close()
        file1 = open("C:\\Users\\admin\\Desktop\\project\\github_working_place\\csharp-python-exchange-via-txt-master\\test.txt","r")
       #else:
        #print("nothing")
       if (d):
        print(d)
       
       #file2.truncate(0)
       file2.write(str(data))
       file2 .close()
       file2 = open("C:\\Users\\admin\\Desktop\\project\\github_working_place\\csharp-python-exchange-via-txt-master\\test2.txt","r+") 
except KeyboardInterrupt:
    pass

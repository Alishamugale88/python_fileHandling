
#open file in append mode it will write at end of file
# open file -1 read("r")  2. write("w")  3.append ("a")  4. create file ("x")
# function of file objects ---- close() read() readline() read(10)  write()

import os

#user define module
import module

f=open("test.txt","a")

print(f.read(5))

f1=open("imp.txt","w")
name=input("Enter your name : ")
print(name)
#write entered names to file imp.txt 
f1.write(name)


#to delete file must import OS module and run as os.remove()

os.remove("./test.txt")
module.removefile()
#closing file

f1.close()


os.remove("./test4.txt")
module.removefile()
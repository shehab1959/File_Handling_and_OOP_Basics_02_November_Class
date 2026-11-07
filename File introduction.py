###File introduction###
#open("filepath","mode") #mode(r,w,a)- read,write,append


## Create file
file = open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "w")
file.write("Hello World\n")
file.write("Ostad\n")
file.write("Ostad ki obostha\n")
file.close()

#This line will print a message in your VS Code terminal so you know it worked!
print("Successfully created 'test.txt' in your computer folder!")



## Read file
file = open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "r")
content = file.read()
file.close()
print(content)
#Hello World
#Ostad
#Ostad ki obostha



##File Append

file = open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "a")
file.write("New contend add to the previous text file\n")
file.write("Added successfully")
file.close()

file = open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "r")
content1 = file.read()
file.close()
print(content1)
#Hello World
#Ostad
#Ostad ki obostha
#New contend add to the previous text file
#Added successfully




##File handling with context manager (alada kore file close korte hoyna)
with open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "r") as file:
    content2 = file.read()
    print(content2)
#Hello World
#Ostad
#Ostad ki obostha
#New contend add to the previous text file
#Added successfully
###File introduction###
#open("filepath","mode") #mode(r,w,a)- read,write,append


## Create file
file = open(r"D:\Ostad\Code\Practice(2nd november class)\test.txt", "w")
file.write("Hello World\n")
file.write("Ostad\n")
file.close()

#This line will print a message in your VS Code terminal so you know it worked!
print("Successfully created 'test.txt' in your computer folder!")

###


#step 1: write to file
file=open("myfile.txt","w")
file.write("Hello Students")
file.close()

#step 2: Append to file
file=open("myfile.txt","a")
file.write("\n Welcome to Python")
file.close()

#step 3: Read from file
file=open("myfile.txt","r")
data=file.read()
print(data)
file.close()

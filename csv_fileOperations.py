#write
import csv

# step 1: Write to csv file
f=open("Students.csv","w",newline='')
write=csv.writer(f)

write.writerow(["Name","Marks"])
write.writerow(["Amit","85"])
write.writerow(["Riya","90"])

f.close()

# read
# step 2: Read from csv file
f=open("Students.csv","r")
reader=csv.reader(f)

for row in reader:
    print(row)

f.close()
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
#Reading file line by line
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split( )
    #print the second word in the line
    print(words[1])
    count= count + 1
#printing all the email addresses and the count of them. 
print("There were", count, "lines in the file with From as the first word")

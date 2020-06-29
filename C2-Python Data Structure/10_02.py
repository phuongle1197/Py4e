name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    #The program looks for 'From ' lines
    if line.startswith('From '):
        words = line.split()
        #splitting the string a second time using a colon.
        hours = words[5].split(":")
        #print(hours[0])
        #use get() and provide a default value of zero when the key is not yet in the dictionary- and then just add one
        counts[hours[0]] =counts.get(hours[0], 0 ) + 1

#print(counts)
#sorted by hour
for k,v in sorted(counts.items()):
    print(k,v)

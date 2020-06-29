fname = input("Enter file name: ")
fh = open(fname)

count= 0
total = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num =line[20:]
    numb = num.strip()
    #convert the extracted value to a floating point number
    number = float(numb)
    count = count + 1
    total = total + number
    #print(line)
avg = total/count

print("Average spam confidence:",avg)

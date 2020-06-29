fname = input("Enter file name: ")
fh = open(fname)

lst=list()

for line in fh:
    # For each line, splitting the line into words
    line = line.rstrip()
    ls = line.split( )
    # For each word, check if already in the list and if not append it to the list.
    for words in ls:
        if words not in lst:
            lst.append(words)

lst.sort()
print(lst)

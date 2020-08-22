#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

#Importing the regex library
import re

#Enter the source file
name = input("Enter file name:")
if len(name) < 1 : name = "regex_sum_42.txt"
#Open the source file
handle = open(name)

#Initialising the sum of the numbers
sum = 0

#Read file line-by-line
for line in handle:
    # Finding all te number as strings into listNums
    listNums = re.findall('([0-9]+)',line.rstrip())
    # if no number in the line, then go to the next loop
    if len(listNums) < 1:
        continue
    else:
        for snum in listNums:
            sum = sum + int(snum)


print(sum)

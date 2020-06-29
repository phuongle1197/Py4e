text = "X-DSPAM-Confidence:    0.8475"
num1 =text.find("0")
#print(num)
num2 =text.find("5")
snum =text[num1:num2+1]
#convert the extracted value to a floating point number
fnum=float(snum)
print(fnum)

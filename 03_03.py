score = input("Enter Score: ")
try:
	scr = float(score)
except:
	scr = -1

if scr >= 0.9:
	print("A")
elif scr <0.9 and scr>= 0.8:
    print("B")
elif scr <0.8 and scr>= 0.7:
    print("C")
elif scr <0.7 and scr>= 0.6:
    print("D")
elif scr < 0.6:
    print("F")
elif scr >=1 or scr <= 0:
    print("Try again")

	

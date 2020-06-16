def computepay(h,r):
    if h <=40:
    	pay=h*r
    else:
    	pay=40*r + (h-40)*r*1.5
    return pay

hrs = input("Enter Hours:")
hours= float(hrs)
rte =input("Enter Rates:")
rates =float(rte)

p = computepay(hours,rates)
print("Pay",p)

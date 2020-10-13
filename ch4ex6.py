def computepay(h,r):
 if h<=40:
  pay = h*r
 elif h>40:
  hr=h-40
  pay = 40*r+hr*r*1.5
 return pay

hrs = input("Enter Hours:")
h=float(hrs) 
rate= input ("Enter Rate:") 
r=float(rate) 
p = computepay(h,r)
print("Pay",p)

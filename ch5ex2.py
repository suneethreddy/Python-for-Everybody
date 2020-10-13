largest = None
smallest = None
while True:
 num = input("Enter a number: ")
 if num is "done":
  break
 try:
  inti =int(num) 
 except:
  print("Invalid input") 
  continue
 if largest is None:
  largest=inti
 if smallest is None:
  smallest=inti
 if inti>largest:
  largest=inti
 if inti<smallest:
  smallest=inti


print("Maximum is", largest)
print("Minimum is", smallest) 

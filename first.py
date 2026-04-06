bill=int(input("enter your electricity bill:"))
connection=(input("enter connection type(domestic/commercial):"))
charge=0
if bill<=100:
  charge=(bill*5)
elif bill<=200:
  charge=(100*5)+(bill-100)*7
else:
   charge=(100*5)+(100*7)+(bill-200)*10
   if connection=="commercial":
      charge+=200
      if bill>300:
        charge+=100
      elif connection=="domestic":

        if bill>200:
          charge=bill-(0.05*bill)

print('total bill is:',charge)


position=input("enter position:")
column=position[0]
row=int(position[1])
column_num=ord(column)-ord('a')+1
total=column_num+row
if total % 2 ==0:
  print("black")
else:
  print("white")

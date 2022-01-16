# my initial solution 
info = input("Enter log: ").split()
totalamount = 0

while info != []:
  if info[0] == "D":
    totalamount = totalamount + int(info[1])
  elif info[0] == "W":
    totalamount = totalamount - int(info[1])
  else:
    break
  info = input("Enter log: ").split()

print("Amount is " + str(totalamount))


#cleaner solution with no repeated lines
totalamount = 0

while True:
  info = input("Enter log: ").split()
  if not info:
    break
  elif info[0] == "D":
    totalamount = totalamount + int(info[1])
  elif info[0] == "W":
    totalamount = totalamount - int(info[1])
  else:
    pass
print("Amount is " + str(totalamount))

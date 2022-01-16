return_list = []
number = int(input())

if number == 1:
  return_list.append(0)

else:
  return_list = [0,1]
  i = 2
  while i < number:
    new_number = return_list[i-2] + return_list[i-1]
    return_list.append(new_number)
    i = i + 1

print(return_list)

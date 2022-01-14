password = input('Please enter a password: ')

size = len(password)

hasnumber = False
hasupper = False 
haslower = False 

for i in password:
  if i.isdigit():
    hasnumber = True 
  elif i.isupper:
    hasupper = True 
  elif i.islower:
    haslower = True 

# case of horrible password
if password == 'password' or password == 'iloveyou' or password == '123456':
  print('Horrible Password')

#strong password 
elif size >= 12 and hasnumber and hasupper and haslower:
  print('Strong Password')

# moderate password
elif size >= 8 and hasnumber:
  print('Moderate Password')

# poor password 
else: 
  print('Poor Password')

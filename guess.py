print("Pick a number between 1 and 100 (inclusive)")
big = 100
small = 0 
guess = int((big+small)/2)

while True:
  print('My guess is: '+ str(guess))
  letter = input('Is my guess too low (L), too high (H), or correct (C)?')
  if letter == 'L':
    small = guess
  elif letter == 'H':
    big = guess 
  elif letter == 'C':
    print('Got it!')
    break
  guess = int((big+small)/2)

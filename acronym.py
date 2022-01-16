acronym = []
capstr = input("Enter string: ").upper()
wordlist = capstr.split()

for word in wordlist:
  for char in word:
    if char.isalpha():
      acronym.append(char)
    break
    
print("Acronym is " + "".join(acronym))

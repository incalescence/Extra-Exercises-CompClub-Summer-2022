#my initial solution 
acronym = []
capstr = input("Enter string: ").upper()
wordlist = capstr.split()

for word in wordlist:
  for char in word:
    if char.isalpha():
      acronym.append(char)
    break
    
print("Acronym is " + "".join(acronym))

#shorter solution
acronym = []
capstr = input("Enter string: ").upper()
wordlist = capstr.split()

for word in wordlist:
    if word[0].isalpha():
      acronym.append(word[0]) 

print("Acronym is " + "".join(acronym))

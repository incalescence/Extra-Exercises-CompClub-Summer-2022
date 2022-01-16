def split(word):
    return [char for char in word]

word = input("Enter a string: ")
characters = split(word)
palindrome = True 
i = 0 
j = 1
totalchar = len(characters)
while i < totalchar/2:
  if characters[i] != characters[totalchar-j]:
    palindrome = False
    break
  i += 1
  j += 1

if palindrome == False :  
  print("The string is not a palindrome.")

else:
  print("The string is a palindrome.")
 
 # could also use a reverse string function using [::-1] then check if the input and reversed strings are the same 

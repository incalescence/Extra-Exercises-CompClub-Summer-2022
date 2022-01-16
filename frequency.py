words = input()
list_of_words = words.split()
returndict = {}

for word in list_of_words:
  if word in returndict:
    returndict[word] += 1
  else:
    returndict[word] = 1

print("Frequency chart")
for w in sorted(returndict.keys()):
    print(str(w) + ": " + str(returndict[w]))

factors = []

number = int(input())

i = 2
while i <= number:
  if number % i == 0:
    factors.append(i)
    number = number/i
  elif number % i != 0:
    i = i + 1

print(factors)

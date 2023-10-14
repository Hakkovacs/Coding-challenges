import sys
largest_number = 0
all_numbers = []

count = int (input ("How many numbers do you want to sort? "))
if count <= 0:
  print ("The number has to be bigger than Zero")
  sys.exit()

for i in range(count):
  number = int (input (f'Enter number {i+1}: \n'))
  all_numbers.append (number)

print (all_numbers)

guess = all_numbers [count-1]

for j in range (count-1):

  for i in range (count - j - 1) :
    if all_numbers [i] > all_numbers [i+1] :
      temp = all_numbers [i]
      all_numbers [i] = all_numbers [i+1]
      all_numbers [i+1] = temp

print (all_numbers)
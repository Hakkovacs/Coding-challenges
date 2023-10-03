count = int (input ("How many numbers do you want to add up? "))
sum = 0
for i in range(count):
  sum += int (input(f"Enter number {i+1}: "))
  print (f"The sum of the numbers is so far {sum}")
print (f"\n The final sum is {sum}")
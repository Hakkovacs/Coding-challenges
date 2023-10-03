text = input('What is your name?\n')
reversedtext = ""
for i in range(len(text)):
  reversedtext = text[i] + reversedtext
print(f"Your name reads backwards {reversedtext}")


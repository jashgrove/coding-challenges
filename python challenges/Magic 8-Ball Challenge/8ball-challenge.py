import random

name = ""
question = "Does my cat love me?"
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very Doubtful"
else:
  answer = "Error"

if name == "":
  print(f"Question: {question}")
else: print(f"{name} asks: {question}")

if question == "":
  print("Sorry you didn't ask a question!")
else:
  print(f"Magic 8-Ball's answer: {answer}")

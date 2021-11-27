import random
randm_numbr=random.randrange(1, 10)
guessed_num = int(input("Guess the number between 1 and 9:"))
if guessed_num >=10 or guessed_num <1:
  print("Guessed number should be between 1 and 9")
elif guessed_num==randm_numbr:
   print("Wow the number is right ")
elif guessed_num<randm_numbr:
   print("The guessed number is low ")
elif guessed_num>randm_numbr:
   print("The guessed number is high ")
else:
  print("Guessed number should be between 1 and 9")
print("The random number is "+str(randm_numbr))
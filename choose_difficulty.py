
# asks user if they would like to play the quiz on easy, medium, or hard
choose_difficulty = input("Would you like to play on easy, medium, or hard\n").lower()

# if easy, the user will be asked easy questions (Haven't made the questions yet)
if choose_difficulty == "easy":
  print ("program continues")
  
# elif medium, the program will print medium difficulty questions
elif choose_difficulty == "medium":
  print ("program continues")
  
# elif hard, the program will print hard difficulty questions
elif choose_difficulty == "hard":
  print ("program continues")
  
elif choose_difficulty == "xxx":
  print ("Thanks for playing")
  exit()

# else, asks user to type easy, medium, hard, or xxx to quit
else:
  print("please type easy, medium, or hard")

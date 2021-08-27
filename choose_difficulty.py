# While True loops the questions and break breaks the loop. I didn't add break for the else because I want the question to loop and ask the user the question again.
while True:
  # asks user if they would like to play the quiz on easy, medium, or hard
  user_difficulty = input("Would you like to play on easy, medium, or hard\n").lower()

  # if easy, the user will be asked easy questions (Haven't made the questions yet)
  if user_difficulty == "easy":
    print ("program continues")
    break
    
  # elif medium, the program will print medium difficulty questions
  elif user_difficulty == "medium":
    print ("program continues")
    break
    
  # elif hard, the program will print hard difficulty questions
  elif user_difficulty == "hard":
    print ("program continues")
    break
    
  # elif xxx,   
  elif user_difficulty == "xxx":
    print ("Thanks for playing")
    exit()

  # else, asks user to type easy, medium, hard, or xxx to quit
  else:
    print("please type easy, medium, or hard")
import random
import time

# Easy mode questions and answers
Question_list_easy = {
   "when would you say kia ora? \n A. when your saying hello to someone\n B. when your wishing someone good health \n C. when your agreeing with someone \n D. all of the above": ["d", "all of the above"],
   "whats the second line of the new zealand national athem?":"o nga iwi matou ra", 
   "What is ocean in Te Reo Maaori? \n A. kātao\n B. Moana\n C. Awa \n D. Wai":["b", "moana"],
   "Whats red in Te Reo Maaori? \n A. whero \n B. Red \n C. whrea \n D. rato" :
   ["a","whero"],
   "what is six in Te Reo Maaori? \n A. Wha  \n B. toro \n C. Rua \n D. ono":
   ["d","ono"]  
   } 
# Medium mode questions and answers
Question_list_medium = {
   "whats the job or an macron??":"to lengthen a vowel",
   "what would you catch with a paa kahwai?  \n A. pekkatua \n B. ika \n C. manu \n D. Matai \n " :["b", "ika"], 
   "If you gave a donation, gift or contribution, you would give a ?":"koha",
   "If you are welcoming someone to a school or marae, you would of give a ?":"powhiri",
   "what colour is the underside of the ponga fround? \n A. Hirwa \n B. Kakariki \n C. Pango \n D. whakiriki \n":["hirwa", "a"]
   } 
# Hard mode questions and answers
Question_list_hard = {
   "what is the translation of hei tiki??":"neck pendant of human form",
   "what would be stored in a paataka? Pikapuka, kai or waka?" :"kai", 
   "what is te reo maaori name for the rugby union?":"hutuporo",
   "if it is ua, what is it?" :"rainy",
   "if you were going for a hikoi you are?" :"going for a walk"
   } 

# difficulty function
def Chosen_difficulty (question):
  valid=False
  while not valid:
    difficulty_response = input (question) .lower()

    if difficulty_response == "easy" or difficulty_response == "e": 
        difficulty_response = "easy"
        return difficulty_response
        
    elif difficulty_response == "medium" or difficulty_response  == "m":
        difficulty_response = "medium"
        return difficulty_response 

    elif difficulty_response == "hard" or difficulty_response  == "h":
      difficulty_response = "hard"
      return difficulty_response      

    elif difficulty_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()     

    else:
      print("Please choose easy, medium or hard") 
      print("Or type xxx to quit") 

quiz_difficulty = Chosen_difficulty ("Would you like to play on easy, medium, or hard\n").lower()

# if easy, the programw will print easy questions
if quiz_difficulty == "easy":
  Question_list = Question_list_easy


# if medium, the programw will print easy questions
elif quiz_difficulty == "medium":
  Question_list = Question_list_medium


# if hard, the programw will print easy questions
elif quiz_difficulty == "hard":
  Question_list = Question_list_hard

# if xxx, program discontinues
elif quiz_difficulty == "xxx":
  print ("Thanks for playing the Te Reo Maaori Quiz")
  print ("We hope to see you again")
  time.sleep(2)
  exit()

# asks user if they would like to play with lives
play_lives = input ("Would you like to play with lives\n")

# if yes, the user will be asked how many lives would they like to have
if play_lives == "yes":
  print ("Thats great")
  print("How many lives would you like to play with")
  user_lives = int(input()) 
  print("You will be playing with {} lives".format(user_lives))
  print("Getting a question wrong will result in you losing a life")
  print()

# else, user will not be playing with lives and lives will equal nothing
else:
  print("You will not be playing with lives")
  user_lives = ()
  print()

print("GOOD LUCK")

# score = 0
score = 0
# the question = one of the questions in the list
question = list (Questions_answers.keys())
#input answer here 
while True:
    if not question:
        break
    # that variable which will have the randomly chose question will mean the same as random.choice(question) which is why the variable is named randomized_question. 
    # random.choice(question) randomly picks one of the questions in the dictionary
    randomize_question = random.choice(question)
    # program prints random question from dictionary. Questions vary depending on what difficulty the user chose
    print(randomize_question)
    while True:
        answer = input('Answer ' )
        # if correct, moves onto next question
        if answer.lower() in Questions_answers[randomize_question]:
            print("Correct Answer")
            print ()
            # if correct, score goes up by 1
            score += 1
            print("your score is now", score)
            print()
            # breaks loop and reasks the question
            break
        else:
            #if wrong
            print("Wrong Answer, try again")
            # if user_lives doesn't = () then minus 1 life
            if user_lives != ():
              user_lives -= 1
              # if user has less than 1 life (0 lives), tell the user they have run out of lives and end program with exit()
              if user_lives < 1:
                print()
                print ("You've run out of lives")
                print("Thanks for playing the Te Reo quiz"\
                " we hope to see you again")
                # ends the program with exit()
                exit()
              else:
                # if user has less than 2 lives, the program will print you have one life
                if user_lives < 2:
                  print("You now have one life left")
                  print()
                else:
                  # tells the user how many lives they have left
                  print("You now have {} lives left".format(user_lives))
                  print()
                  print("Try again")
                  # asks user the question they just got wrong
    question.remove(randomize_question)
  print("You did very well")
  # if user played with lives, the program will tell the user how many lives they had left and their final score
  if user_lives != ():
    print("Your final score was {} and you had {} lives left".format(score, user_lives) )
  # if the user didn't play with lives, the program will only tell them their final score
  else:
    print("Your final score was", score)

  # program asks user if they would like to play the quiz again
  play_again = input("Would you like to play the quiz again? Maybe you'll be able to beat your high score\n")

  #if answer is not yes, break the outer infinite loop
  if play_again != "yes": 
    print("Thanks for playing")
    break 
    time.sleep(2)
    exit()

  else:
    score = 0
    print()
    # ask user if they would like to play on the same difficulty
    same_difficulty = input ("Would like to play on the same difficulty?\n")
    # if no, ask what difficulty they would like to play
    if same_difficulty == "no":


     
      # Asks user if they would like to play on easy, medium, or hard
      quiz_difficulty = Chosen_difficulty ("Would you like to play on easy, medium, or hard\n").lower()

      # if easy, the programw will print easy questions
      if quiz_difficulty == "easy":
        print("That's great. You'll be asked easy questions")
        print()
        Question_list = Question_list_easy


      # if medium, the programw will print easy questions
      elif quiz_difficulty == "medium":
        print("That's great. You'll be asked medium level questions")
        print()
        Question_list = Question_list_medium


      # if hard, the programw will print easy questions
      elif quiz_difficulty == "hard":
        print("That's great. You'll be asked hard questions")
        print()
        Question_list = Question_list_hard

      # if xxx, program discontinues
      elif quiz_difficulty == "xxx":
        print ("Thanks for playing the Te Reo Maaori Quiz")
        print ("We hope to see you again")
        time.sleep(2)
        exit()
    # if yes or anything else, the user will play on the same difficulty
    else:
      print("You will play on the same difficulty")

    print ()
    
    # If user did play with lives earlier, asks user how many lives they would like to play for the second time
    play_lives = input ("Would you like to play with lives\n")

    # if yes, the user will be asked how many lives would they like to have
    if play_lives == "yes":
      print ("Thats great")
      print("How many lives would you like to play with")
      user_lives = int(input()) 
      print("You will be playing with {} lives".format(user_lives))

    # else, lives will equal nothing
    else:
        print("You will not be playing with lives")
        user_lives = ()

    print("Goold luck!!!")
    print()
      
#import random
import time
import random
# Made by Kafi Ashkir

# dictionaries with questions and answers. Most questions are from the website https://www.tepapa.govt.nz/discover-collections/read-watch-play/maori/te-reo-maori-quiz. Please go check them out because this program wouldn't be that good if I didn't have their questions (I don't own the questions but they're owned by teppa.govt.nz). 

credit_to_website = "(questions are from tepapa.govt.nz)"

# Easy mode questions and answers
Question_list_easy = {
   "when would you say kia ora? \n A. when you are saying hello to someone\n B. when your wishing someone good health \n C. when you're agreeing with someone \n D. all of the above": ["d", "all of the above",],
   "what's the second line of the new Zealand national anthem?":["o nga iwi matou ra"], 
   "What is ocean in Te Reo Maaori? \n A. kātao\n B. Moana\n C. Awa \n D. Wai":["b", "moana"],
   "What's red in Te Reo Maaori? \n A. whero \n B. Red \n C. whrea \n D. rato" :["a","whero"],
   "what is six in Te Reo Maaori? \n A. Wha  \n B. toro \n C. Rua \n D. ono":
   ["d","ono"]  
   } 
# Medium mode questions and answers
Question_list_medium = {
   "what's the job of a macron?" :["to lengthen a vowel", "vowel", "to extend a vowel", "extend vowel"],
   "what would you catch with a paa kahwai?  \n A. pekkatua \n B. ika \n C. manu \n D. Matai \n " :["b", "ika"], 
   "If you gave a donation, gift or contribution, you would give a ?":["koha"],
   "If you are welcoming someone to a school or marae, you would of give a ?":["powhiri"],
   "What colour is the underside of the ponga found? \n A. Hirwa \n B. Kakariki \n C. Pango \n D. whakiriki \n":["hirwa", "a"]
   } 
# Hard mode questions and answers
Question_list_hard = {
   "What is the translation of hei tiki??":["neck pendent","neck pendent of human form", "neck pendent"],
   "what would be stored in a paataka? Pikapuka, kai, or waka?" :["kai"], 
   "what is te reo maaori name for the rugby union?":["hutuporo"],
   "if it is ua, what is it?" :["rainy"],
   "if you were going for a hikoi you are?" :["going for a walk", "walk"]
   }


# functions 

# Played_before function. The function asks the user a question (Have you played the te Reo maaori quiz before) and uses valid = False to make while not valid which equals true which puts the component in a constant loop which only stops if the user does something that goes into the if block which has the return response which takes the program out of the function.

# It uses if, elif, and else statements to execute a part of code if a condition is true. As you can see if the user types yes or y, it returns the user's response (which makes the program exit the function and allows the program to move to the next thing). There is no return under the else statement because I want the question to repeat if the user does something that falls into the else statement.
def played_before(question):
  # puts question in forever loop
  valid=False
  # while not valid (while true) loops the program
  while not valid:
    # asks user the question
    user_response = input (question) .lower()

    # if user types yes or y, the users response will equal (mean the same as) yes 
    if user_response == "yes" or user_response  == "y":   
        user_response = "yes"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return user_response

    # if user types no or n, the users response will equal (mean the same as) no 
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return user_response 

    # if the user types xxx, the program will end.
    elif user_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()

    # else, the program will ask the user to type yes or no or type xxx to quit then the question repeats
    else:
      print("Please say yes or no") 
      print("Or type xxx to quit") 


# Choose difficulty function. The function asks the user a question (What difficulty would you like to play easy, medium, or hard.) and uses valid = False to make while not valid = true which puts the component in a constant loop which only stops if the user does something that falls into the if block which has return which takes the program out of the function. 
def Chosen_difficulty(question):
  # makes valid = false which makes while not valid true
  valid=False
  # while not valid (while true) loops the program
  while not valid:
    # response = input (question).lower() meaning that the users response equals the input to the question. The .lower() makes upper case inputs into lower case letters
    response = input (question) .lower()
    
    # if response = easy, the program will be played on easy
    if response == "easy": 
        response = "easy"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return response
        
    # if response = medium, the program will be played on medium    
    elif response == "medium":
        response = "medium"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return response 

    # if response = hard, the program will be played on hard.
    elif response == "hard":
      response = "hard"
      # The program returns the response which tells the program to exit the function and to run the rest of the program
      return response      

    # if user types xxx, the program ends
    elif response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()     

    # else, the program will ask the user to type easy, medium, or hard or xxx to quit. The question will repeat
    else:
      print("Please choose easy, medium or hard") 
      print("Or type xxx to quit")

# Play_lives function. The function asks the user a question (Would you like to play with lives). It also uses valid = False to make while not valid = true which puts the component in a constant loop which only stops if the user does something that goes into the if block.

# It uses if, elif, and else statements to execute a part of code. If the user's response falls into an if or elif statement, the program returns the user's response (which makes the program exit the function and allows the program to move to the next thing). There is no return under the else statement because I want the question to repeat if the user does something that falls into the else statement.
def play_lives(question):
  # puts question in forever loop
  valid=False
  # while not valid (while true) loops the program
  while not valid:
    # asks user the question
    user_response = input (question) .lower()

    # if user types yes or y, the user will play with lives
    if user_response == "yes" or user_response  == "y":   
        user_response = "yes"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return user_response

    # if user types no or n, the user will not play with lives
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return user_response 

    # if the user types xxx, the program will end.
    elif user_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      time.sleep(2)
      exit()

    # else, the program will ask the user to type yes or no or type xxx to quit, then the question repeats
    else:
      print("please type yes, no, or xxx to quit") 


# lives_check function. This function asks the user a question (How many lives would you like to play with) and uses valid = False to make while not valid = true which puts the component in a constant loop which only stops if the user does something that goes into the if block. The reason why the valid = false means true is because if it doesn't equal false it must equal true. It also uses try to check for errors and it also uses except ValueError to handle the error message

# It uses if and else statements to execute a part of code. If the user types a number between 0 and 10, the program will return the user's response (which makes the program exit the function and allows the program to move onto the next thing). There is no return under the else statement because I want the question to repeat again if the user does something that falls into the else statement. The function also only allows answers in whole numbers and numbers between 1 and 10. If the user inputs something that isn't a whole number or is between 1 and 10, the program will input an error.
def lives_check (question, low, high):
  # the error code that appears when the user types something that causes an error (A number that isn't between 0 and 10 or a number that is a decimal, or is typed in words)
  error = "please enter a whole number between 0 and 10\n"
  # valid = false which makes while not valid meanwhile true because if it "while not false" that means it is "while true"
  # valid = false which helps put the function in a loop
  valid = False
  # while not valid (while true) loops the program
  while not valid:
    # try block tests for errors
    try:
      # users response = an integer input meaning that the users response must be an integer
      response = int(input(question))
      #if the amount is too low /too high give
      if 0 < response <= 10:
        # The program returns the response which tells the program to exit the function and to run the rest of the program
        return response
      #output an error if the user's response isn't a whole number between 0 and 10
      else:
        print(error)
    # handles the ValueError message and makes the program print the error message 
    except ValueError:
     # prints error message instead of the ValueError message so the program doesn't syntax error
     print(error)

# Main Routine

# welcomes the user
print("Welcome to the Te Reo Maaori quiz")
# Asks user their name
print("What is your amazing name?")
# The users input when asnwering their name is stored in a variable which is then printed when the program greets the user in Te Reo Maaori
name = input ( )
print("Kia Ora " + name)

#asks user if they have played the Te Reo Maaori quiz
played_quiz = played_before ("Have you played the Te Reo Maaori quiz before " + name + "?" + "\n" )

# if yes, program continues
if played_quiz == "yes":
  print("That's amazing")
  
# if no, explains what the quiz is
elif played_quiz == "no":
  print("The Te Reo Maaori quiz is a program which helps students get better at speaking Te Reo Maaori")
  print("It has easy, medium, and hard difficulties and many questions which I got from the website tepapa.govt.nz which is the website for the New Zealand national museum")
  print()

# if xxx, program ends
elif played_quiz == "xxx":
  print("Thanks for playing the Te Reo Maaori quiz")
  print("We hope to see you again")
  time.sleep(2)
  exit()

# else, asks user to type yes or no or xxx to quit then the question repeats
else:
  print("Please say yes or no") 


# program asks the user if they would like to play on easy, medium, or hard
quiz_difficulty = Chosen_difficulty ("Would you like to play the quiz on easy, medium, or hard\n").lower()

# if easy, the program will print easy questions
if quiz_difficulty == "easy":
  print("That's great, you will be asked easy level questions which I got from the national New Zealand museum website teppa.govt.nz")
  # Changes the dictionary to the difficulty the user has chosen.
  Question_list = Question_list_easy
  print()


# if medium, the program will print medium questions
elif quiz_difficulty == "medium":
  print("That's great, you will be asked medium level questions which I got from the national New Zealand museum website teppa.govt.nz")
  # Changes the dictionary to the difficulty the user has chosen.
  Question_list = Question_list_medium
  print()

# if hard, the program will print hard questions
elif quiz_difficulty == "hard":
  print("That's great, you will be asked hard level questions which I got from the national New Zealand museum website teppa.govt.nz")
  # Changes the dictionary to the difficulty the user has chosen.
  Question_list = Question_list_hard
  print()

# if xxx, program discontinues
elif quiz_difficulty == "xxx":
  print ("Thanks for playing the Te Reo Maaori Quiz")
  print ("We hope to see you again")
  time.sleep(2)
  exit()

# else, the program will ask the user to type easy, medium, hard or xxx, then the question repeats
else:
  print("please type easy, medium, or hard. or xxx to quit")   

# asks the user if they would like to play with lives
user_play_lives = play_lives ("Would you like to play with lives\n").lower()

# if yes, the user will be asked how many lives would they like to have
if user_play_lives == "yes":
  print ("That's great")
  # asks the user how many lives they would like to play with (Must be a number between 0 and 10)
  user_lives = lives_check ("How many lives would you like to play with? ", 0, 10)
  print("That's amazing! You will be playing with {} lives".format(user_lives))
  print()

# if no, the user will not play with lives
elif user_play_lives == "no":
  print ("That's great")
  print("You will not be playing with lives")
  user_lives = ()

# else, the user will be asked to typed yes or no, or xxx to quit
else:
  print("please type yes, no, or xxx to quit")


# wishes the user good luck and and gives credit to website
print("GOOD LUCK!!! {}. I didn't make the questions".format(credit_to_website))
print()

# score = 0 but goes up by 1 if the user gets a question correct
score = 0
while True:
  # the question = one of the questions in the list
  question = list (Question_list.keys())
  #input answer here 
  while True:
      if not question:
          break
      # the variable which will have the randomly chose question will have the same value as random.choice(question) which is why the variable is named randomized_question. 
      # random.choice(question) randomly picks one of the questions in the dictionary
      randomize_question = random.choice(question)
      # program prints random question from dictionary. Dictionary questions vary depending on what difficulty the user chose
      print(randomize_question)
      while True:
          # the users answer = the variable answer
          answer = input('Answer ' )
          # if answer is correct, it moves onto next question
          if answer.lower() in Question_list[randomize_question]:
              print("Correct Answer")
              print ()
              # if correct, score goes up by 1
              score += 1
              # tells user their score
              print("your score is now", score)
              print()
              # breaks loop and asks the next question
              break
          # else (If not answer)
          else:
              print("Wrong Answer, try again")
              # if user_lives doesn't = () then minus 1 life
              if user_lives != ():
                user_lives -= 1
                # if user has less than 1 life (0 lives), tell the user they have run out of lives and end program with exit()
                if user_lives < 1:
                  print()
                  print ("You've run out of lives")
                  print("Thanks for playing the Te Reo quiz"\
                  " We hope to see you again")
                  time.sleep(2)
                  # ends the program with exit()
                  exit()
                else:
                  # if the user has less than 2 lives, the program will print you have one life left
                  if user_lives < 2:
                    print("You now have one life left")
                    print()
                  else:
                    # tells the user how many lives they have left
                    print("You now have {} lives left".format(user_lives))
                    print()
                    print("Try again")
                    # component loops and asks user the question they just got wrong
      question.remove(randomize_question)
  print("You did very well")
  # if user played with lives, the program will tell the user how many lives they had left and their final score
  if user_lives != ():
    print("Your final score was {} and you had {} lives left".format(score, user_lives) )
  # if the user didn't play with lives, the program will only tell them their final score
  else:
    print("Your final score was", score)
    
  # program asks the user if they would like to play the quiz again
  play_again = input("Would you like to play the quiz again? Maybe you'll be able to beat your high score. (You'll be able to change the difficulty and the lives)\n").lower()

  #if answer is not yes, break the outer infinite loop and end the program
  if play_again != "yes": 
    print("Thanks for playing")
    time.sleep(2)
    break 


  else:
    # score = 0 now because the user wants to play again
    score = 0
    print()
    print("That's amazing, you can always type xxx to end the program by the way")
    # ask the user if they would like to play on the same difficulty
    same_difficulty = input ("Would like to play on the same difficulty?\n").lower()
    # if no, ask what difficulty they would like to play
    if same_difficulty == "no":

      # Asks user if they would like to play on easy, medium, or hard
      quiz_difficulty = Chosen_difficulty ("Would you like to play on easy, medium, or hard\n").lower()

      # if easy, the program will print easy questions
      if quiz_difficulty == "easy":
        print("That's great. You'll be asked easy questions which I got from the national New Zealand museum website teppa.govt.nz")
        print()
        # switches to the dictionary with easy questions
        Question_list = Question_list_easy


      # if medium, the program will print medium questions
      elif quiz_difficulty == "medium":
        print("That's great. You'll be asked medium level questions which I got from the national New Zealand museum website teppa.govt.nz")
        print()
        # switches to the dictionary with medium questions
        Question_list = Question_list_medium


      # if hard, the program will print hard questions
      elif quiz_difficulty == "hard":
        print("That's great. You'll be asked hard questions which I got from the national New Zealand museum website teppa.govt.nz")
        print()
        # switches to the dictionary with hard questions
        Question_list = Question_list_hard

      # if xxx, break the outer infinite loop and end the program
      elif quiz_difficulty == "xxx":
        print ("Thanks for playing the Te Reo Maaori Quiz")
        print ("We hope to see you again")
        time.sleep(2)
        break
  
    # if yes or anything else, the user will play on the same difficulty
    else:
      print("You will play on the same difficulty")

    print ()
    
    # asks the user if they would like to play with lives
    user_play_lives = play_lives ("Would you like to play with lives\n").lower()

    # if yes, the user will be asked how many lives would they like to have
    if user_play_lives == "yes":
      print ("That's great")
      # asks the user how many lives they would like to play with (Must be a number between 0 and 10)
      user_lives = lives_check ("How many lives would you like to play with? ", 0, 10)
      print("That's amazing! You will be playing with {} lives".format(user_lives))
      print()

    # if yes, the user will be asked how many lives would they like to have
    if user_play_lives == "no":
      print ("That's great")
      print("You will not be playing with lives")
      user_lives = ()

    # if xxx, break the outer infinite loop and end the program
    elif user_play_lives == "xxx":
      print ("Thanks for playing the Te Reo Maaori Quiz")
      print ("We hope to see you again")
      time.sleep(2)
      break

    # else, the user will be playing with no lives and lives will = nothing
    else:
      print("please type yes, no, or xxx to quit")

    print("GOOD LUCK!!! {}. I didn't make the questions".format(credit_to_website))
    print()
    # program loops and asks questions again

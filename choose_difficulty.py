import random

# dictionaries

# Easy mode questions and answers
Question_list_easy = {
   "when would you say kia ora? \n A. when your saying hello to someone\n B. when your wishing someone good health \n C. when your agreeing with someone \n D. all of the above": ["d", "all of the above"],
   "whats the second line of the new zealand national athem?":["o nga iwi matou ra"], 
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
   "If you gave a donation, gift or contribution, you would give a ?":["koha"],
   "If you are welcoming someone to a school or marae, you would of give a ?":["powhiri"],
   "what colour is the underside of the ponga fround? \n A. Hirwa \n B. Kakariki \n C. Pango \n D. whakiriki \n":["hirwa", "a"]
   } 
# Hard mode questions and answers
Question_list_hard = {
   "what is the translation of hei tiki??":["neck pendant of human form"],
   "what would be stored in a paataka? Pikapuka, kai or waka?" :["kai"], 
   "what is te reo maaori name for the rugby union?":["hutuporo"],
   "if it is ua, what is it?" :["rainy"],
   "if you were going for a hikoi you are?" :["going for a walk"]
   }

# functions

# Choose difficulty function. The function asks the user a question (What difficulty would you like to play easy, medium, or hard.) and uses valid = False to make make while not valid = true which puts the component in a constant loop which only stops if the user does something that goes into the if block which has the return response which takes the program out of the function. The reason why the valid = false means true is because if it doesn't equal false it must equal true. It also uses .lower() to turn all upper case inputs into lower case leters
def Chosen_difficulty(question):
  # makes valid = false which makes while not valid mean while true because if its while not false that means it means while true.
  valid=False
  # while not valid (while true) loops the program
  while not valid:
    # response = input (question).lower() meaning that the users response equals the input to the question. The .lower() makes upper case inputs into lower case letters
    response = input (question) .lower()
    
    # if response = easy, then the users response will be know as easy
    if response == "easy": 
        response = "easy"
        # return response which tells the program to exit the function and to run the rest of the program
        return response
        
    # if response = easy, then the users response will be know as easy    
    elif response == "medium":
        response = "medium"
        # return response which tells the program to exit the function and to run the rest of the program
        return response 

    # if response = easy, then the users response will be know as easy 
    elif response == "hard":
      response = "hard"
      # return response which tells the program to exit the function and to run the rest of the program
      return response      

    # if user types xxx, the program ends
    elif response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      exit()     

    # else, the program will ask the user to type easy, medium, or hard or xxx to quit. The the question will repeat
    else:
      print("Please choose easy, medium or hard") 
      print("Or type xxx to quit")


# program asks user if they would like to play on easy, medium, or hard
quiz_difficulty = Chosen_difficulty ("Would you like to play on easy, medium, or hard\n").lower()

# if easy, the programw will print easy questions
if quiz_difficulty == "easy":
  print("Thats great, you will be asked easy level questions")
  # switches to the dictionary with easy questions
  Question_list = Question_list_easy


# if medium, the programw will print easy questions
elif quiz_difficulty == "medium":
  print("Thats great, you will be asked medium level questions")
  # switches to the dictionary with medium questions
  Question_list = Question_list_medium


# if hard, the programw will print easy questions
elif quiz_difficulty == "hard":
  print("Thats great, you will be asked hard level questions")
  # switches to the dictionary with hard questions
  Question_list = Question_list_hard

# if xxx, program discontinues
elif quiz_difficulty == "xxx":
  print ("Thanks for playing the Te Reo Maaori Quiz")
  print ("We hope to see you again")
  exit()


score = 0
question = list (Question_list.keys())
#input answer here 
while True:
    if not question:
        break
    ques = random.choice(question)
    print(ques)
    while True:
        answer = input('Answer ' )
        # if correct, moves onto next question
        if answer.lower() in Question_list[ques]:
            print("Correct Answer")
            print ()
            # if correct, score goes up by 1
            score += 1
            print("total score is", score)
            print()
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer, try again")
    question.remove(ques)
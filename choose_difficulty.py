import random
import time

Question_list_easy = {
   "when would you say kia ora? \n A. when your saying hello to someone\n B. when your wishing someone good health \n C. when your agreeing with someone \n D. all of the above": ["d", "all of the above"],
   "whats the second line of the new zealand national athem?":"o nga iwi matou ra", 
   "What is ocean in Te Reo Maaori? \n A. kātao\n B. Moana\n C. Awa \n D. Wai":["b", "moana"],
   "Whats red in Te Reo Maaori? \n A. whero \n B. Red \n C. whrea \n D. rato" :
   ["a","whero"],
   "what is six in Te Reo Maaori? \n A. Wha  \n B. toro \n C. Rua \n D. ono":
   ["d", "ono"]  
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
   "if you were going for a hikoi you are?" :"going for a walk"}



# user difficulty function
def Chosen_difficulty(question):
  valid=False
  while not valid:
    difficulty_response = input (question) .lower()

    if difficulty_response == "easy": 
        difficulty_response = "easy"
        return difficulty_response
        
    elif difficulty_response == "medium":
        difficulty_response = "medium"
        return difficulty_response 

    elif difficulty_response == "hard":
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

# if easy, the program will print easy questions
if quiz_difficulty == "easy":
  Question_list = Question_list_easy


# if medium, the program will print easy questions
elif quiz_difficulty == "medium":
  Question_list = Question_list_medium


# if hard, the program will print easy questions
elif quiz_difficulty == "hard":
  Question_list = Question_list_hard

# if xxx, program discontinues
elif quiz_difficulty == "xxx":
  print ("Thanks for playing the Te Reo Maaori Quiz")
  print ("We hope to see you again")
  time.sleep(2)
  exit()

else:
  print("please type easy, medium, or hard")


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
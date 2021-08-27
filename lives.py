import random

play_lives = input ("Would you like to play with lives\n")

# if yes, the user will be asked how many lives would they like to have
if play_lives == "yes":
  print ("Thats great")
  print("How many lives would you like to play with")
  user_lives = int(input()) 
  print("You will be playing with {} lives".format(user_lives))


else:
  user_lives = ()
  print("You will not be playing with lives")

# quiz questions 
Questions_answers = {
    "What is red in Te Reo Maaori?  \n A. whero \n B. Red \n C. whrea \n D. rato" :["a", "whero"],
}   

score = 0
question = list (Questions_answers.keys())
#input answer here 
while True:
    if not question:
        break
    ques = random.choice(question)
    print(ques)
    while True:
        answer = input('Answer ' )
        # if correct, moves onto next question
        if answer.lower() in Questions_answers[ques]:
            print("Correct Answer")
            print()
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer, try again")
            user_lives-=1
            print("You now have {} lives left".format(user_lives))
            if user_lives < 1:
              print()
              print("Thanks for playing the Te Reo quiz"\
              " we hope to see you again")
              exit()  

    question.remove(ques)
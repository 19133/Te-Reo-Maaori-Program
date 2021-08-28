import random

# lives_check function. The function asks the user a question (How many lives would you like to play with) and uses valid = False to make make while not valid = true which puts the component in a constant loop which only stops if the user does something that goes into the if block which has the return response which takes the program out of the function. The reason why the valid = false means true is because if it doesn't equal false it must equal true. It also uses try to check for errors and it also uses except ValueError to handle the error message

# It uses if and else statements to execute a part of code if a condition is true. As you can see if the user types a number between 1 and 10, the program will return the users response (which makes the program exit the function and allows the program to move to the next thing). There is no return under the else statement because I want the question to repeat again if the user does something that falls into the else statement. The function aslo only allows answers in integers and inputs an error if the user types something that isn't a integer (a integer is a whole number), or an iteger that isn't between 1 and 10.
def lives_check (question, low, high):
  # the error code that appears when the user types something that causes an error
  error = "please enter a whole number between 1 and 10\n"
  # valid = false which makes while not valid mean while true because if its while not false that means it means while true
  # valid = false which helps put the function in a loop
  valid = False
  # while not valid (while true) loops the program
  while not valid:
    # try block tests for errors
    try:
      # users response = an integer input meaning that the users response must be an integer
      response = int(input(question))
      #if the amount is too low /too high give
      if 1 < response <= 10:
        # return response which tells the program to exit the function and to run the rest of the program
        return response
      #output an error if the users response isn't a whole number between 1 and 10
      else:
        print(error)
    # handles the ValueError message and makes the program print the error message 
    except ValueError:
     print(error)

# asks user if they would like to play with lives
play_lives = input ("Would you like to play with lives\n")

# if yes, the user will be asked how many lives would they like to have
if play_lives == "yes":
  print ("Thats great")
  print("How many lives would you like to play with")
  # asks user how many lives they would like to play with (Must be a number between 1 and 10)
  user_lives = lives_check ("how much many lives would you like to play with? ", 0, 10)
  print("you will be playing with {} lives".format(user_lives))

# else, user will be playing with no lives and lives will = nothing
else:
  print("You will be playing with 0 lives")
  user_lives = ()

# questions list, (using one question for testing purposes)
Questions_answers = {
    "What is red in Te Reo Maaori?  \n A. whero \n B. Red \n C. whrea \n D. rato" :["a", "whero"],
}   

score = 0
question = list (Questions_answers.keys()) 
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
            print ()
            # if correct, score goes up by 1
            score += 1
            print("your score is now", score)
            print()
            break
        else:
            #if wrong, Asks the same question again
            print("Wrong Answer, try again")
            if user_lives != ():
              user_lives -= 1
              if user_lives < 1:
                print()
                print ("You've run out of lives")
                print("Thanks for playing the Te Reo quiz"\
                " we hope to see you again")
                exit()
              else:
                if user_lives < 2:
                  print("You now have one life left")
                  print()
                else:
                  print("You now have {} lives left".format(user_lives))
                  print()
                  print("Try again")
    question.remove(ques)
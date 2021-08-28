# Played_before function. The function asks the user a question (Have you played the tereo maaori quiz before) and uses valid = False to make make while not valid = true which puts the component in a constant loop which only stops if the user does something that goes into the if block which has the return response which takes the program out of the function.

# It uses if, elif and else statements to execute a part of code if a condition is true. As you can see if the user types yes or y, it returns the users response (which makes the program exit the function and allows the program to move to the next thing). There is no return under the else statement because I want the quetion to repeat again if the user doesn something that falls into the else statement.
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
        # return response which tells the program to exit the function and to run the rest of the program
        return user_response

    # if user types no or n, the users response will equal (mean the same as) no 
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        # return response which tells the program to exit the function and to run the rest of the program
        return user_response 

    # if the user types xxx, the program will end.
    elif user_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")
      exit()

    # else, the program will ask the user to type yes or no or type xxx to quit then the question repeats
    else:
      print("Please say yes or no") 
      print("Or type xxx to quit") 

# Main Routine

# welcomes user and asks users name
print("Welcome to the Te Reo Maaori quiz")
# Asks user their name
print("What is your amazing name?")
name = input ( )
print("Kia Ora " + name)

#asks user if they have played the Te Reo Maaori quiz
played_quiz = played_before ("Have you played the Te Reo Maori quiz " + name + "?" + "\n" )

# if yes, program continues
if played_quiz == "yes":
  print("That's amazing")
  
# if no, explains what the quiz is
elif played_quiz == "no":
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

# if xxx, program ends
elif played_quiz == "xxx":
  print("Thanks for playing the Te Reo Maaori quiz")
  print("We hope to see you again")
  exit()
# else, asks user to type yes or no or xxx to quit then the question repeats
else:
  print("Please say yes or no") 

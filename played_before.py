
# yes/no function
def played_before(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "yes" or user_response  == "y":   
        user_response = "yes"
        return user_response
      
    elif user_response == "no" or user_response  == "n":
        user_response = "no"
        return user_response 

    elif user_response == "xxx":
      print("Thanks for playing the Te Reo Maaori quiz")
      print("We hope to see you again")


    else:
      print("Please say yes or no") 
      print("Or type xxx to quit") 

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
  print("program continues")
  
# if no, explains what the quiz is
elif played_quiz == "no":
  print("Thats ok")
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

# if xxx, program ends
elif played_quiz == "xxx":
  print("Thanks for playing the Te Reo Maaori quiz")
  print("We hope to see you again")

# else, asks user to type yes or no or xxx to quit then the question repeats
else:
  print("Please say yes or no") 

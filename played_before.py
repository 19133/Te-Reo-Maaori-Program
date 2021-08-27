# welcomes user and asks users name
print("Welcome to the Te Reo Maaori quiz")
# Asks user their name
print("What is your amazing name?")
name = input ( )
print("Kia Ora " + name)

#asks user if they have played the Te Reo Maaori quiz
played_before = input ("Have you played the Te Reo Maori quiz " + name + "?" + "\n" )

# if yes, program continues
if played_before == "yes":
  print("program continues")
  
# if no, explains what the quiz is
elif played_before == "no":
  print("Thats ok")
  print("The Te Reo Maaori quiz is a program which tests and helps students enhance their Te Reo Maaori language skill")

# else, asks user to type yes or no or xxx to quit then the question repeats
else:
  print("Please say yes or no") 
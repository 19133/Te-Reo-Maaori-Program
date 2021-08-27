# quiz questions 
Questions_answers = {
    "What is ocean in Te Reo Maaori? \n A. kātao\n B. Moana\n C. Awa \n D. Wai":"b" or "moana",
    "What is red in Te Reo Maaori?  \n A. whero \n B. Red \n C. whrea \n D. rato" :"a" or "whero",
    "If it is Ua it is what? \n A. Rainy \n B. Sunny \n C. hot \n D. 21 hours ":"a" or "rainy"
}   

score = 0
question = list (Questions_answers.keys())
#input answer here 
while True:
  answer = input('Answer ' )
  # if correct, moves onto next question
  if answer.lower() == Questions_answers:
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
question.remove

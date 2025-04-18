def QuestionsMarks(strParam):
  result = False

  for i in range(len(strParam)):
    if strParam[i].isdigit(): #check if the the character is a number
      for j in range(i+1, len(strParam)):
        if strParam[j].isdigit(): #check if the next character is a number
          if int(strParam[i])+int(strParam[j])==10: #check if the sum of the first and second numbers is 10
            between = strParam[i+1:j] #get the characters between the two numbers
            if between.count("?") != 3: #check if there are three question marks between the numbers
              return "false"
            else:
              result = True
          break

  return "true" if result else "false"

print(QuestionsMarks(input()))

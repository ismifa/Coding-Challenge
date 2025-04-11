def BracketMatcher(strParam):
  bracket = []

  for i in strParam:
    if i == '(':
      bracket.append(i)
    elif i == ')':
      if not bracket:
        return 0
      bracket.pop() #remove the last opening parenthesis that has a matching closing one
      
  return 1

print(BracketMatcher(input()))

import re

def CodelandUsernameValidation(strParam):
  str_len = len(strParam)

  if str_len >= 4 and str_len <= 25 and strParam[0].isalpha() and bool(re.fullmatch(r'\w+', strParam)) and not strParam.endswith('_'):
    result = 'true'
  else:
    result = 'false'

  return result

print(CodelandUsernameValidation(input()))

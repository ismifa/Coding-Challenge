import re

def LongestWord(sen):
  words = re.findall(r'\b\w+\b', sen) #split string
  longest = max(words, key=len) #find the longest word
  
  return longest

print(LongestWord(input()))

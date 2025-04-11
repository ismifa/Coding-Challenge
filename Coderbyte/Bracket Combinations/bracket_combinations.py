import math

def BracketCombinations(num):
  # Catalan number formula
  C = 1/(num+1)*math.comb(2*num, num)

  return int(C)

print(BracketCombinations(input()))

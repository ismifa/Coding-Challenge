from collections import Counter

def TreeConstructor(strArr):
  child_list = []
  parent_list = []

  # Split pairs of integers
  for i in strArr:
    child, parent = map(int, i.strip("()").split(","))
    child_list.append(child)
    parent_list.append(parent)

  # Check whether a parent has more than 2 children
  for i,j in Counter(parent_list).items():
    if j > 2:
      return 'false'

  # Check whether a child has more than 1 parent
  for i,j in Counter(child_list).items():
    if j > 1:
      return 'false'

  return 'true'

print(TreeConstructor(input()))

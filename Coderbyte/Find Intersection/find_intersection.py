def FindIntersection(strArr):
  num_list = [list(map(int, i.split(", "))) for i in strArr] #convert a list of strings into a list of integers

  intersection = set(num_list[0]) & set(num_list[1]) #find the intersection between two lists
  sorted_intersection = ",".join(str(i) for i in sorted(intersection)) #sorts the numbers, turns them into strings, and joins them with commas

  # Case when there is no intersection
  if len(intersection) == 0:
    return 'false'

  return sorted_intersection

print(FindIntersection(input()))

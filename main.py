#function letter_count(), which takes a word list and returns a dictionary which has the letters as keys and the values the number of times each letter appears in the word list.

def letter_count(d):
  new = {}
  
  for zoo in d:
    for letter in zoo:
      if letter in new:
        new[letter] += 1
      else:
        new[letter] = 1
  return new
  
d = ['car', 'bat', 'rat']

print("\nInput: ", d)
print("Output: ", letter_count(d), '\n')
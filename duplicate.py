def remove_duplicates(word):
  numbers_game = "".join(sorted(dict.fromkeys(word)))
  return (numbers_game, len(word) - len(numbers_game))

print (remove_duplicates('aaabbbac'))
print (remove_duplicates('a'))
print (remove_duplicates('thelexash'))
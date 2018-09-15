def is_isogram(word):
 if not isinstance(word, str):
  raise TypeError('Argument should be a string')
 if not word:
  isogram = False
 if word == " ":
  isogram = False
 else:
  isogram = len(word) == len(set(word.lower()))
 return word, isogram

print is_isogram('abolishment')
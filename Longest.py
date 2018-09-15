def longest(string):
  sentence = string.split(' ')
  return max (sentence, key = len)

print (longest("This is Andela"))
print (longest("Brilliance is evenly distributed"))
  
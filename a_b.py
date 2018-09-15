def power(a,b):
  return 1 if b == 0 else a * power(a, b - 1)
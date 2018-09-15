def my_sort(num):
  odd = [i for i in num if i % 2 != 0]
  even = [i for i in num if i % 2== 0]
  
  return sorted(odd) + sorted(even)
print (my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print (my_sort([1, 2]))
print (my_sort([2, 1]))
print (my_sort([3, 3, 4]))
print (my_sort([90, 45, 66]))
def num_check(my_list):
    
    numbers_list = []
    for num in my_list:
        if not isinstance(num, int):
            raise TypeError('List must contain numbers only.')
        else:
            if my_list.count(num) >= 3:
                numbers_list.append(num)
        
    remaining = [num for num in my_list if num not in numbers_list]

    return tuple(remaining)

print(num_check([7,7,7,5,5,1,5,]))
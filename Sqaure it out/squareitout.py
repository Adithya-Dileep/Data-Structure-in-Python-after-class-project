sqaures = [1,2,3,4,5,6,7,8,9,10]
print('List of square values:', sqaures)
odd_sqaures = [num for num in sqaures if num % 2 != 0]
even_squares = [num for num  in sqaures if num % 2 == 0]
print('Odd squares:', odd_sqaures)
print('Even squares:', even_squares)
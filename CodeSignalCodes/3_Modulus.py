'''
Your task is to implement a function that, given a number n, returns -1 
if this number is not an integer and n % 2 otherwise. It is guaranteed that 
if the number represents an integer, it will be written without a decimal point.
'''
#Solution1
def solution1(n):
    if isinstance(n, int) :
        return n % 2
    else:
        return -1

#Solution 2
def solution2(n):
    if type(n)==int :
        return n % 2
    else:
        return -1

print(solution1(15))
print(solution2(15.3))

'''Difference between isinstance and type
Speed is not the only difference between these two functions. There is actually an important distinction between how they work:

type only returns the type of an object (its class). We can use it to check if variable is of a type str.
isinstance checks if a given object (first parameter) is:
an instance of a class specified as a second parameter. For example, is variable an instance of the str class?
or an instance of a subclass of a class specified as a second parameter. In other words - is variable an instance of a subclass of str? '''
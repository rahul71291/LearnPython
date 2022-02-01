#For n = 50, the output should be
#solution(n) = 6.

#50 = 110010, a number that consists of 6 digits. Thus, the output should be 6.

#Solution 1
def countBits(n):
    ntobin = (bin(n)[2:len(bin(n))])
    return len(ntobin)

#Solution2 
def solution(n):
    return len(bin(n)[2:len(bin(n))])

#solution 3 
# int.bit_length()
#Returns the number of bits required to represent an 
#integer in binary, excluding the sign and leading zeros
def bit_length(n):
    return n.bit_length()

n = int(input("Please Enter a number : "))
print(countBits(n))
print(solution(n))
print(bit_length(n))

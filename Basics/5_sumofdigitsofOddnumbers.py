# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
# odd = x & 1 return True if x is Odd
# even = (not(x & 1)) return True if x is Even
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)

# 11) Given a string S consisting only '0's and '1's, print the last index of the '1' present in
# it.if 1 is not present, print "1 is not present"

# Example input1:
# Enter a string of zeroes and ones: 00101010101010
# Output: 12

# Example input 2:
# Enter a string of zeroes and ones: 00000000000000000000
# Output: 1 is not present 

string = input("enter a string ")
i = string.rfind("1")
if i<0:
    print("1 is not present")
else:
    print(i)
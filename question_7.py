# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.

# Example:

# Input 1:
# aA1_67
# Input 2:
# a987 abC012

# Output 1:
# 1
# Output 2:
def CheckPassword(str,n):
    if n < 4:
        return 0
    if str[0].isnumeric():
        return 0
    num=0
    caps=0
    sp=0
    for i in str:
        if i.isupper():
            caps+=1
        if i.isnumeric():
            num+=1
        if i==" " or i=="/":
            sp+=1
    if caps==1 and num==1 and sp!=1: 
            return True
    else:
            return False
str=input()
n=len(str)
print(CheckPassword(str,n))
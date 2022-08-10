############################################
def r_message():
    return "Recursion is" + r_message_util(0)

def r_message_util(n):
    if n > 10:
        return " fun!"
    return " very" + r_message_util(n+1)

# print (r_message()) #

############################################

# iterative
def print_countdown_iterative(n):
    for i in range(n, -1, -1):
        print(i)

# recursive
def print_countdown_recursive(n):
    if n < 0:
        return
    print(n)
    print_countdown_recursive(n-1)
# usually recursive call modifies input (n)



# print_countdown_iterative(10) #
# print_countdown_recursive(10) #


############################################

def rec_factorial(n): # function definition
    if n <= 1:
        return 1
    return n * rec_factorial(n-1) # shows the recursive call/step
# finds factorial
# 1 would be the base case of the function (because it does not cause recurrsion)

# print(rec_factorial(5))

############################################

# FIBONACCI SEQUENCE: 0, 1, 1, 2, 3, 5, 8, ...

# pattern:
# 5th = 4th + 3rd
# 4th = 3rd + 2nd
# 3rd = 2nd + 1st

# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(n) = fib(n-1) + fib(n-2)

# base case: 
# if n = 1 -> 0
# if n = 2 -> 1

def fibonnaci1(n): # iterative
    assert n > 0
    secondLast = 0
    Last = 1
    if n == 1:
        print(secondLast)
    elif n==2:
        print(Last)
    else:
        for i in range(3, n+1):
            result = secondLast + Last
            secondLast = Last
            Last = result
        print(result)

def fibonnaci2(n): # 
    assert n > 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnaci2(n-1) + fibonnaci2(n-2)

############################################

def isPalindrome(input_str):
    n = len(input_str)
    if n == 0:
        return True
    return isPalindromeRecursive(input_str, 0, n-1)

def isPalindromeRecursive(input_str, start, end):
    if start == end:
        return True

    # skip non-alphanumeric values
    while not input_str[start].isalnum():
        start += 1
    while not input_str[end].isalnum():
        end -= 1
    
    if input_str[start].lower() != input_str[end].lower():
        return False

    if start < end + 1:
        return isPalindromeRecursive(input_str, start + 1, end - 1)
    
    return True
    
# print(isPalindrome("test"))
# print(isPalindrome("kayak"))


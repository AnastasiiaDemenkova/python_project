# WARM_UP-1
# sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.



def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

# Monkey_trouble

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
       return True
    else:
       return False

# diff_21
# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
def diff21(n):
    if n <= 21:
        return (21-n)
    elif n > 21:
        return 2 * (n - 21)

# near_hundred

# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
        if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
            return True
        else:
            return False

def near_hundred(n):
    if 110 >= n >= 90 or 210 >= n >= 190:
        return True

    else:
        return False



#parrot_trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble
def parrot_trouble(talking, hour):
    if talking and hour < 7 or talking and hour >= 21:
        return True
    else:
        return False

# pos_neg
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return ((a < 0 and b > 0) or ( a > 0 and b < 0))







import numpy as np

#The point of this program is to calculate the number that for a given N satisfies x^x = N
def check(N):
    if N <= 1:
        print("Please enter a number greater than 1 for now")
        return check(int(input("Please input an N")))
    else:
        return N

print("Please input an N")
N = float(input())

N = check(N)

lower_limit = 1
upper_limit = N

guess = (lower_limit + upper_limit) / 2

while round(guess - np.log(N)/np.log(guess), 5) != 0:
    guess = (lower_limit + upper_limit) / 2
    #print(guess)
    if guess - np.log(N)/np.log(guess) > 0:
        upper_limit = guess
    elif guess - np.log(N)/np.log(guess) < 0:
        lower_limit = guess

print("{} is the answer".format(guess))

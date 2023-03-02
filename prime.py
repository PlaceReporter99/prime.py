import math
def isprime(n):
    x = 2
    if n == 2:
        return True
    elif n == 3:
        return True
    elif n == 1:
        return False
    else:
        while x <= math.sqrt(n):
            if n % x == 0:
                return False
            else:
                x = x + 1
    return True
def prime(n):
    z = 0
    y = 2
    while z < n:
        if isprime(y):
            z = z + 1
        y = y + 1
    return y - 1
def ask():
    print()
    userask = input("Type 1 if you want to know if a number is prime. Type 2 if you want to know the prime number from the ordinal (Is it the 1st prime, the 2nd prime, etc.). Type any other character to exit the programme. ")
    if userask == "1":
        print()
        isitprime = int(input("What number do you want to check the primality of? "))
        print()
        if isprime(isitprime) == True:
            print(str(isitprime) + " is a prime number!")
        elif isprime(isitprime) == False:
            print(str(isitprime) + " is not a prime number, so it is a composite number (unless it's 1 or 0, those numbers are neither prime nor composite)!")
        else:
            print("There has been an error, the programme has not returned true or false")
    elif userask == "2":
        print()
        nprime = int(input("What ordinal number (enter as cardinal (1, 2, 3, etc.)) would you like to know the prime number of? "))
        print()
        print("The " + str(nprime) + "st/nd/rd/th prime number is " + str(prime(nprime)))
    else:
        quit()
    ask()
ask()
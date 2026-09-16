# Roshan Tamang
# CIT-104 Assignment Three
# Prime Factorization
#
# Algorithm Description:
# 1. Ask the user to enter a number between 2 and 100.
# 2. Start with a possible factor of 2.
# 3. Check whether the number can be divided evenly by the factor.
# 4. If it can, print the factor and divide the number by that factor.
# 5. Continue checking the same factor until it no longer divides evenly.
# 6. Increase the factor by 1 and repeat the process.
# 7. If the original number is prime, print "PRIME".
# 8. Otherwise, print all of the prime factors separated by spaces.


# Get a number from the user.
number = int(input("Input number: "))

# Keep a copy of the original number so we can determine
# whether it was prime after finding its factors.
original_number = number

# Store the prime factors in a list.
factors = []

# Start checking possible factors at 2.
factor = 2

# Continue until the number has been completely factored.
while number > 1:
    # If the current factor divides the number evenly,
    # it is a prime factor.
    if number % factor == 0:
        factors.append(factor)
        number = number // factor
    else:
        # Move to the next possible factor.
        factor += 1

# If there is only one factor and it is the original number,
# then the original number was prime.
if len(factors) == 1 and factors[0] == original_number:
    print("PRIME")
else:
    # Print the prime factors separated by spaces.
    print(*factors)

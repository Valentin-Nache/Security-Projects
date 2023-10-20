import random


# This function performs one iteration of the Miller-Rabin primality test
def test(n):
    # Initialize variables k and q
    k = 0
    q = n - 1

    # Find the largest power of 2 that divides q
    while q % 2 == 0:
        k += 1
        q //= 2

    # Select a random integer a in the range [2, n - 2]
    a = random.randint(2, n - 2)

    # Check if a^q mod n is 1
    if pow(a, q, n) == 1:
        return "inconclusive"

    # Check if a^((2^j) * q) mod n is n - 1 for each value of j from 0 to k - 1
    for j in range(k):
        if pow(a, (2 ** j) * q, n) == n - 1:
            return "inconclusive"

    # If none of the above tests returned "inconclusive", return "composite"
    return "composite"


# This function performs the Miller-Rabin primality test with "rounds" iterations
def miller_rabin(n, rounds):
    # Perform the TEST function "rounds" times
    for _ in range(rounds):
        result = test(n)
        # If any of the tests return "composite", return "composite"
        if result == "composite":
            return "composite"
    # If all of the tests return "probably prime", return "probably prime"
    return "probably prime"


number_to_test = ""
while number_to_test != 0:
    # Get number to be tested from user
    number_to_test = int(input("Please enter the number you would like to test for primality or enter 0 to exit: "))
    # Test 20 times
    if number_to_test != 0:
        print(miller_rabin(number_to_test, 20))



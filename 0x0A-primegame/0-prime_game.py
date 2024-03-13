#!/usr/bin/python3
""" Maria and Ben are playing a game """


def isWinner(x, nums):
    """ Maria and Ben are playing a game """

    def is_prime(num):
        """ Maria and Ben are playing a game """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """ Maria and Ben are playing a game """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(primes, n):
        """ Maria and Ben are playing a game """
        if n % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    wins = {"Maria": 0, "Ben": 0}

    for i in range(x):
        n = nums[i]
        primes = get_primes(n)
        winner = can_win(primes, n)
        wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

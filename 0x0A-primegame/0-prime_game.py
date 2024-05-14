#!/usr/bin/python3
"""Maria and Ben are playing a game"""

def isWinner(x, nums):
    """Function to determine the winner of the game.
    x - rounds
    nums - numbers list
    """
    # If the number of rounds is less than or equal to 0, or the list of numbers is None, return None
    if x <= 0 or nums is None:
        return None
    # If the number of rounds does not match the length of the list of numbers, return None
    if x != len(nums):
        return None

    # Initialize scores for Ben and Maria
    ben = 0
    maria = 0

    # Create a list of 1s with length equal to the maximum number in the list of numbers plus 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # Set the first two elements of the list to 0
    a[0], a[1] = 0, 0
    # Remove multiples of each number in the list
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # For each number in the list of numbers, if the sum of the elements in the list up to that number is even, increment Ben's score; otherwise, increment Maria's score
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # If Ben's score is higher than Maria's, return "Ben"; if Maria's score is higher, return "Maria"; if their scores are equal, return None
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """Function to remove multiples of a given number from a list.
    ls - list
    x - number
    """
    # For each number in the list starting from 2, try to set the element at the index equal to the current number times the given number to 0; if an error occurs (e.g., the index is out of range), break the loop
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break


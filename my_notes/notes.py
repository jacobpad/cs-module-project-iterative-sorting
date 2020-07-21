print('\n\n---------------------------------------------------------------')
import random
import time
print('------ Binary Search ------')
print('Nothing to print here, just made a function.')


def binary_search(list, item):
    '''
    If the guess is too high, you update high to make it lower.
    '''
    low = 0
    high = (len(list) - 1)
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# my_list = [1, 3, 5, 7, 9]
# print('\n', binary_search(my_list, 3))  # => 1 - Remember, lists start at 0. The second slot has index 1.
# print('\n', binary_search(my_list, -1))  # => None - Indicates that the item wasn’t found.


# https://github.com/jacobpad/Computer-Science-Lambda-School/blob/master/grokking_algorithms%20(1).pdf
# EXERCISES - Page 9

# 1.1
#####################################################################
# Suppose you have a sorted list of 128 names, and you’re searching #
# through it using binary search. What’s the maximum number of      #
# steps it would take?                                              #
# ----------------------------------------------------------------- #
# log2(128) ==> 7                                                   #
# 128 ÷ 2 = 64                                                      #
#  64 ÷ 2 = 32                                                      #
#  32 ÷ 2 = 16                                                      #
#  16 ÷ 2 = 8                                                       #
#   8 ÷ 2 = 4                                                       #
#   4 ÷ 2 = 2                                                       #
#   2 ÷ 2 = 1                                                       #
#####################################################################

# 1.2
#####################################################################
# Suppose you double the size of the list. What’s the maximum       #
# number of steps now?                                              #
# ----------------------------------------------------------------- #
# log2(256) ==> 8                                                   #
# 256 ÷ 2 = 128                                                     #
# 128 ÷ 2 = 64                                                      #
#  64 ÷ 2 = 32                                                      #
#  32 ÷ 2 = 16                                                      #
#  16 ÷ 2 = 8                                                       #
#   8 ÷ 2 = 4                                                       #
#   4 ÷ 2 = 2                                                       #
#   2 ÷ 2 = 1                                                       #
#####################################################################

# Page 11
# #######################################################################
# Let’s assume it takes 1 millisecond to check one element. With        #
# simple search, Bob has to check 100 elements, so the search takes     #
# 100 ms to run. On the other hand, he only has to check 7 elements     #
# with binary search (log2 100 is roughly 7), so that search takes 7    #
# ms to run. But realistically, the list will have more like a billion  #
# elements. If it does, how long will simple search take? How long      #
# will binary search take?                                              #
# --------------------------------------------------------------------- #
print('\n---------------------------------------------------------------')
#######################################################################
print('------ Put a "X" items in a list (in order) ------')

start_time = time.time()

# Make a list of X items
my_list = []
X = 10000         # 10,000
# X = 100000      # 100,000
# X = 1000000     # 1,000,000
# X = 10000000    # 10,000,000
# X = 1000000000  # 100,000,000
# X = 1000000000  # 1,000,000,000
print(f'X is: {X}')
Y = random.randint(1, X) # The number to guess

for i in range(X):
    my_list.append(i+1)

end_time = time.time()
print(end_time - start_time, 'seconds')
#######################################################################

print('\n------ The number to guess ------')
print(f'Y is: {Y}')

#######################################################################
print('\n------ Binary Search ------')

start_time = time.time()
print(binary_search(my_list, Y))
end_time = time.time()
print(end_time - start_time, 'seconds')

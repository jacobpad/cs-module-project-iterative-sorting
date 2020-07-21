import random
import time

print('\n---------------------------------------------------Selection Sort---') # 372.9070301055908 seconds


def selection_sort(arr):
    '''https://www.youtube.com/watch?v=5KjapFQNxUo'''

    for i in range(len(arr) - 1):       # Establish the length of the list
        cur_index = i                   # Set the 0 index to a variable
        for j in range(i+1, len(arr)):  #
            if arr[j] < arr[cur_index]:  # If index 'j' is smaller,
                cur_index = j           # It becomes the current index
                #
        temp = arr[i]                   # This
        arr[i] = arr[cur_index]         # Is The
        arr[cur_index] = temp           # Swap
        #
        # print(arr)                    # Uncomment this to see the sorting process
        #
    return arr                          # The return of the passed in list


start_time = time.time()

print('------ Make An Unsorted List ------')
random_list = [(random.randint(1, 10000)) for i in range(100000)]
# print(f'The unsorted list: \n{random_list}')


print('\n------ Pass Array To Function ------')
selection_sort(random_list)
print('Successfully Passed To selection_sort')


print('\n------ Print Sorted List ------')
# print(f'Here is the list in it\'s sorted form:\n{random_list}')


print('\n------ How Long Did It Take? ------')
end_time = time.time()
print(end_time - start_time, 'seconds')


print('\n------------------------------------------------------Bubble Sort---') # 796.8302628993988 seconds


def bubble_sort(arr):
    '''
    https://www.youtube.com/watch?v=Vca808JTbI8
    '''

    temp = 0
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        # print(arr)

    return arr


start_time = time.time()

print('------ Make An Unsorted List ------')
random_list = [(random.randint(1, 10000)) for i in range(100000)]
# print(f'The unsorted list: \n{random_list}')


print('\n------ Pass Array To Function ------')
bubble_sort(random_list)
print('Successfully Passed To selection_sort')


print('\n------ Print Sorted List ------')
# print(f'Here is the list in it\'s sorted form:\n{random_list}')


print('\n------ How Long Did It Take? ------')
end_time = time.time()
print(end_time - start_time, 'seconds')


# '''
# STRETCH: implement the Counting Sort function below

# Counting sort is a sorting algorithm that works on a set of data where
# we specifically know the maximum value that can exist in that set of
# data. The idea behind this algorithm then is that we can create "buckets"
# from 0 up to the max value. This is most easily done by initializing an
# array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

# Each buckets[i] then is responsible for keeping track of how many times
# we've seen `i` in the input set of data as we iterate through it.
# Once we know exactly how many times each piece of data in the input set
# showed up, we can construct a sorted set of the input data from the
# buckets.

# What is the time and space complexity of the counting sort algorithm?
# '''
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr

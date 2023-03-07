# You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. 
# Write a function to search this element in the given input array/list using 'Binary Search'. 
# Return the index of the element in the input array/list. 
# If the element is not present in the array/list, then return -1.

# Input format :
# The first line contains an Integer 'N', which denotes the size of the array/list.
# The second line contains 'N' single space-separated integers representing the elements in the array/list.
# The third line contains the value of X to be searched for in the array/list.

from typing import *

def binarySearch(arr : List[int], n : int, x : int) :
    #Your code goes here
    beg = 0
    end = n-1
    mid = (beg+end)//2
    while beg < end and arr[mid] != x:
        if arr[mid] > x:
            end = mid - 1
        else:
            beg = mid +1
        mid = (beg+end)//2
    
    if arr[mid] == x:
        return mid
    else:
        return -1
    
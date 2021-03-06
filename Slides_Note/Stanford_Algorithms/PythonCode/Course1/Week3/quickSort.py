# -*- coding: utf-8 -*-
"""
@author: HYJ
"""

## In-place Quick Sort
# 就是相当于一直翻转，最后一个即为当前的最大值
def partition(array):
    arrayLen = len(array)
    pivotIndex = 0
    storeIndex = 0
    pivot = array[pivotIndex:pivotIndex+1]
    for i in range(storeIndex+1, arrayLen):
        if array[i] < array[pivotIndex]:
            storeIndex += 1
            array[i], array[storeIndex] = array[storeIndex], array[i]
    array[storeIndex], array[pivotIndex] = array[pivotIndex], array[storeIndex]
    lo = array[:storeIndex]
    hi = array[storeIndex+1:]
    return lo, hi, pivot

def quickSort(array):
    sortedArray = []
    arrayLen = len(array)
    if arrayLen <= 1:
        return array
    if arrayLen == 2:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    lo, hi, pivot = partition(array)
    #print(lo)
    #print(hi)
    lo = quickSort(lo)
    hi = quickSort(hi)
    sortedArray = lo
    sortedArray.extend(pivot)
    sortedArray.extend(hi)
    return sortedArray

originArray = eval(input('Input array: '))

sortedArray = quickSort(originArray)

print('Sorted array is {}'.format(sortedArray))
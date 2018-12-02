import math

def GetBestPrice(units, prices):
    max = 0
    maxIndex = -1
    for index in range(len(units)):
        composition = units[index] * prices[index]
        if (composition > max):
            max = composition
            maxIndex = index
    return prices[maxIndex]


def MultiplyLists(arr1, arr2):
    return [a*b for a, b in zip(arr1, arr2)]

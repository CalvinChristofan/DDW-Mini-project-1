import random


def gen_random_int(number: int, seed: int) -> list[int]:
    result = None
    random.seed(seed)
    result = list(range(number))
    random.shuffle(result)
    return result


def create_string(array: list[int]) -> str:
    output = ""
    for i in range(len(array)):
        output += str(array[i])
        if i < len(array) - 1:
            output += ", "
    output += "."
    return output



def my_sort(array):
    n = len(array)
    for i in range(1, n):                        
        for j in range(1, n):                    
            first_number = array[j-1]
            second_number = array[j]
            if first_number > second_number:     
                array[j-1], array[j] = array[j], array[j-1]
    return array 


#quicksort

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
 
 
def _quicksort(array, low, high):
    if low < high:
        p = _partition(array, low, high)
        _quicksort(array, low, p - 1)
        _quicksort(array, p + 1, high)
 
 
def _partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

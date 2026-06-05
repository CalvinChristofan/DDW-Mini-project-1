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

numbers_in_words = {
    "zero": 0,
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9, 
    "ten": 10,
    "eleven": 11, 
    "twelve": 12, 
    "thirteen": 13, 
    "fourteen": 14, 
    "fifteen": 15, 
    "sixteen": 16, 
    "seventeen": 17, 
    "eighteen": 18, 
    "nineteen": 19,
    "twenty": 20, 
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 100 * 10,
    "million": (100*10)**2,
    "billion": ((100*10)**3),
    "trillion": ((100*10)**4),
}

segments = [ 'thousand', 'million', 'billion', 'trillion']


multipliers = segments + ['hundred']


def get_word_nested_list_segments(word:str):
    word = word.replace('-', ' ').lower()
    word_arr = word.split(' ')
    nested_list: list[list[int]] = []
    item_list = []
    length = len(word_arr)

    def append_to_temp_item(item):
        if numbers_in_words.get(item, None):
            item_list.append(item)

    for i in range(length):
        word = word_arr[i]
        is_last = i == length-1
        append_to_temp_item(word)
        if word in segments or is_last:
            nested_list.append(item_list)
            item_list = []
    return nested_list 


def conquer(list_item:list[str]):
    num = 0
    for word in list_item:
        num_value = numbers_in_words.get(word)
        if(num_value):
            if word in multipliers :
                if num > 0:
                    num *= num_value 
                else: 
                    num = num_value
            else:
                num += num_value
    return num


def divide_list(nested_list:list[list[str]]):
    n = len(nested_list)
    if n == 1:
        return conquer(nested_list[n-1])
    mid = n//2

    return divide_list(nested_list[0:mid]) \
        + divide_list(nested_list[mid:n])
    

def convert_words_to_numbers(word:str):
    nested_list = get_word_nested_list_segments(word)
    return divide_list(nested_list) 


def normalize_result(numbers:int):
    str_value = str(numbers)
    n = len(str_value)
    if n > 3:
        quotient = n//3
        _list = []

        for i in range(1, quotient+1):
            j = i * 3 * -1
            k = j + 3
            if k == 0:
                _list.append(str_value[j:])
            else:
                _list.append(str_value[j:k])
            if i == quotient and j*-1 != n:
                _list.append(str_value[:j])


        return ','.join(_list[i] 
                for i in range(len(_list)-1, -1, -1))
    return str_value


if __name__ == "__main__":
    word = input("Enter value in words: ")
    numbers = convert_words_to_numbers(word)
    result = normalize_result(numbers)
    print(result)
    



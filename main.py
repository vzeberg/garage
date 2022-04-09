def find_second_index(symbol, sequence):
    i = 0
    for index, element in enumerate(sequence):
        if element == symbol:
            i += 1
        if i == 2:
            return index


print(find_second_index('b', 'bob'))

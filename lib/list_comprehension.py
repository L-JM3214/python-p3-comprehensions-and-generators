#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)

def make_exclamation(sentence_list):
    new_list = [word + '!' for word in sentence_list]
    return new_list

result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)

    
    
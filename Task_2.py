from typing import Callable
import re

def generator_numbers(text: str):
    '''Generates all numbers from text, separated by spaces'''
    pattern = re.compile(r'(?<=\s)[+-]?\d+(?:\.\d+)?(?=\s)')
    matches = pattern.findall(f' {text} ')
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    '''Returns the sum of all numbers in a text using the func generator.'''
    result = 0
    for n in func(text):
        result += n
    return result
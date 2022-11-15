'''
Created on 9 Nov 2022 at 5:29 pm

@author: Prital Bamnodkar
'''

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def get_recurring_fractions(n):
    '''
    In:
        n: int

    Out:
        a list of tuples of n and 1/n. only tuples with 1/n being a recurring fraction are considered.
    '''
    out = []
    recurring_fract_len = len(str(1/3))

    for i in range(2, n):
        fract = 1/i
        if len(str(fract)) >= recurring_fract_len:
            out.append((i, fract))

    return out

def test_get_recurring_fractions():
    n = 10
    res = get_recurring_fractions(n)
    print(*res, sep='\n')

# returns a list of slices of str. the slices will be of the specified size.
def split_into_parts(inStr, size):
    out = []
    str_len = len(inStr)
    start_index = 0
    end_index = 0

    while end_index <= str_len:
        end_index = start_index + size

        out.append(inStr[start_index : end_index])
        start_index = end_index

    return out

# check if all elements in a list are identical. all elements must be str or lists
def are_same(ls):
    if ls == [] or len(ls) == 1:
        return True
    
    first_elem = ls[0]
    last_elem = ls[-1]

    for elem in ls[:-1]:
        if elem != first_elem:
            return False
    
    if len(first_elem) > len(last_elem):
        return first_elem[:len(last_elem)] == last_elem
    else:
        return first_elem == last_elem

def find_recurring_part(fract):
    for size in range(1, len(fract)):
        parts = split_into_parts(fract, size)
        found = are_same(parts)

        if found:
            return parts[0]
    return None

def get_recurring_part(fract):
    iterable = fract[:]
    out = ''
    non_recurring_part = ''

    while len(iterable) > 1:
        temp = find_recurring_part(iterable)

        if temp == None:
            non_recurring_part += iterable[0]
            iterable = iterable[1:]
        else:
            out = temp
            break
    return (non_recurring_part, out)


def format_fract(fract):
    '''
    IN:
        fract: a float
        a fraction in decimal form

    Out:
        a string of the properly formatted fraction
        e.g. 0.3333333333 -> 0.(3)
             0.1666666666 -> 0.1(6)
    '''
    fract_parts = get_recurring_part(fract)
    return f'{fract_parts[0]}({fract_parts[1]})'

def test_get_recurring_part():
    n = 3
    print(get_recurring_part(1/n))

def test_split_into_parts():
    size = 4
    s = 'abcdefghij'
    print(split_into_parts(s, size))

def test_get_recurring_part():
    s = '123456'
    print(get_recurring_part(s))

def test_format_fraction():
    fract = '0.67121212121212'
    print(format_fact(fract))

if __name__ == '__main__':
    fract = '0.13333333333'

    print(format_fract(fract))
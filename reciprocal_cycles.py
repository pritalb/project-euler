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

def test_get_recurring_cycles():
    n = 10
    res = get_recurring_fractions(n)
    print(*res, sep='\n')

if __name__ == '__main__':
    test_get_recurring_cycles()
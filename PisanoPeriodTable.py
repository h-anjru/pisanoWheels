#!/usr/bin/env python
""" Pisano period.
"""

__author__ = 'Andrew Rowles'
__email__ = 'andrew@rowles.io'

import numpy as np

# The list length of the Fibonacci Sequence
FIB_LIM = 15000
MODULO = list(range(1598,10000))
#MODULO = 3

def F():
    """ Generate sequence of Fibonacci numbers.
    """
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

def fibonacci_modulo(lim=FIB_LIM, mod=MODULO):
    """ Generate sequence of Fibonacci numbers modulo mod.
    Parameters
    ----------
    lim: integer
        The number of Fibonacci numbers to generate.
    mod: integer
        The modulo.
    Return a list of the Fibonacci numbers modulo.
    """
    fibs = []
    fib_seq = F()
    for n in range(lim):
        fibs.append(next(fib_seq) % mod)
    return fibs

def find_period(l):
    """ Finds the period of list of numbers.
    Parameters
    ----------
    l: integer[]
        The sequence of numbers.
    Return
    ------
    steps: integer
        The period.
    Returns None, if no period is found.
    """
    steps = 1
    for i in range(1, len(l)):
        if l[i] == l[0]:
            if l[:i] == l[i:i+i]:
                return steps
        steps += 1
    return None


def pisano_period(mod=MODULO, lim=FIB_LIM, console=False):
    """ Calculate the Pisano period.
    Parameters
    ----------
    mod: integer
        ...
    lim: integer
        ...
    """
    # Sequence of Fibonacci numbers modulo mod
    mod_fibs = fibonacci_modulo(mod=mod, lim=lim)

    # Find the Pisano period
    period = find_period(mod_fibs)

    if console and period:
        print('Pisano Period modulo %s' % mod)
        print('Period Length: %s' % find_period(mod_fibs))
        s = mod_fibs[:period]
        string = ' '.join(str(e) for e in s)
        string = string.replace(' 0 ','\n0 ')
        #print(string)
        print('---')
        
        # Nateloop
        focus = mod/2
        for ii in range(0,len(s)):
            if s[ii] > focus:
                s[ii] = mod-s[ii]
        string = ' '.join(str(e) for e in s)
        string = string.replace(' 0 ','\n0 ')
        #print(string)

        # pie chart of Nateloop
        # generate slices
        per = find_period(mod_fibs)
        ratio = 100 / per

        s_flip = [-e+max(s) for e in s]
        # convert Pisano period to grayscale hex values
        s0 = [hex(round(255 * e/max(s_flip))) for e in s] # stretch range to 0-255
        s0 = [e.replace('0x','') for e in s0] # remove 0x from beginning
        for ii in range(0,len(s0)):
            if len(s0[ii]) == 1:
                s0[ii] = '0' + s0[ii]
        s0 = ['#'+e*3 for e in s0]

        zeroes = s.count(0)
    return mod,find_period(mod_fibs),zeroes

    
def main():
    chart = []
    for ii in range(min(MODULO),max(MODULO)+1):
        [m,p,z] = pisano_period(ii,FIB_LIM,True)
        chart.append([m,p,z])
    return chart

table = main()

np.savetxt('table_'+str(min(MODULO)+1)+'_'+str(max(MODULO)+1)+'.csv',table,delimiter=',')
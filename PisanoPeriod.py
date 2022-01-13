#!/usr/bin/env python
""" Pisano period.
"""

__author__ = 'Andrew Rowles'
__email__ = 'andrew@rowles.io'

import matplotlib.pyplot as plt

# The list length of the Fibonacci Sequence
FIB_LIM =20000
#MODULO = list(range(999,1598))
MODULO = [25, 25, 50, 75, 125, 200, 325, 525, 850, 1375, 2225, 3600, 5825, 9425, 15250, 24675, 39925, 64600, 104525, 169125, 273650, 442775, 716425, 1159200, 1875625, 3034825, 4910450, 7945275, 12855725, 20801000, 33656725, 54457725, 88114450, 142572175, 230686625, 373258800, 603945425, 977204225]

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
        # count zeroes for classification
        zeroes = s.count(0)
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

        # pie chart of the Grimes number
        # generate slices
        per = find_period(mod_fibs)
        ratio = 100 / per
        slice = [ratio] * per
        # flip values to so that 0=white, max = black
        s = [-e+max(s) for e in s]
        # convert Pisano period to grayscale hex values
        s0 = [hex(round(255 * e/max(s))) for e in s] # stretch range to 0-255
        s0 = [e.replace('0x','') for e in s0] # remove 0x from beginning
        for ii in range(0,len(s0)):
            if len(s0[ii]) == 1:
                s0[ii] = '0' + s0[ii]
        s0 = ['#'+e*3 for e in s0]
        # plot and save
        plt.pie(slice,explode=None,labels=None,colors=s0,
                startangle=360/(2*per)-90,counterclock=False,radius=1.618,
                wedgeprops={'linewidth':0,'edgecolor':'white'})
        plt.axis('equal')
        plt.axis([-2,2,-2,2])
        plt.annotate('Pisano period, modulo %s' % mod,
                     xy=(-2,-1.83),fontsize=5)
        plt.annotate('Period length = %s' % per,
                     xy=(-2,-1.89),fontsize=5)
        plt.annotate(string,xy=(-2,-1.49),fontsize=5)
        # save in different folders based on class
        plt.savefig('test2//fibwheel'+str(mod)+'.png',dpi=600, 
                    bbox_inches='tight')
        plt.close()
    return None

    
def main():
    [pisano_period(m,FIB_LIM,True) for m in MODULO]


main()
from webbrowser import get
import numpy as np
import math as m
import sys

class Factors:
    class Left: 
        x0_ = 0
        x1 = 0
        x2 = 0
    class Right:
        x0 = 0
        x1 = 0
        x2 = 0
    
def get_factors(s, f):
    i = 0
    while (i < len(s)):
        if ('X' in s[i]):
            print(s[i][2:])
            if (s[i][2:] > '2'):
                print("Degree Too high")
            print(s[i])
        i += 1

def get_factors_dic(s, dic):
    i = 0
    neg = 1
    reverse = 1
    while (i < len(s)):
        if ('=' in s[i]):
            reverse = -1
        if ('X' in s[i]):
            if (i - 3 >= 0 and s[i - 3] == '-'):
                neg = -1
            if (s[i] in dic):
                dic[s[i]] = float(s[i - 2]) * neg * reverse + float(dic[s[i]])
            else:
                dic[s[i]] = float(s[i - 2]) * neg * reverse
            print(dic[s[i]])
            neg = 1
        i += 1

def main():
    dic = {}
    f = Factors
    string = ' '.join(sys.argv[1:])
    print(string)
    tab = string.split('=')
    left = tab[0]
    right = tab[1]
    left = left.split(' ')[:-1]
    right = right.split(' ')[1:]
    print(left)
    print(right)

    s = string.split(' ')

    get_factors_dic(s, dic)

    # get_factors(left, f.Left)
    # get_factors(right, f.Left)


main ()

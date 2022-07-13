from webbrowser import get
import numpy as np
import math as m
import sys

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
    string = ' '.join(sys.argv[1:])
    print(string)
    s = string.split(' ')

    get_factors_dic(s, dic)


main ()

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
            if (int(s[i][2:]) in dic):
                dic[int(s[i][2:])] = float(s[i - 2]) * neg * reverse + float(dic[int(s[i][2:])])
            else:
                dic[int(s[i][2:])] = float(s[i - 2]) * neg * reverse
            neg = 1
        i += 1

def show_form(dic):
    # dic = sorted(dic)
    # for key in dic:
    #     if (float(key) > 2 and dic[key] != 0):
    #         print("Degree is too high")
    #     print(str(key) + " " + str(dic[key]))

    sorted_dic = sorted(dic)
    for key in sorted_dic:
        print("Key : " + str(key) + "   Value : " + str(dic[key]))
        print ("Polynomial degree: " + str(key))
        if (key > 2 and dic[key] != 0):
            print("The polynomial degree is strictly greater than 2, I can't solve.")

    # for key in sorted(dic):
    #     print("Key : " + str(key) + "   Value : " + str(dic[key]))


def main():
    dic = {}
    string = ' '.join(sys.argv[1:])
    print(string)
    s = string.split(' ')

    get_factors_dic(s, dic)

    show_form(dic)
    

main ()

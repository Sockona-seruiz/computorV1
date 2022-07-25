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
    delta = 0
    sorted_dic = sorted(dic)
    deg = 0
    for key in sorted_dic:
        # print("Key : " + str(key) + "   Value : " + str(dic[key]))
        if (key > deg and dic[key] != 0):
            deg = key
    print ("Polynomial degree: " + str(deg))
    if (deg > 2):
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return ()
    # ax2 + b2 + c = 0
    #delta = b2 - 4ac
    delta = dic[1]**2 - (4 * dic[2] * dic[0])
    sqdelta = m.sqrt(abs(delta))
    # print("delta = " + str(delta) + " sqrt(delta) = " + str(sqdelta))

    if (deg == 2):
        if (delta > 0):
            print("Discriminant is strictly positive, the two solutions are:")
            x1 = (-dic[1] - sqdelta) / (2 * dic[2])
            x2 = (-dic[1] + sqdelta) / (2 * dic[2])
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
        elif (delta == 0):
            print("Discriminant is equal to 0, the solution is:")
            x0 = (-dic[1]) / (2 * dic[2])
            print("x0 = " + str(x0))
        else:
            print("Discriminant is strictly negative, the two complexe solutions are:")
            x1_l = (-dic[1] / (2 * dic[2]))
            x1_r = sqdelta / (2 * dic[2])
            print("x1 = " + str(x1_l) + " + i * " + str(x1_r))
            print("x2 = " + str(x1_l) + " - i * " + str(x1_r))
            #x1 = (-b - i * sqrt(delta)) / (2 * a)
            #x2 = (-b + i * sqrt(delta)) / (2 * a)


def main():
    dic = {}
    dic[0] = 0
    dic[1] = 0
    dic[2] = 0
    string = ' '.join(sys.argv[1:])
    print(string)
    s = string.split(' ')

    get_factors_dic(s, dic)

    show_form(dic)
    
main ()

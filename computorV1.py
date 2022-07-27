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
            if ("." in s[i][2:]):
                print ("Error : non whole coefficient")
                return (-1)
            elif (int(s[i][2:]) in dic):
                dic[int(s[i][2:])] = float(s[i - 2]) * neg * reverse + float(dic[int(s[i][2:])])
            else:
                dic[int(s[i][2:])] = float(s[i - 2]) * neg * reverse
            neg = 1
        i += 1
    return (1)

def show_form(dic):
    delta = 0
    sorted_dic = sorted(dic)
    deg = 0
    r_form = ""
    for key in sorted_dic:
        # print("Key : " + str(key) + "   Value : " + str(dic[key]))
        if (key > deg and dic[key] != 0):
            deg = key
        if (dic[key] > 0):
            r_form += " + " + str(dic[key]) + " * X^" + str(key) + " "
        elif (dic[key] < 0):
            r_form += " - " + str(dic[key])[1:] + " * X^" + str(key) + " "
    if (r_form.startswith(" + ")):
        r_form = r_form[3:]
    elif (r_form == ""):
        r_form = "0 "
    print ("Reduced form : " + r_form + "= 0" + "\n")
    print ("Polynomial degree: " + str(deg) + "\n")
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
    elif (deg == 1):
        print ("The solution is:")
        print ("x = " + str(-dic[0] / dic[1]))
    else:
        if (dic[0] != 0):
            print ("The equation has no solution")
        else:
            print ("Each real number is a solution")


def main():
    dic = {}
    dic[0] = 0
    dic[1] = 0
    dic[2] = 0
    string = ' '.join(sys.argv[1:])
    # print(string)
    s = string.split(' ')

    if (get_factors_dic(s, dic) == -1):
        return

    show_form(dic)
    
main ()

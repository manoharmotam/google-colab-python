#!/usr/bin/env python3

def middle3(str):
    middle = int(len(str)/2)
    mid = str[middle]
    mid = str[middle - 1] + mid + str[middle + 1]
    print(mid)

str = input("Enter your String here: ")

middle3(str)

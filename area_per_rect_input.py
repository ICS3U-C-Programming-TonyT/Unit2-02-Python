#!/usr/bin/env python3

# Created by: Tony Tran
# Created on: September. 25, 2023
# This program does Area and Perimeter using User Input

l = float(input("Length: "))
w = float(input("Width: "))
A = format(l * w)
P = format((2 * l) + (2 * w))
print(f"Area [{A} = {l} * {w}] ")
print(f"Perimeter [{P} = 2*{l} + 2*{w}]")

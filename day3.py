import numpy as np
import functools
input = []

with open('inputs/day3.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

def largest_value_in_intstr(intstr):
    largest = 1
    current_loc = 0
    largest_loc = 0
    for intager in intstr:
        if int(intager) > largest:
            largest = int(intager)
            largest_loc = current_loc
        current_loc += 1
    if largest == 1:
        largest_loc = intstr.rfind('1')
    return largest, largest_loc

def maximum_joltage(intstr_list):
    joltage = 0
    for intstr in intstr_list:
        largest1, largest_loc1 = largest_value_in_intstr(intstr)
        if largest1 == 1:
            joltage += 11
        elif largest_loc1 == len(intstr) -1:
            largest2, _ = largest_value_in_intstr(intstr[:-1])
            joltage += largest2 * 10 + largest1
        else:
            largest2, _ = largest_value_in_intstr(intstr[largest_loc1+1:])
            joltage += largest1 * 10 + largest2
    return joltage

print(maximum_joltage(input))

# WORKS FOR EXAMPLE CASES BUT NOT FOR INPUT
def maximum_joltage_override(intstr_list,num_batteries=12):
    joltage = 0
    power_list = [10**i for i in range(num_batteries-1,-1,-1)]
    for intstr in intstr_list:
        twelve_largest = []
        current_loc = 0
        for _ in range(num_batteries):
            largest, largest_loc = largest_value_in_intstr(intstr)
            twelve_largest.append((largest_loc + current_loc, largest))
            if largest == 1:
                intstr = intstr[:largest_loc] +'0'+ intstr[largest_loc+1:]
            elif len(intstr.replace('0','')) - largest_loc > num_batteries - len(twelve_largest):
                intstr = intstr[largest_loc+1:]
                current_loc += largest_loc + 1
            else: 
                intstr = intstr[:largest_loc] +'0'+ intstr[largest_loc+1:]
        twelve_largest.sort()
        joltage += sum([a[1]*b for a,b in zip(twelve_largest, power_list)])
    return joltage

# WORKS FOR INPUT
def maximum_joltage_override_working(intstr_list, num_batteries=12):
    joltage = 0
    for intstr in intstr_list:
        max_joltage = 0
        cutoff = 0
        for x in range(num_batteries, 0, -1):
            window = intstr[cutoff:len(intstr)-x+1]
            largest = max(int(intchar) for intchar in window)
            cutoff += window.index(str(largest)) + 1
            max_joltage = 10 * max_joltage + largest
        joltage += max_joltage
    return joltage

print(maximum_joltage_override_working(input))
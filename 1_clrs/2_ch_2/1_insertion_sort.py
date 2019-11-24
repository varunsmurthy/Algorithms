# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:07:11 2015

@author: Varun
"""

import random
import time

def insertion_sort(ip_list):
    ip_length = len(ip_list)
    for j in range(1,ip_length):
        i = j-1
        while i>=0 and ip_list[i] > ip_list[i+1]:
            temp = ip_list[i]
            ip_list[i] = ip_list[i+1]
            ip_list[i+1] = temp
            i = i-1
    return ip_list

def main():
    ip_list = []
    for i in range(1,10000):
        ip_list.append(random.randint(0,999999))
    correct_list = sorted(ip_list)
    start_time = time.time()
    sorted_list = insertion_sort(ip_list)
    end_time = time.time()
    if sorted_list == correct_list:
        print("Succesful! Time = %f" %(end_time - start_time))
    

if __name__ == "__main__":
    main()
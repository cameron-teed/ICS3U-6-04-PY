#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Dec 2019
# This program uses an array

import random

def d_array(collum, row):
    
    array = []
    average = 0
    
    for counter in range(0, row): 
        temp_collum = []
        
        for counter1 in range(0, collum):
            temp_collum.append(random.randint(0, 50+1))
            
        array.append(temp_collum)
        print ("{}".format(temp_collum), end="")
        print("")
        
    for row_value in array:
        for single_element in row_value:
            average += single_element
   
    return average


def main():
    # this function uses an array

    collum = int(input("Please enter how many collums you would like: "))
    row = int(input("Please enter how many rows you would like: "))
    print("")
    
    average = d_array(collum, row)
    
    average = average/(row*collum)
    
    print("")
    print (average) 
 


if __name__ == "__main__":
    main()

#!/usr/biin/env python3
#Include Numpy
import numpy as np
def main(): 
	
	i = 0     #declare an integer i, set to 0
	x = 119.0	#declare a float x, with val 119
	
	for i in range(120):	#loops i from 0 to 119
		if((i%2)==0):
			x += 3.  	#same as x=x+3
		else: x -= 5. 	#x=x-5
	
	s="%3.2e" % x	#quotes for string, % for format, 3 integers, 2 after the decimal, e for scientific notation all for x
	print(s)

#now the rest of the program continues
if __name__ == "__main__":	#if the main function exists, run it
	main()
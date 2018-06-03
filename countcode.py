#!/usr/bin/env python

import os
import sys
from tabulate import tabulate

if __name__ == '__main__':
	base_dir = ""
	try:
		base_dir = str(sys.argv[1])
		extensions = [str(ext) if ext[0] == "." else "."+ext for ext in sys.argv[2:]]
		print base_dir
		if len(extensions) == 0:
			print "Checking " + str(len(extensions)) + " extensions:", extensions
		else:
			print "Checking all extensions"
	except:
		print "Please provide a valid directory and a list of file extensions as the argument to this script"
		print "If no file extensions are provided, we'll count everything."
		exit()

	count = {}
	lines = {}

	for root, _, files in os.walk(base_dir):
	    for file in files:
	    	__, ext = os.path.splitext(file)
	    	if ext in extensions or len(extensions) == 0:
	    		with open(os.path.join(root, file), 'r') as infile:
	    			for i, l in enumerate(infile):
	    				pass
	    		if ext not in count:
	    			count[ext] = 1
	    			lines[ext] = i
	    		else:
		    		count[ext] += 1
		    		lines[ext] += i

	data = []
	for ext in count:
		data.append([ext, count[ext], lines[ext]])
	data.sort(key=lambda x: x[2], reverse=True)
	print tabulate(data, headers=["Extension", "# files", "# lines"], tablefmt='orgtbl')
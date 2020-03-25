#! /usr/bin/python

import sys, re

if (len(sys.argv) != 3):
	print("Usage: append_declarations INPUT_FILE OUTPUT_FILE [INDENTATION]")
	print("Default indentation is 1.")
	sys.exit()
try:
	indentAmount = int(sys.argv[3])
except:
	indentAmount = 1

file = open(sys.argv[1], "r")
inputFile = file.read()
file.close()
declarations = re.findall("(?<!;\n\n)(?<=\n\n).+\)", inputFile)
print(declarations)
file = open(sys.argv[2], "a")
for dec in declarations:
	type, tab, name  = dec.partition("\t")
	if not dec.startswith("int\tmain"):
		file.write(type + tab * indentAmount + name + ";\n\n")
file.close()
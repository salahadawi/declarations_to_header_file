#! /usr/bin/python

import sys, re

if (len(sys.argv) < 3):
	print("Usage: append_declarations INPUT_FILE OUTPUT_FILE [INDENTATION]")
	print("Default indentation is 1.")
	sys.exit()
try:
	indentAmount = int(sys.argv[3])
except:
	indentAmount = 1

try:
	file = open(sys.argv[1], "r")
except:
	print("Input file not found.")
	sys.exit()
inputFile = file.read()
file.close()
declarations = re.findall("[^\t\n]+\t.+\)", inputFile)
try:
	file = open(sys.argv[2], "a")
except:
	print("Output file not found.")
	sys.exit()
for dec in declarations:
	type, tab, name  = dec.partition("\t")
	if not dec.startswith("int\tmain"):
		file.write("\n" + type + tab * indentAmount + name + ";\n")
file.close()
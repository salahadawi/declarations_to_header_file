#! /usr/bin/python

import sys, re

# Check if there are enough arguments
if (len(sys.argv) < 3):
	print("Usage: append_declarations INPUT_FILE OUTPUT_FILE [INDENTATION]")
	print("Default indentation is 1.")
	sys.exit()

#Check if there is a third argument for indentation size
try:
	indentAmount = int(sys.argv[3])
except:
	indentAmount = 1

# Open file specified in first argument, if it fails return an error
try:
	file = open(sys.argv[1], "r")
except:
	print("Input file not found.")
	sys.exit()

# Read and save input file to string
inputFile = file.read()
file.close()

# Find all declarations in input file
declarations = re.findall("[^\t\n]+\t.+\)", inputFile)

# Open file specified in second argument, if it fails return an error
try:
	file = open(sys.argv[2], "r+")
except:
	print("Output file not found.")
	sys.exit()

# Read and save input file to string upto but not including #endif statement
outputFile = ""
for line in file:
	if line.startswith("#endif"):
		file.seek(-len(line) - 1, 1)
		break
	outputFile += line

# Find all prototypes that already exist in output file to avoid duplicates
existingPrototypes = re.findall("[^\t\n]+\t.+\)", outputFile)

# Find all new declarations and write them to output file as prototypes
# int main is excluded
for dec in declarations:
	if dec not in existingPrototypes:
		type, tab, name  = dec.partition("\t")
		if not dec.startswith("int\tmain("):
			file.write("\n" + type + tab * indentAmount + name + ";\n")

# Write #endif statement after all prototypes
file.write("\n#endif")

file.close()
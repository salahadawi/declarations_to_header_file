#! /usr/bin/python3

import sys, re
# Check if there are enough arguments
if (len(sys.argv) < 3):
	print("Usage: ./add_prototypes INPUT_FILE OUTPUT_FILE [INDENTATION]")
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
filePos = 0
for line in file:
	if line.startswith("#endif"):
		file.seek(filePos - 1, 0)
		break
	outputFile += line
	filePos += len(line)

# Find all prototypes that already exist in output file to avoid duplicates
existingPrototypes = re.findall("\t[^\t]+\)", outputFile)

# Find all new declarations and write them to output file as prototypes
# int main is excluded
addedPrototypesAmount = 0
for dec in declarations:
	if re.search('\t[^\t]+\)', dec).group() not in existingPrototypes:
		returnType, tab, name  = dec.partition("\t")
		if not "\tmain(" in dec:
			prototype = re.search('[^\t].+(?=\()', name).group()
			file.write("\n" + returnType + tab * indentAmount + name + ";\n")
			# Print each added prototype
			print("%s\t%-30s%s" % (returnType, prototype, "\t"), end="")
			print("--prototype added with indentation ", end="")
			print(str(indentAmount) + ".")
			addedPrototypesAmount += 1

# Write #endif statement after all prototypes
file.write("\n#endif")
file.close()

# Print info once script is complete
if addedPrototypesAmount:
	print("Success! " + str(addedPrototypesAmount), end="")
	if addedPrototypesAmount > 1:
		print(" prototypes have been added.")
	else:
		print(" prototype have been added.")
else:
	print("No prototypes have been added.")
	print(str(len(existingPrototypes)) + " declarations were found ", end=""),
	print("which already exist in " + sys.argv[2] + ".")

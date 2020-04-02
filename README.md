# Add prototypes automatically to header file.
This script can be used to automatically get each function declaration from a specified source file, and add it's respective function prototype to a specified header file.

Prototypes already existing in the output file are not added to avoid duplicates.
## Usage
```
./add_prototypes.py INPUT_FILE OUTPUT_FILE [INDENTATION]
```
Indentation changes the amount of tabs between prototype return type and function name.

Default indentation is 1.

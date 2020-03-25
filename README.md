# Append prototypes to header file.
This script can be used to automatically get each function declaration from a specified source file, and append it's respective function prototype to a specied header file.
## Usage
```
./append_prototypes INPUT_FILE OUTPUT_FILE [INDENTATION]
```
Indentation changes the amount of tabs between prototype return type and function name.

Default indentation is 1.

## To fix
If the source file does not comform to the Norm, the script might not detect all declarations

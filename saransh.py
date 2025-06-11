"""for i in range(5):
    if i==3:
        pass
    else:
        print(i)

# break statement - allows you to exit the loop early even if the condition is till true. This is useful when you want to stop the loop based on specific condition during the execution

i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i+= 1"""

# while statement - while loop in python repeatedly executes a block of code as long as the given condition is true
i = 1
while i<6:
    print(i)
    i+= 1


# file handling - refers to the process of creating opening , reading, writing, appending and closing files using programming. It enables programmes to store output and read input from files.
# why file handling is imp - it allows  data to be stored permanently
# configuration management, report generation, data import and export

# FILE OPERATIONS review

# Opening a file (open()): returns a file project
# Reading from a file: read(),readline(),or readlines().
# Writing to a file : write()or writelines()
# Appending content: a mode appends to existing files
# Closing a file: close()method or with context manager

# TEXT VS BINARY FILES
# text files stores the data in human readable form . Example- .txt, .csv,.xml,.json

# binary files - the data is which is stored in binary numbers LIKE 0 and 1 . eXAMPLE - .pdf , .jpg , .mp3
# This requires b mode ( eg - "rb" , "wb")      reading and writing
 
# MODE DESCRIPTION
'r' Read (default)

# MODE DESCRIPTION
'w'Write (overwrites)
'a' Append
'b' Binary
'x' Create a new File
'+' Read and write




FileType = {"txt":"Text File","doc":"Word Document","xls":"Excel","ppt":"powerpoint","pdf":"Portable Document Format","py":"Python"}
#I've declared the possible types of extensions, acting like a library of sorts for the program to choose from.
FileName = input("Enter your file name: ")
#Input to be accepted from the user
x = FileName.split(".")
#Makes the input split so that x reads it seperately with one dot
print("The extension name of your file is detected as ",FileType[x[-1]])
#Returns the last element through a negative input which ensures we don't need to explicitly find the length of the iterable before using it.

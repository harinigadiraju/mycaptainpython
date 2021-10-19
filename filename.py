filename = input("Enter file name: ")
ext = filename.split(".",-1)
print("the extension of the file is : " + repr(ext[-1]))

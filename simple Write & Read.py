file = open("test.txt", "w")
file.write("Test")
file.write("\n")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

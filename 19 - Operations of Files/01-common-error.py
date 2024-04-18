# # Normally used senario
file = open ("try.txt", "r")
t = file.read()
print(t)
file.close()

# will give error because file is not readable
file = open ("try.txt", "w")
# t = file.read() # io.UnsupportedOperation: not readable
t = file.write("")
print(t)
file.close()
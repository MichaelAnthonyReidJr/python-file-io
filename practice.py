
# file_object = open('dummy.txt', 'r')
# readFile = file_object.read()
# print(readFile)
# print(type(file_object))
# file_object.close()

# new_file = open('Reid_Family', 'w')
# new_file.write("Michael, Lilia, Aaron, ")
# new_file.close()

with open('Reid_Family', 'a') as new_file:
    new_file.write("Gabriella, Jaden, Achilles, Angelica")


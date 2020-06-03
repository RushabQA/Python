new_file = open("new_file.txt", "r")
lines = new_file.readline()
new_file.close()

new_file = open("new_file.txt", "w")
new_file.write(lines)
new_file.close()




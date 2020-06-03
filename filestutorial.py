filename = open("filename.txt", "r")

outfile = ""

for line in range(10):
    if line % 2 == 0:
        outfile += filename.readline()
    else:
        filename.readline()

filename = open("filename.txt", "w")
filename.write(outfile)
filename.close()
teams = open("teams.txt", "r")

outfile = ""
variable = "this is a new line"

for line in range(6):
    if line == 1:
        print (variable)
    else:
        teams.readlines()

teams = open("teams.txt", "w")
teams.write(outfile + variable)
teams.close()
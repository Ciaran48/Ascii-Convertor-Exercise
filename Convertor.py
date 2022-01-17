#gets the file that will be converted
readFile = open("Ascii file.txt", "r")

#saves the converted file here
writeFile = open("Ascii vals.txt", "w")

#End of file(EOF) is false lets the programme start
EOF = False

#while the file has not ended making it loop 
while not EOF :

    #readstheline
    line = readFile.readline()

    #Sets EOF to true if applicable
    if line == "": EOF = True
    
    #replaces the commas with spaces
    line = line.replace(","," ")

    #splits the sequence of digits from the commas creating a list named ascii
    line = line.split()

    #turns the strings into int
    thefile = map(int, line)

    #Chooses the character
    for char in thefile:

            #output is created
            conversion=str(unichr (char))
            if conversion == "#":
                conversion = " "

            #makes it print contiously
            print conversion,

            #writes the file
            writeFile.write(conversion)

text_file = open('working_with_files_text',"r")

content = text_file.readlines()

for line in range(1,(len(content)+1)):
    if (line%2) == 1:
        print(content[line])





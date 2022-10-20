fp = open("report_json.json", "r")
#reading text line by line
text= fp.readlines()
#searching for character to remove
char = text[2][9]
#removing the character by replacing it with blank
text[1] = text[1].replace(char, "")

#opeing the file in write mode
fw = open("report_json.json", "w") 
#writing lines one by one
for lines in text:
   fw.write(lines)
#closing the file
fw.close()
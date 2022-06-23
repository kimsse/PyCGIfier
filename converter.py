import json
import sys
import os

def user_input():
    respond = ""
    respond = input(respond)
    return respond

def checkFileExtension(origin_file_name):
    origin_file_name = os.path.basename(origin_file_name)

    ext_num = 0
    file_name_num = 0
        
    for i in origin_file_name:
        if (i != "."):
            file_name_num += 1
        else:
            break
    
    file_ext = origin_file_name[file_name_num + 1: len(origin_file_name) + 1]
    return file_ext

# check the completion of config
with open("./config.json", "r") as config_json:
    config_dic = json.load(config_json)
respond = ""

if (config_dic["python-compiler-location"] == "undefined"):
    output = sys.path
    compiler_location = output[4] + "/python.exe"
    print("System has detected your current python compiler: " + compiler_location)
    print("If you want to change another python compiler, enter the compiler\'s location. Otherwise, keep it as a blank")
    respond = ""
    respond = input(respond)
    if (respond == ""):
        config_dic["python-compiler-location"] = compiler_location
    else:
        config_dic["python-compiler-location"] = respond
else:
    pass

print("Currently using compiler: " + config_dic["python-compiler-location"])
print("Please enter the location that your source file.")
print("The source files\'s format are usually HTML, CSS, and JavaScript.")
print("System will try to recognize the file format automatically.")
target_file_location = user_input()
# start progress
target_file_name = os.path.basename(target_file_location) # gather the pure file name with extension
print("Selected file:" + target_file_name)
target_file_extension = checkFileExtension(target_file_name) # gather the file extension
print("File type: " + target_file_extension)

print("Is this that you want? yes or no")
respond = user_input()
if (respond != "yes"):
    print("Please indicate the file extension. If you want to discard this progress, enter cancel.")
    respond = user_input()
    if (respond == "cancel"):
        pass
    else:
        target_file_extension = respond
else:
    pass
# open source file and read
try:
    source_file = open(target_file_location, "r")
except:
    print("Error: Cannot get the source file. Maybe this file or directory is no longer exist.")
    exit()
    
source_file_contents = source_file.readlines()
print(source_file_contents)
source_file.close()

# delete all the TABS
output_source_file_content = []
for i in source_file_contents:
    while (("\t" in i) == True):
        i = i.strip("\t")
    output_source_file_content.append(i)

# create final file
if (target_file_extension == "html" or ".html"):
    pass
elif (target_file_extension == "css" or ".css"):
    pass
elif (target_file_extension == "js" or ".js"):
    pass
else:
    print("Error: Unsupport file extensino!")
    exit()
output_file = open(target_file_name + ".py", "w")

# write content into it
output_file.writelines("#!" + config_dic["python-compiler-location"] + "\n")
output_file.writelines("import cgi\n")
output_file.writelines("import cgitb\n")

if ((target_file_extension == "html" or ".html") == True):
    output_file.writelines("print(\"Content-type: text/html\")\n")
elif ((target_file_extension == "css" or ".css") == True):
    output_file.writelines("print(\"Content-type: text/css\")\n")
elif ((target_file_extension == "js" or ".js") == True):
    output_file.writelines("print(\"Content-type: text/js\")\n")

output_file.writelines("# converted source code\n")
output_file.writelines("print(\"\"\"\n")
for i in output_source_file_content:
    output_file.writelines(i + "\n")
output_file.writelines("\"\"\")\n")
output_file.close()
print("Progress done! Check your new py file in the same directory.")
exit()
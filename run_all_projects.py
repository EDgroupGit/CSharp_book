import os
import shutil
import subprocess
import re

directories_to_check = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22"] # Which directory do you want to start with?
excluded_directory = ["02", "20"]

def run(directory, fw):
    
      print(directory)
      for fname in os.listdir(directory):
            if fname.endswith('.csproj'):
                try:
                    # output = subprocess.check_output(f'dotnet run', shell=True, timeout=15)
                    output = subprocess.check_output('dotnet run', timeout=5, universal_newlines=True, encoding="utf8",  errors="ignore")
                    fw.write(f'{directory} \n') 
                    str_output = output
                    print(str_output)
                    #str_output = re.sub(r"\r\r\n", "\n", str_output)
                    fw.write(str_output)
                
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
                    fw.write(f'{directory} \n') 
                    # str_output = e.output.decode('cp949', errors='ignore')
                    str_output = e.output
                    str_output = str_output.replace('\r\r\n', '\n')
                    fw.write(str_output)
                
                fw.flush()

                # fw.write('\n')
                break
            else:
                  pass
      # if os.path.exists("*.csproj"):
            
directories = []
# Get all the subdirectories of directory_to_check recursively and store them in a list:
for directory in directories_to_check:
    directories.extend([os.path.abspath(x[0]) for x in os.walk(directory)])

#directories.remove(os.path.abspath(directories_to_check)) # If you don't want your main directory included

with open("this_is_output.txt", "w+", encoding='utf-8') as fw:                
    for i in directories:
        if os.path.exists(i):
            os.chdir(i)     # Change working Directory
            run(i, fw)      # Run your function
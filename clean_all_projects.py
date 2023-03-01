import os
import shutil

directory_to_check = "." # Which directory do you want to start with?

def cleanup(directory):
      print(directory)
      for fname in os.listdir(directory):
            if fname.endswith('.csproj'):

                  command = "dotnet clean"
                  os.system(command) #The command can also be passed as a string, instead of a variable
                  
                  path = directory + "\\bin"
                  if os.path.exists(path):
                        shutil.rmtree(path)
                        path = directory + "\\obj"
                        shutil.rmtree(path) 

                  break
            else:
                  pass
      # if os.path.exists("*.csproj"):
            
# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included

for i in directories:
      if os.path.exists(i):
            os.chdir(i)         # Change working Directory
            cleanup(i)      # Run your function

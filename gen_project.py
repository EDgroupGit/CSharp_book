import os

csproj_content = """<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net5.0</TargetFramework>
  </PropertyGroup>

</Project>
"""

# listup directories 02~19
for top_level in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 22]:
    top_dir = "{:02d}".format(top_level)
    #print(top_dir)

    project_dirs = os.listdir(top_dir)

    for project_dir in project_dirs:
        csproj_path = os.path.basename(project_dir) + ".csproj"
     
        # check if there is any C# file.
        #print(os.path.isdir("/home/el"))

        with open(top_dir + "\\" + project_dir + "\\" + csproj_path, 'w') as csproj:
            csproj.write(csproj_content)
#Since OS is a module, it's necessary to import it for it's usage;
import os;

#OS is a module containing the available actions and informations about the operational system.
#Operational System 
#=> Environment (Contains the informations about the sphere that let you act in the OS.)

#"os.environ" is a property which works like a dictionary and contains the information about the OS environment.
environment = os.environ
""" print(f"This desktop remains to {environment.get("USERNAME")}!"); """

#WORKING WITH DIRECTORIES 💡

#"os.getcwd" (Get Current Working Directory) is a function which returns the path where the terminal runs the code.
""" print(os.getcwd()) """

#"os.chdir" (Change Directory) is a function which changes the CWD (Current Working Directory).
#os.chdir(r"C:\Users\guga6\OneDrive\Documentos\studies\python-course\reviews");
""" print(os.getcwd()) """

#"os.mkdir" (Make Directory) is a function which creates a directory into a specific path.
""" os.mkdir("TEST"); """
#"os.mkdir" + "s" (Make Directories) is function which allows you to create more than one directory at once by passing a continous path.

#"os.listdir" (List Directory) is a function which returns a list containing the files names inside a directory.
""" print(os.listdir()); """

#"os.rmdir" (Remove Directory) is a function which removes a directory. By the way, only empty directories can be removed.
""" os.rmdir("TEST"); """

#WORKING WITH FILES 💡

#"os.startfile" is a function which starts/open a file.
#os.chdir(r"C:\Users\guga6\Downloads");
""" os.startfile("cyber-security.pdf"); """

#"os.rename" is a function which renames a file.
#os.chdir(r"C:\Users\guga6\Downloads");
""" os.rename("cyber-security.pdf", "cyber-security-roadmap.pdf");"""

#"os.remove" is a function which removes a file.

#"os.walk" is a function which returns a LIST containing ROOT, DIRECTORIES & FILES until a certain destiny directory.
""" walk_until_cwd = os.walk(os.getcwd());
for root, dirs, files in walk_until_cwd :
  print(dirs); """
#The code above follows a certain path printing all the files names containing in each step of the walk.💡

#WORKING WITH PAHTS (OS.PATH) 💡
#"os.path" is the OS module's SUBMODULE which allows us to work with PATHS in the OS envionment.

#"os.path.basename" is a function which returns the base name ("CORE NAME") of the CWD (Current Working Directory).
""" cwd = os.getcwd();
print(os.path.basename(cwd)); """

#"os.path.commonpath" is a function which returns a path which is common part in the comparation between more than one path.
#path_one = os.getcwd() + r"\challenges\file-manager";
""" path_two = os.getcwd()

print(path_one + "\n" + path_two);
print("The common path, in this situation, is: " + os.path.commonpath([path_one, path_two])) """

#"os.path.commonprefix" is a function that works like the "os.path.commonpath", but this function treats the path like a literal string. Then, the common path reffers to what is common between the strings!

#path_one = os.getcwd() + r"\knowing-os-module\test-1";
#path_two = os.getcwd() + r"\knowing-os-module\test-2";

""" print(path_one + "\n" + path_two);
print("The common path, in this situation, is: " + os.path.commonpath([path_one, path_two]))
print("The common prefix, in this situation, is: " + os.path.commonprefix([path_one, path_two])) """

#"os.path.dirname" is a function which returns the path until the CWD's parent directory (Like "os.getcwd() - 1");
""" print(os.getcwd())
print(os.path.dirname(os.getcwd())); """

#"os.path.join" is a function for constructing a path by passing some informations which may compose the path.
""" drive = input("Insert the computer drive for the search: ");
user = input("Insert the computer user for the search: ");
filename = input("Insert the file name for the opening: "); """

#searching_path = os.path.join(drive,r'\Users',user,'Downloads')
""" os.chdir(searching_path);
os.startfile(filename); """

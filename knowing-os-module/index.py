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
walk_until_cwd = os.walk(os.getcwd());
for root, dirs, files in walk_until_cwd :
  print(dirs);
#The code above follows a certain path printing all the files names containing in each step of the walk.💡
import os;

""" env = os.environ;
print(env.get("LANG")); """

#Directories
""" os.chdir("C:/Users/guga6/Downloads");
print(os.listdir());

os.mkdir("test-directory");

print(os.listdir());

os.rmdir("test-directory");

print(os.listdir()); """

""" cwd = os.getcwd();
print(cwd); """

#Files
""" os.chdir("C:/Users/guga6/Downloads");
os.system("echo > test.txt");
os.remove("test.txt"); """

""" path = os.getcwd() + "/knowing-os-module";
walk_until_path = os.walk(path);

for root, dirs, files in walk_until_path :
  print(files); """

#Paths
""" cwd = os.getcwd() + "/knowing-os-module/test-1";
path_two = os.getcwd() + "/knowing-os-module/test-2"

print(cwd);
print("\n");
print(path_two);
print("The common path between these paths is: " + os.path.commonpath([cwd, path_two]));
print("The common prefix between these paths is: " + os.path.commonprefix([cwd, path_two])); """

""" cwd = os.getcwd();
parent_path = os.path.dirname(cwd);
print(parent_path); """

""" drive = input("Select the computer drive for the scan: ");
user = os.environ["USERNAME"];
filename = input("Select the file name for the scan: ");

path_for_scan = os.path.join(drive, r"\Users", user, "Downloads");

os.chdir(path_for_scan);

try :
  os.startfile(filename); 
except :
  print("The inserted filename does not math any existent file."); """
#Open a file -> open(file_path, mode) | Comum Opening Modes -> "w"(write) "r"(read) "a"(append)
sample_file = open("files-management-py/file.txt", "a");

#Write in a file -> .write()
sample_file.write(
  "\n" + input("Insert a name for register: ")
  );

#Close a file -> .close()
sample_file.close();
sample_file = open("files-management-py/file.txt", "r");

#Read file lines -> .readLines()
for record in sample_file.readlines() :
  print(record.replace("\n", ""));

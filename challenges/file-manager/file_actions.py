def openFile(file_path, opening_mode) :
  try :
    return open(file_path, opening_mode);
  except:
    print("Error while trying to find the file.");
  return None;

def writeIntoFile(file_path, content) :
  target_file = openFile(file_path, "a");
  if target_file == None : return False;

  try :
    target_file.write("\n" + str(content));
  except :
    print("\n⚠ Invalid content.");
    return False;
    

  target_file.close();
  return True;
def showFileContent(file_path) :
  target_file = openFile(file_path, "r");
  if target_file == None : return False;

  for content_line in target_file.readlines() :
    print(content_line);
  print("+--------------------------+");

  target_file.close();
  return True;

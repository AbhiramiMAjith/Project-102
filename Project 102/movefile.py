import os
import shutil

from_dir = "C:/Users/Abhirami M Ajith/Downloads"
to_dir = "C:/Users/Abhirami M Ajith/Downloads"
listOfFiles = os.listdir(from_dir)

for i in listOfFiles:
    name, ext = os.path.splitext(i)
    if (ext == ''):
        continue
    if(ext in [".pdf",'.txt',".doc",".docx"]):
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "document_files"
        path3 = to_dir + "/document_files/" + i

        if (os.path.exists(path2)):
            print("Moving "+ i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving "+ i)
            shutil.move(path1, path3)
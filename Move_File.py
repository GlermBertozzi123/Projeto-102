import os
import shutil

from_dir = "C:/Users/glerm/OneDrive/Área de Trabalho/PASTA/from_dir"
to_dir = "C:/Users/glerm/OneDrive/Área de Trabalho/GameCode/Projeto 102/to_dir"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name,extension = os.path.splitext(filename)
    if extension == "":
        continue
    if extension in[".txt",".pdf",".doc",".docx",".png",".jpg",".jpeg"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "arquivo_documento"
        path3 = to_dir + "/" + "arquivo_documento" + "/" + filename
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
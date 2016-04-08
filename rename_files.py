import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Python34\Programs py\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Python34\Programs py\prank")
    
    #(2) for each of the file, rename filename
    for file_name in file_list:
        print("old name - " + file_name)
        print("new name - " + file_name.lstrip("0123456789"))
        os.rename(file_name,file_name.lstrip("0123456789")) 
    os.chdir(saved_path)   
  
        
rename_files()

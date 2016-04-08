import os

def rename_files.():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\DPAUL\Desktop\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\DPAUL\Desktop\prank")
    
    #(2) for each of the file, rename filename
    for file_name in file_list:

        print("old name - " + file_name)
        os.rename(file_name, file_name.translate(None,'0123456789'))
        os.chdir(saved_path)
        print("new name - " + file_name.translate(None,'0123456789'))
        
        
  
        
rename_files.()

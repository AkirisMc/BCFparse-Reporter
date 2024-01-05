"""
This module contains functions for opening, reading and creating text files.  
It also contains the functions for printing the section (Summary numbers) of the input file and for creating
the output subfolder. 
All the functions from OS module are imported.
All the module functions are exported to argumentsfunctions.py and mainfunction.py
"""

import os 

def opening_file(inputfile):
    """Opens a text file and reads it line by line.
    Returns the file content.
    
    input_f -- the input file that will be processed (str)"""

    cwd = os.getcwd()
    file = cwd + "/" + inputfile 
    fr = open(file, "r")
    lines = fr.readlines()
    fr.close()
    return lines

def printing_sn(inputfile):
    """Prints the Summary numbers of a text file on the command line.
    
    input_f -- the input file that will be processed (str)"""

    cwd = os.getcwd()
    file = cwd + "/" + inputfile 
    fr = open(file, "r")
    lines = fr.readlines()
    fr.close()
    for line in lines:
        if(line.startswith("# SN") or line.startswith("SN")):
            print(line)

def creating_subdir(arg_name, output_dir):
    """Creates a subfolder with the selected argument name inside of the output directory.
    Returns the path that will be used for storing the rest of the files.
    
    arg_name -- the name of the selected argument (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    cwd = os.getcwd()
    par_dir = os.path.dirname(cwd)
    given_path = os.path.join(par_dir, output_dir)

    if(given_path == cwd):
        path = os.path.join(given_path, arg_name) 
        os.mkdir(path)
        return path
    else:
        os.chdir(given_path)
        path = os.path.join(given_path, arg_name)
        os.mkdir(path)
        return path

def creating_textfile(path, lines, file_txt, arg_name):
    """Creates a new text file with the requested section of the input file.
    
    path -- the parent directory path (str)
    lines -- the file content (str)
    file_txt -- the argument name with a .txt extension (str)
    arg_name -- the selected argument name (str)"""

    cleaned_txt_file = path + "/" + file_txt
    fw = open(cleaned_txt_file, 'w')
    
    for line in lines:
        if(line.startswith("# " + arg_name) or line.startswith(arg_name)):
            fw.write(line)
    fw.close()
    
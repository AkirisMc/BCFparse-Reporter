"""
This module contains functions for creating texts files and plots for each section of 
the input file. 
All the functions from filesfunctions.py and plotsfunctions are imported.
All the module functions are exported to mainfunction.py
"""

from filesfunctions import *
from plotsfunctions import *

def tstv_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument TSTV
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""
  
    arg_name = "TSTV"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_scatterplot(path, file_txt, file_png)
 
def sis_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument SiS
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "SiS"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_piechart(path, file_txt, file_png)

def af_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument AF
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "AF"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_barchart(path, file_txt, file_png)
 
def qual_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument QUAL
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "QUAL"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_lineplot(path, file_txt, file_png)

def idd_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument IDD
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "IDD"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_barchart2(path, file_txt, file_png)

def st_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument ST
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "ST"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_barchart3(path, file_txt, file_png)

def dp_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument DP
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "DP"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_lineplot2(path, file_txt, file_png)

def psc_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument PSC
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "PSC"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_scatterplot2(path, file_txt, file_png)

def psi_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument PSI
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "PSI"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_scatterplot3(path, file_txt, file_png)

def hwe_function(input_f, output_dir):
    """Creates a text file and a plot when the optional argument HWE
    is selected.
    
    input_f -- the input file that will be processed (str)
    output_dir -- the selected directory where the outputs will be stored (str)"""

    arg_name = "HWE"
    file_txt = arg_name + ".txt"
    file_png = arg_name + ".png"
    print("you have selected the section:", arg_name)
    lines = opening_file(input_f)
    path = creating_subdir(arg_name, output_dir)
    creating_textfile(path, lines, file_txt, arg_name)
    creating_barchart4(path, file_txt, file_png)



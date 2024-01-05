"""
This script contains the main function which is the entry point of the program.
All the functions from filesfunctions.py, plotsfunctions.py and argumentsfunctions.py modules are imported.
All the functions from argparse module are imported as well as the method arg from ast module. 
"""

import argparse
from ast import arg
from filesfunctions import *
from plotsfunctions import *
from argumentsfunctions import *

def main():
    """
    The main function contains all the steps that the program follows in order to parse and process the input
    file and generate the results inside of a new subfolder located inside of the chosen output directory.  
    """
    # adding description of the script
    parser = argparse.ArgumentParser(description="""This script receives a .vchk file and generates text files \
        and plots of specific sections of the file""")

    # adding compulsory arguments 
    # input file
    parser.add_argument("input_f", metavar="input_file", type=str, help="Vchk file")
    # output directory
    parser.add_argument("output_dir", metavar="output_directory", type=str, help="The directory where output files are stored")

    # adding optional arguments 
    parser.add_argument("-tstv", action="store_true", help="Transitions/Transversions")
    parser.add_argument("-sis", action="store_true", help="Singleton stats")
    parser.add_argument("-af", action="store_true", help="Stats by non-reference allele frequency")
    parser.add_argument("-qual", action="store_true", help="Stats by quality")
    parser.add_argument("-idd", action="store_true", help="InDel distribution")
    parser.add_argument("-st", action="store_true", help="Substitution types")
    parser.add_argument("-dp", action="store_true", help="Depth distribution")
    parser.add_argument("-psc", action="store_true", help="Per-sample counts")
    parser.add_argument("-psi", action="store_true", help="Per-sample Indels")
    parser.add_argument("-hwe", action="store_true", help="Hardy Weinberg equilibrium")
    parser.add_argument("-all", action="store_true", help="Process all sections")

    # extracting the arguments from the argparse object
    args = parser.parse_args() 
    # storing the arguments in new variables
    input_f = args.input_f
    output_dir = args.output_dir

    # printing the summary numbers on the command line
    printing_sn(input_f)

    # using if conditionals statements to generate the results depending on the selected optional argument/s
    if args.tstv:
        tstv_function(input_f, output_dir)
    if args.sis:
        sis_function(input_f, output_dir)
    if args.af:
        af_function(input_f, output_dir)
    if args.qual:
        qual_function(input_f, output_dir)
    if args.idd:
        idd_function(input_f, output_dir)
    if args.st:
        st_function(input_f, output_dir)
    if args.dp:
        dp_function(input_f, output_dir)
    if args.psc:
        psc_function(input_f, output_dir)
    if args.psi:
        psi_function(input_f, output_dir)
    if args.hwe:
        hwe_function(input_f, output_dir)
    if args.all:
        tstv_function(input_f, output_dir)
        sis_function(input_f, output_dir)
        af_function(input_f, output_dir)
        qual_function(input_f, output_dir)
        idd_function(input_f, output_dir)
        st_function(input_f, output_dir)
        dp_function(input_f, output_dir)
        psc_function(input_f, output_dir)
        psi_function(input_f, output_dir)
        hwe_function(input_f, output_dir)
        print("you have selected all the sections")
    
if(__name__ == "__main__"):
    main()




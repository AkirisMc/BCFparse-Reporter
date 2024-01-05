"""
This module contains the functions for generating different types of plots according to the 
selected argument/s.
All the functions from matplotlib.pyplot library and pandas module are imported.
All the module functions are exported to argumentsfunctions.py and mainfunction.py
"""
import pandas as pd
import matplotlib.pyplot as plt

def creating_scatterplot(path, file_txt, file_png):
    """Creates a scatter plot opening and reading the TSTV text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = ['ts/tv', 'ts/tv (1st ALT)']
    values = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            values.append(float(lin_split[4]))
            values.append(float(lin_split[7]))
    
    plt.style.use('seaborn-paper')
    plt.scatter(names, values, linewidths = 0.5)
    plt.title("Transitions/Transversions by sample")
    plt.tight_layout()
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_piechart(path, file_txt, file_png):
    """Creates a pie chart opening and reading the SiS text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = ['allele count',	'number of SNPs',	'number of transitions',	'number of transversions', \
        	'number of indels',	'repeat-consistent',	'repeat-inconsistent',	'not applicable']
    values = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            for i in range(2, len(lin_split)):
                values.append(float(lin_split[i]))
    
    plt.style.use('seaborn-paper')
    plt.pie(values, autopct='%1.01f%%', startangle=90)
    plt.title("Singleton stats")
    plt.legend(names, bbox_to_anchor=(-0.21,0.0), loc="lower left")
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_barchart(path, file_txt, file_png):
    """Creates a bar chart opening and reading the AF text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    data = dict()

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            data[lin_split[2]] = float(lin_split[3]) 
        
        names = list(data.keys())
        values = list(data.values())

    plt.style.use('seaborn-paper')    
    plt.barh(names, values)
    plt.title("Stats by non-reference allele frequency")
    plt.xlabel("frequency")
    plt.ylabel("alleles")
    plt.tight_layout()
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_lineplot(path, file_txt, file_png):
    """Creates a line plot opening and reading the QUAL text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = []
    values = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            names.append(lin_split[2])
            values.append(float(lin_split[3]))
    
    plt.style.use('seaborn-paper')
    plt.plot(names[20:35], values[20:35], color='#5a7d9a', linewidth=1.5)
    plt.title("Stats by quality (samples 23-37)")
    plt.xlabel("sample id")
    plt.ylabel("quality")
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_barchart2(path, file_txt, file_png):
    """Creates a bar chart opening and reading the IDD text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    namesdel = []
    valuesdel = []
    namesin = []
    valuesin = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            if(int(lin_split[2]) < 0):
                namesdel.append(lin_split[2])
                valuesdel.append(float(lin_split[3]))
            else:
                namesin.append(lin_split[2])
                valuesin.append(float(lin_split[3]))

    plt.style.use('seaborn-paper')
    plt.bar(namesdel[50:60], valuesdel[50:60], label='deletions', width=1)
    plt.bar(namesin[0:10], valuesin[0:10], label='insertions', width=1)
    plt.title("InDel distribution (samples -10:10)")
    plt.xlabel("length (deletions negative)")
    plt.ylabel("count")
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_barchart3(path, file_txt, file_png):
    """Creates a bar chart opening and reading the ST text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = []
    values = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            names.append(lin_split[2])
            values.append(float(lin_split[3]))
    
    plt.style.use('seaborn-paper')
    plt.bar(names, values)
    plt.title("Substitution types")
    plt.xlabel("type")
    plt.ylabel("count")
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_lineplot2(path, file_txt, file_png):
    """Creates a line plot opening and reading the DP text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    bins = []
    fraq_gen = []
    fraq_sites = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            bins.append(lin_split[2])
            fraq_gen.append(float(lin_split[4]))
            fraq_sites.append(float(lin_split[6]))
    
    plt.style.use('seaborn-paper')
    plt.plot(bins[0:21], fraq_gen[0:21], 'b^-', label='fraction of genotypes(%)')
    plt.plot(bins[0:21], fraq_sites[0:21], 'go-', label='fraction of sites(%)' )
    plt.title("Depth distribution (samples 0-20)")
    plt.xlabel("bins")
    plt.ylabel("percentages")
    plt.legend()
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_scatterplot2(path, file_txt, file_png):
    """Creates a scatter plot opening and reading the PSC text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = []
    transitions = []
    transversions = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            names.append(lin_split[2])
            transitions.append(float(lin_split[6]))
            transversions.append(float(lin_split[7]))
    
    plt.style.use('seaborn-paper')
    plt.scatter(names, transitions, linewidths = 0.5, label='number of Transitions')
    plt.scatter(names, transversions, linewidths = 0.5, label='number of Transversions')
    plt.title("Per-sample counts")
    plt.xlabel("samples")
    plt.ylabel("counts")
    plt.legend()
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_scatterplot3(path, file_txt, file_png):
    """Creates a scatter plot opening and reading the PSI text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    names = []
    nhets = []
    naa = []

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            names.append(lin_split[2])
            nhets.append(float(lin_split[7]))
            naa.append(float(lin_split[8]))
    
    plt.style.use('seaborn-paper')
    plt.scatter(names, nhets, linewidths = 0.5, label='nhets')
    plt.scatter(names, naa, linewidths = 0.5, label='naa')
    plt.title("Per-Sample Indels")
    plt.xlabel("samples")
    plt.ylabel("counts")
    plt.legend(bbox_to_anchor=(-0.019,0.0))
    plt.savefig(path + '/' + file_png)
    plt.close()

def creating_barchart4(path, file_txt, file_png):
    """Creates a barchart opening and reading the HWE text file and stores the result 
    in the selected subfolder.
    
    path -- the parent directory path (str)
    file_txt -- the argument name with a .txt extension (str)
    file_png -- the argument name with a .png extension (str)"""

    txtfile_path = path + "/" + file_txt
    fr = open(txtfile_path, "r")
    data = dict()

    for line in fr:
        if(not(line.startswith("#"))):
            lin = line.strip("\n")
            lin_split = lin.split("\t")
            data[lin_split[2]] = float(lin_split[3]) 
        
        names = list(data.keys())
        values = list(data.values())

    plt.style.use('seaborn-paper')    
    plt.barh(names, values)
    plt.title("Hardy Weinberg equilibrium 1st ALT allele frequency")
    plt.xlabel("frequency")
    plt.ylabel("alleles")
    plt.tight_layout()
    plt.savefig(path + '/' + file_png)
    plt.close()



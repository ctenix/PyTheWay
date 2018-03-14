import re, csv, os 
import pandas as pd
import numpy as np


columnnames =["PT","AU","DE", "AF","TI","SO","LA","DT","ID","AB","C1","RP","EM","CR","NR","TC","U1","PU","PI","PA","SN","EI","JI","PD","PY","VL","IS","BP","EP","DI","PG","WC","SC","GA","UT"]

#To convert Web of Science files to list of list of dictionary
def convertWOScsv(filename):
    #open file
    openfile = open(filename)
    sampledata = openfile.read()
    sampledata = sampledata
    # separate each article record - note: each article is separated by two line breaks
    individualrecords = sampledata.split('\n\n')
    databaseofWOS = []
    # parse individual record
    for recordindividual in individualrecords:
        onefile = {}
        for x in columnnames:
            #perform regex to divide tag and label
            everyrow = re.compile("\n"+x + " " + r'((.*?))\n[A-Z][A-Z1]', re.DOTALL)
            rowsdivision = everyrow.search(recordindividual)
            #If tag exists add to the file
            if rowsdivision:
                onefile[x] = rowsdivision.group(1)
        databaseofWOS.append(onefile)
    return databaseofWOS

    #To convert Web of Science files in bulk to dataframe
def massconvertWOS():
    publicationslist = []
    #Converts all text files in the same directory to one dataframe
    for file in os.listdir():
        if file.endswith(".txt"):
            converttotable = convertWOScsv(file)
            publicationslist += converttotable
    return pd.DataFrame(publicationslist)

    #To convert dataframe back to Web of Science files for processing in other programs
def convertWOStext(dataframe, outputtext):
    txtresult = ""
    for y in range(0, len(dataframe)):
        for x in columnnames:
            if dataframe[x].iloc[y] != np.nan:
                txtresult += x + " " + str(dataframe[x].iloc[y]) + "\n"
        txtresult += "ER\n\n"
    f = open(outputtext, "w", encoding='utf-8')
    f.write(txtresult)
    f.close()
#Convert files to dataframe
df = massconvertWOS()
df.dropna(how="all", inplace=True)
df.head(1)
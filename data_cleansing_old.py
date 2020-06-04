import os
import pandas as pd
import csv


rootdir = ("C:\\Users\\elisk\\Desktop\\Data\\CHMU\\chmu-process-script\\outputs\\unzips")

for subdir, dirs, files in os.walk(rootdir):
    for entry in files:
        if entry.endswith('C2POHSTT_SCE_N.csv'):
            filePath = os.path.join(subdir, entry)
            with open(filePath, 'r', encoding="cp1250") as fn:
                lines = fn.readlines
                print(lines)
                #for line in lines:
                   # print(line)
                



"""             filePath = os.path.join(subdir, entry)
            with open(filePath, 'r', encoding="cp1250") as fn:
                lines = [line.rstrip('\n') for line in fn]
                listAll = [list(g) for k, g in groupby(lines, key=bool) if k]
                print(listAll)
               # for i in listAll:
                    #print(i) """
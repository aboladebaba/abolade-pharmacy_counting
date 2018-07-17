#!/usr/bin/env python

import sys
import csv

def pharmacy_counting(filename, outpufile):
    
    """
    Reads a given file and extracts drug name, number 
    of unique prescribers and total cost of each dispensed.
    
    Parameters
    ----------
    filename : string (required)
        Text file to extract data from
    outputfile : string (required)
        Text file to store the results of this processing.
        
    Returns
    -------
    results.txt : file
        file containing the result of the extraction
    
    """
    meds = {}
    with open(filename, 'r') as fh:
        reader = csv.reader(fh)
        next(reader, None) # skip the header row
        
        for row in reader:
            if len(row) == 5:
                temp = meds.get(row[3], [[], []])
                temp[0].append(row[0]) # ID
                temp[1].append(float(row[4]))
                meds[row[3]] = temp
    # agg the counts
    results = []
    for key, val in meds.items():
        drug_name = key
        num_prescriber = len(set(val[0]))
        total_cost = sum(val[1])
        temp = drug_name, num_prescriber, total_cost
        results.append(temp)
        
    sorted_results = sorted(results, key=lambda elem: elem[2], reverse=True)
    
    fh.close()
    
    # write out the file
    textfile = open(outpufile, 'w')
    textfile.write('drug_name,num_prescriber,total_cost'+'\n')
    for item in sorted_results:
        temp = item[0]+','+repr(item[1])+','+repr(item[2])+'\n'
        textfile.write(temp)
        
if __name__ == "__main__":
    
    pharmacy_counting(sys.argv[1], sys.argv[2])

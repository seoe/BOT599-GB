# =============================================================== #
# 2017 Spring BOT 599 
# by Eugene Seo
# Code Description: Merge sub feature files into one table.
# =============================================================== #

import sys
import pickle

def write(output, filenames):
    with open ('features.txt', 'rb') as fp:
        f = open("features.txt", 'rb')
        features = "gene_id\t" + f.read() + "\n"
        print(features)
        
    with open(output, 'w') as outfile:
        outfile.write(features)
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                    
def merge():
    batch_num = int(sys.argv[1])
    pos_filenames = []
    neg_filenames = []
    for i in range(1,batch_num+1):
        pos_filenames.append("GetFeatures/pos."+str(i)+".features.txt")
        neg_filenames.append("GetFeatures/neg."+str(i)+".features.txt")
    write('MakeFinalFeatureTables/pos.features.txt', pos_filenames)
    write('MakeFinalFeatureTables/neg.features.txt', neg_filenames)
    
def main():  
    merge()
                    
if __name__ == "__main__":
    main()
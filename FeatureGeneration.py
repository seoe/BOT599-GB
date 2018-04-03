# =============================================================== #
# 2017 Spring BOT 599 
# by Eugene Seo
# Code Description: Generate features from each sub fasta files.
# =============================================================== #

import sys
import numpy
import csv
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
import FastaFileSplitter as ffs
import pickle

def pattern_count(my_seq, pattern):
    abs_num = my_seq.count(pattern)
    ratio = float(abs_num * 100) / len(my_seq)
    return ratio

def main():
    task_id = sys.argv[1]
    labels = ["pos", "neg"]

    # load seqeunces from each sub fa file
    for label in labels:
        input_filename = "SplitFasta/"+label+"."+task_id+".fa"
        samples, sample_num = ffs.count_seq(input_filename, label)
        
        #features_label = features = ["A", "T", "G", "C"]
        
        features = ["TTT", "TCT", "TAT", "TGT",
                    "TTC", "TCC", "TAC", "TGC",
                    "TTA", "TCA", "TAA", "TGA",
                    "TTG", "TCG", "TAG", "TGG",
                    "CTT", "CCT", "CAT", "CGT",
                    "CTC", "CCC", "CAC", "CGC",
                    "CTA", "CCA", "CAA", "CGA",
                    "CTG", "CCG", "CAG", "CGG",
                    "ATT", "ACT", "AAT", "AGT",
                    "ATC", "ACC", "AAC", "AGC",
                    "ATA", "ACA", "AAA", "AGA",
                    "ATG", "ACG", "AAG", "AGG",
                    "GTT", "GCT", "GAT", "GGT",
                    "GTC", "GCC", "GAC", "GGC",
                    "GTA", "GCA", "GAA", "GGA",
                    "GTG", "GCG", "GAG", "GGG"] # DNA codons
        
        features = features + ["TCTCC", "TG"] # Exon
        features = features + ["AG", "GC", "CG"] # 5 UTR
        features = features + ["GT", "TAAC", "TA", "AT", "AATAAA"] # 3 UTR
        features = features + ["CTAAC", "CTAAT", "CTGAC", "CTGAT"] # additional 3 UTR      
        features = features + ["TATA", "CAAT", "CCAAT", "GC", "TTTATAAA"] # Promoter
        
        features_label = features + ["GC-content"]      
        
        if int(task_id) == 1:
            outfile = open("features.txt", 'wb')
            outfile.write("\t".join(features_label))
            outfile.close()

        feature_num = len(features)
        feature_data = numpy.zeros((sample_num, feature_num+2)).astype(object)

        for i in range(0, sample_num):
            feature_data[i][0] = label+str(i)
            sequence = ''.join(samples[i])
            my_seq = Seq(sequence, IUPAC.unambiguous_dna)
            for j in range(0, feature_num):
                pattern = features[j]
                pattern_freq = pattern_count(my_seq, pattern)
                feature_data[i][j+1] = pattern_freq
            feature_data[i][j+2] = GC(my_seq)
        output_filename = "GetFeatures/"+label+"."+task_id+".features.txt"
        with open(output_filename, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            [writer.writerow(r) for r in feature_data]

if __name__ == "__main__":
    main()
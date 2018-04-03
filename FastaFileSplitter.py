# =============================================================== #
# 2017 Spring BOT 599 
# by Eugene Seo
# Code Description: Seperate Fasta file of class 1 and 2 into sub files of them.
# =============================================================== #

import sys

def count_seq(filename, label):
    input_filename = filename    
    header_line = ""
    seq_line = ""
    sequences = []
    lines = []
    count = 0
    header_write = False
    with open(input_filename,"r") as input:       
        for line in input:
            if not line.strip():
                continue
            if(">" in line):
                lines = []
                header_line = line
                lines.append(header_line)
                count = count + 1
                header_write = False
            else:
                if "unavailable" not in line:
                    seq_line = line
                    lines.append(seq_line)
                    if header_write is not True:
                        sequences.append(lines)
                        header_write = True
                else:
                    count = count - 1
    return sequences, count

def divide_num(total_seq_num, batch_num):
    batch_seq_num = total_seq_num/batch_num
    remain = total_seq_num % batch_num
    batch_size = []
    for i in range(0, batch_num):
        if remain > 0:
            batch_size.append(batch_seq_num+1)
            remain = remain - 1
        else:
            batch_size.append(batch_seq_num)
    print("batch size:", batch_size)
    return batch_size

def split_file(batch_size, label, sequences):
    batch_num = len(batch_size)
    pre_num = 0
    line_num = 0
    for i in range(0,batch_num):
        output_filename = "SplitFasta/"+label+"."+str(i+1)+".fa"
        output = open(output_filename,"wb")
        for j in range(0,batch_size[i]):
            idx = j+pre_num            
            line_num += len(sequences[idx])
            for k in range(0, min(len(sequences[idx]),4)): 
                output.write(sequences[idx][k])
        pre_num = pre_num + batch_size[i]        
        output.close()
    #print("total line_num", line_num)
    #print("total seq num", sum(batch_size))
    #print("mean line_num", line_num/sum(batch_size))
        
def main():
    batch_num = int(sys.argv[1])
    filenames = ["pos.fa", "neg.fa"]
    labels = ["pos", "neg"]    
    
    class_sequences = []
    class_sequences_num = []
    for i in range(2):
        sequences, seq_num = count_seq("OrigSeqs/"+filenames[i], labels[i])
        print(labels[i], "seq num:", seq_num) 
        class_sequences.append(sequences)
        class_sequences_num.append(seq_num)
    min_sequence_num = min(class_sequences_num)
    batch_size = divide_num(min_sequence_num, batch_num)        
    for i in range(2):
        split_file(batch_size, labels[i], class_sequences[i])        

if __name__ == "__main__":
    main()
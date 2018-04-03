2017 Spring BOT 599 Project Codes

Name: Eugene Seo

[ Dataset ]
Dataset: Cow genes and Human genes
Class 1 - Exon
Class 2 - Flank-upstream

[ File Description ]
1. FastaFileSplitter.py - Fasta File Splitter Script
2. FeatureGeneration.py - Feature Generation Script
3. FeatureTableCollector.py - Feature Table Collector Script

[*** Run Process ***] 
1. ./split.sh 
   : split original fasta files into sub files. (It runs for both pos and neg classes at once.)
2. ./submit.sh 
   : generate features from sub files. (you can run 'clean.sh' before running 'submit.sh' to clear the data previously generated from different features)
3. ./check.sh
   : check the pipeline process to be done.
4. ./merge.sh 
   : merge sub feafure files into one table. (It runs for both pos and neg classes at once.)
5. ./call_quick_svm.sh 
   : check the accuracy of classification from the SVM classifier. (It will take about 70s to get the result with all features I use.)

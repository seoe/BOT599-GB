positiveExamples=MakeFinalFeatureTables/pos.features.txt
negativeExamples=MakeFinalFeatureTables/neg.features.txt

Rscript quick_svm.R $positiveExamples $negativeExamples

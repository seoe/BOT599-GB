#!/bin/bash
#$ -S /bin/bash
#$ -N TEST_1_SEO
#$ -cwd
#$ -o errors_TEST_1_SEO.log
#$ -j y
#$ -t 1-5:1

./mytest.sh $SGE_TASK_ID

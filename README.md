# Python script to compile error/mutation types on SiMSen-seq filtered consensus files


## What does this pipeline do?
This pipeline is composed of a series of python scripts that will merge the absolute count of errors per position and coverage per position of number of filtered.cons files, extract the frequency of each type of mutation per sample and save it to a file per sample, merge all mutation types files in a single file and calculate the mean and standard deviation on this mutation types across replicates of the same biological sample.

## What is the input to this pipeline?
Filtered.cons files are the output of running umi_error_correct pipeline with the filter_cons.py script on the resulting consensus files.

## What are the output files?
The output of the complete pipeline is a number of files that include: a merged_errors.xls file, a merged_coverages.xls, one mut_freqs.xls file per original sample, a mutations_types_merged.xls file and a mutation_types_stats_merged.xls file.

## How do I run the pipeline?
The pipeline can be run by running the script "errors_output.py". This script will execute all the steps of the pipeline, but these can also be run separately if needed. The input arguments to the scripts are detailed in the help messages obtained by running the scripts without arguments. 

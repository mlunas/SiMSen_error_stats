# Python course project 
Remote repository for Manuel's 2021 Pyhton course project

# What does this pipeline do?
This pipeline is composed of a series of python scripts that will merge the absolute count of errors per position and coverage per position of number of filtered.cons files, extract the frequency of each type of mutation per sample and save it to a file per sample, merge all mutation types files in a single file and calculate the mean and standard deviation on this mutation types across replicates of the same biological sample.

# What is the input to this pipeline?
Filtered.cons files are the output of running umi_error_correct pipeline with the filter_cons.py script on the resulting consensus files.

# What are the output files?
The output of the complete pipeline is a number of files that include: a merged_errors.xls file, a merged_coverages.xls, one mut_freqs.xls file per original sample, a mutations_types_merged.xls file and a mutation_types_stats_merged.xls file.

# How do I run the pipeline?
The pipeline can be run by running the script "errors_output.py". This script will execute all the steps of the pipeline, but these can also be run separately if needed. The input arguments to the scripts are detailed in the help messages obtained by running the scripts without arguments. 

# Known errors/bugs (to be corrected):

## Excel returns a message stating files may be corrupted, what do I do?
For moment being the output files format is saved as plain text with a .xls termination to trick Excel into recognizing these files to open them. However, you may get this error message when opening, you can just click on "open anyways" and the files will work. Future implementations will solve this by using a different module to save and format the output files.

## Error on terminal: No such file or directory
This error can happen if you don't write correctly the path your input files or to your output folder. Remember that if using this pipeline on windows, you should use ascending diagonal bars (/) instead of the system default descending ones (\\) to separate directories. You may also get this error if you don't create your output directory before executing the pipeline.

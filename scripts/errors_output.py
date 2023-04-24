#!/usr/bin/env python3
import sys
import argparse
import statistics
from merge_coverage import merge_coverage
from merge_errors import merge_errors
from mut_type_freq import mut_type_freq
from merge_mut_type_freqs import merge_mut_type_freqs
from merge_means_mut_type import merge_means_mut_type



def errors_output(infile,outdir):
    #Foolproofing so output directory is passed no matter of whether the diagonal bar is provided in the outdir argument or not: 
    if outdir[-1]=="/":
        pass
    else:
        outdir=str(outdir)+"/" 
         
    merge_coverage(infile,outdir)
    merge_errors(infile,outdir)
    for i in infile:
        mut_type_freq(i,outdir)
    mut_files=[]
    
    for i in infile:
        if "/" in i:
            mut_files.append(outdir+i.split("/")[-1][:-17]+"mut_freqs.xls")
        else:
            mut_files.append(outdir+i[:-17]+"mut_freqs.xls")

    merge_mut_type_freqs(mut_files,outdir)   

    merge_means_mut_type(outdir+"mutation_types_merged.xls",outdir)

if __name__=='__main__':
    def parseArgs():
        parser=argparse.ArgumentParser(description="Run the error type pipeline")
        parser.add_argument('-i','--infile',dest='infile',help='Path to input file(s)',nargs='+',required=True)
        parser.add_argument('-o','--outdir',dest='outdir',help='Output directory', required=False)
        args=parser.parse_args(sys.argv[1:])
        return(args)

    errors_output(parseArgs().infile,parseArgs().outdir)

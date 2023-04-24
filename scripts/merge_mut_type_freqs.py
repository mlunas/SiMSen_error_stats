#!/usr/bin/env python3
import sys
import argparse

def merge_mut_type_freqs(infile,outdir):

    outfilename="mutation_types_merged.xls"
    
    #Assign output directory to either default (infile directory) or provided (in this case also clean up path from output filename):
    if str(outdir)=="None":
        outdir=str()
    
            
    #Foolproofing so output directory is passed no matter of whether the diagonal bar is provided in the outdir argument or not: 
    if outdir[-1]=="/":
        pass
    else:
        outdir=str(outdir)+"/"
 
    # Merge all mutation frequencies files into a single output file: 
    for filename in infile:
        with open(filename) as f, open(outdir+outfilename, 'a') as g:
            for line in f:
                g.write(line)
            g.write('\n')


if __name__=='__main__':
    def parseArgs():
        parser=argparse.ArgumentParser(description="Merge mutation types files")
        parser.add_argument('-i','--infile',dest='infile',help='Path to input file',nargs='+',required=True)
        parser.add_argument('-o','--outdir',dest='outdir',help='Name of the output directory, infile directory by default',required=False)
        args=parser.parse_args(sys.argv[1:])
        return(args)
    
    merge_mut_type_freqs(parseArgs().infile)

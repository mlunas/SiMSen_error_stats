#!/usr/bin/env python3
import sys
import argparse
import statistics

    
def merge_coverage(infile,outdir):
    lines=newlines=name=value=[]
    n,m,fn,sample_name=[-1,1,1,""]
    file=infile[0]
    
    # Fixing the format for the output directory:
    if outdir is None:
        outdir=""
    else:
        if outdir[-1]!="/":
            outdir+="/"

    outfilename= outdir+"merged_coverages.xls"
    
    #Open the first file, extract the header and save the needed values to the first line of the merged file:
    with open(file) as f:
        line1=f.readline()
        parts=line1.split('\t')
        # Clear file paths from the sample names:
        if "/" in file:
            file=file.split("/")[-1]
        # Clear sequencing data file name formatting from sample names:
        name1=file.split("-")[0]
        with open(outfilename, 'w') as g:
            g.write(parts[2]+'\t'+parts[3]+'\t'+parts[4]+'\n')
        for line in f:    
            parts=line.split('\t')            
            with open(outfilename, 'a') as g:    
                g.write(parts[2]+'\t'+parts[3]+'\t'+parts[4]+'\n')    
                
    # For each file, extract the coverage values per position and save them to the output file:              
    for filename in infile:    
        with open(filename) as f:
            if "/" in filename:
                filename=filename.split("/")[-1]
            name2=filename.split("-")[0]
            for line in f:
                if n<0:
                    n+=1
                    if name1==name2:
                        sample_name= str(name2+"_"+str(m))
                        m+=1
                    else:
                        m=1
                        sample_name= str(name2+"_"+str(m))
                        name1=name2    
                        m+=1
                else:
                    n+=1
                    parts=line.split('\t')
                    ref=parts[4]
                    cov=float(parts[12])
                    value.append(cov)
                        
            newlines=[str(sample_name)+'\n']
        
            for i in range(n):
                newlines.append(str(value[i])+'\n')
            
            with open(outfilename) as f:
                lines=f.readlines()
    
            with open(outfilename, 'w') as g:
                for i in range (n+1):
                    g.write(lines[i].rstrip()+'\t'+newlines[i])
        n=-1
        value=[]                
if __name__=='__main__':
    def parseArgs():
        parser=argparse.ArgumentParser(description="Merge error absolute frequencies ")
        parser.add_argument('-i','--infile',dest='infile',help='Path to input file',nargs='+',required=True)
        parser.add_argument('-o','--outdir',dest='outdir',help='Path to the output directory',required=False)
        args=parser.parse_args(sys.argv[1:])
        return(args)

    merge_coverage(parseArgs().infile,parseArgs().outdir)

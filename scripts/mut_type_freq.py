#!/usr/bin/env python3
import sys
import argparse


def mut_type_freq(filename,outdir):
    subs=transt=transv=delt=inst=N=total=subs_freq=transt_freq=transv_freq=delt_freq=inst_freq=N_freq=0
    lines= -1
    
    #Remove formatting characters and file path from filename to keep only sample name:
    outfilename=filename[:-17]+'mut_freqs.xls'
    if "/" in filename:
        samplename=(filename.split("/")[-1])[:-14]
    else:    
        samplename=filename[:-14]
        
    #Assign output directory to either default (infile directory) or provided (in this case also clean up path from output filename):
    if str(outdir)=="None":
        outdir=str()
    else:
        if "/" in outfilename:
            outfilename=outfilename.split("/")[-1]
            
        #Foolproofing so output directory is passed no matter of whether the diagonal bar is provided in the outdir argument or not: 
        if outdir[-1]=="/":
            pass
        else:
            outdir=str(outdir)+"/"
        
    #Open the input and output files, extract the non-consensus reads and calculate Absolute frequency, Relative frequency (proportion), Rate per total number of positions and Cumulative relative   frequency for transitions, transversions, insertions and deletions:
    with open(filename) as f, open(outdir+outfilename, 'w') as g:
        for line in f:
            lines+=1
            parts=line.split('\t')
            if (parts[16].rstrip() not in '') and (parts[16].rstrip() != 'Max Non-ref Allele'):
                total+=1
                ref=parts[4]
                var=parts[16].rstrip()
                mut=ref+'-'+var
                if mut == 'T-C' or mut == 'C-T' or mut == 'A-G' or mut == 'G-A':
                    transt+=1
                    transt_freq+=float(parts[15])
                elif mut == 'T-A' or mut == 'T-G' or mut == 'C-G' or mut == 'C-A' or mut == 'A-T' or mut == 'A-C' or mut == 'G-C'or mut == 'G-T':
                    transv+=1
                    transv_freq+=float(parts[15])
                elif var == 'D':
                    delt+=1
                    delt_freq+=float(parts[15])
                elif var == 'I':
                    inst+=1
                    inst_freq+=float(parts[15])
                elif var == 'N':
                    N+=1
                    N_freq+=float(parts[15])
        
        # Calculate substitutions (transtions + transversions) statistics and write the data to a file in a tab separated table format so it is easily readable in softwares like Excel or LibreOffice:       
        subs=transt+transv
        subs_freq=transt_freq+transv_freq
        g.write(samplename+'\t'+str(total)+" positions with variants in the sample"+'\n')
        g.write("Mutation type	Absolute frequency	Proportion	Rate per total number of positions	Type of mutation cumulative relative frequency"+'\n')
        g.write('Substitutions'+'\t'+str(subs)+'\t'+str(subs/total)+'\t'+str(subs/lines)+'\t'+str(subs_freq)+'\n')
        g.write('Transitions'+'\t'+str(transt)+'\t'+str(transt/total)+'\t'+str(transt/lines)+'\t'+str(transt_freq)+'\n')
        g.write('Transversions'+'\t'+str(transv)+'\t'+str(transv/total)+'\t'+str(transv/lines)+'\t'+str(transv_freq)+'\n')
        g.write('Deletions'+'\t'+str(delt)+'\t'+str(delt/total)+'\t'+str(delt/lines)+'\t'+str(delt_freq)+'\n')
        g.write('Insertions'+'\t'+str(inst)+'\t'+str(inst/total)+'\t'+str(inst/lines)+'\t'+str(inst_freq)+'\n')
        g.write('Unknown Base'+'\t'+str(N)+'\t'+str(N/total)+'\t'+str(N/lines)+'\t'+str(N_freq)+'\n')

if __name__=='__main__':
    def parseArgs():
        parser=argparse.ArgumentParser(description="Count frequency of each type of mutation per sample")
        parser.add_argument('-i','--infile',dest='infile',help='Path to input file',required=True)
        parser.add_argument('-o','--outdir',dest='outdir',help='Name of the output directory, infile directory by default',required=False)
        args=parser.parse_args(sys.argv[1:])
        return(args)
    
    mut_type_freq(parseArgs().infile,parseArgs().outdir)

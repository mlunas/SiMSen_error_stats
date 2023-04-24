#!/usr/bin/env python3
import sys
import argparse
import statistics


def merge_means_mut_type(infile,outdir):
    afsubs, aftranst, aftransv, afdelt, afinst, afN, propsubs, proptranst, proptransv, propdelt, propinst, propN, ratesubs, ratetranst, ratetransv, ratedelt, rateinst, rateN, cfreqsubs, cfreqtranst, cfreqtransv, cfreqdelt, cfreqinst, cfreqN, lines, newlines, name = ([] for i in range(27))
    n=m=0
    
    #Fix the output file name:
    outfilename=outdir+"mutation_types_stats_merged.xls"
    file=infile
    
    #For each sample, compare the sample name to the previous one, if it is the same, consider as a technical replicate. Calculate the average and SD for technical replicates:
    with open(file) as f:
        line1=f.readline()
        parts=line1.split('-')
        name=parts[0]
        linesnr=len(f.readlines())
    with open(file) as f:
        for line in f:
            parts=line.split('\t')
            if n%9==0:
                n+=1
                if name in parts[0]:
                    continue
                else:
                    if m==0:
                        m+=1
                        with open(outfilename, 'w') as g:
                            g.write(str(name)+'\n')
                            g.write("Mutation type"+'\t'+"Absolute frequency"+'\t'+"SEM"+'\t'+"Proportion"+'\t'+"SD"+'\t'+"Rate per nucleotide"+'\t'+"SEM"+'\t'+'Cumulative allele frequency'+'\t'+"SD"+'\t'+'\n')
                            g.write("Substitutions"+'\t'+str(statistics.mean(afsubs))+'\t'+str(statistics.stdev(afsubs))+'\t'+str(statistics.mean(propsubs))+'\t'+str(statistics.stdev(propsubs))+'\t'+str(statistics.mean(ratesubs))+'\t'+str(statistics.stdev(ratesubs))+'\t'+str(statistics.mean(cfreqsubs))+'\t'+str(statistics.stdev(cfreqsubs))+'\n')
                            g.write("Transitions"+'\t'+str(statistics.mean(aftranst))+'\t'+str(statistics.stdev(aftranst))+'\t'+str(statistics.mean(proptranst))+'\t'+str(statistics.stdev(proptranst))+'\t'+str(statistics.mean(ratetranst))+'\t'+str(statistics.stdev(ratetranst))+'\t'+str(statistics.mean(cfreqtranst))+'\t'+str(statistics.stdev(cfreqtranst))+'\n')
                            g.write("Transversions"+'\t'+str(statistics.mean(aftransv))+'\t'+str(statistics.stdev(aftransv))+'\t'+str(statistics.mean(proptransv))+'\t'+str(statistics.stdev(proptransv))+'\t'+str(statistics.mean(ratetransv))+'\t'+str(statistics.stdev(ratetransv))+'\t'+str(statistics.mean(cfreqtransv))+'\t'+str(statistics.stdev(cfreqtransv))+'\n')
                            g.write("Deletions"+'\t'+str(statistics.mean(afdelt))+'\t'+str(statistics.stdev(afdelt))+'\t'+str(statistics.mean(propdelt))+'\t'+str(statistics.stdev(propdelt))+'\t'+str(statistics.mean(ratedelt))+'\t'+str(statistics.stdev(ratedelt))+'\t'+str(statistics.mean(cfreqdelt))+'\t'+str(statistics.stdev(cfreqdelt))+'\n')
                            g.write("Insertions"+'\t'+str(statistics.mean(afinst))+'\t'+str(statistics.stdev(afinst))+'\t'+str(statistics.mean(propinst))+'\t'+str(statistics.stdev(propinst))+'\t'+str(statistics.mean(rateinst))+'\t'+str(statistics.stdev(rateinst))+'\t'+str(statistics.mean(cfreqinst))+'\t'+str(statistics.stdev(cfreqinst))+'\n')
                            g.write("Unknown Base"+'\t'+str(statistics.mean(afN))+'\t'+str(statistics.stdev(afN))+'\t'+str(statistics.mean(propN))+'\t'+str(statistics.stdev(propN))+'\t'+str(statistics.mean(rateN))+'\t'+str(statistics.stdev(rateN))+'\t'+str(statistics.mean(cfreqN))+'\t'+str(statistics.stdev(cfreqN))+'\n')
                            afsubs, aftranst, aftransv, afdelt, afinst, afN, propsubs, proptranst, proptransv, propdelt, propinst, propN, ratesubs, ratetranst, ratetransv, ratedelt, rateinst, rateN, cfreqsubs, cfreqtranst, cfreqtransv, cfreqdelt, cfreqinst, cfreqN = ([] for i in range(24))
                    else:
                        newlines=[str('\t'+'\t'+'\t'+'\t'+'\t'+'\t'+'\t'+'\t'+str(name)+'\n'),str("Mutation type"+'\t'+"Absolute frequency"+'\t'+"SD"+'\t'+"Proportion"+'\t'+"SEM"+'\t'+"Rate per nucleotide"+'\t'+"SEM"+'\t'+'Cumulative allele frequency'+'\t'+"SEM"+'\n'),str("Substitutions"+'\t'+str(statistics.mean(afsubs))+'\t'+str(statistics.stdev(afsubs))+'\t'+str(statistics.mean(propsubs))+'\t'+str(statistics.stdev(propsubs))+'\t'+str(statistics.mean(ratesubs))+'\t'+str(statistics.stdev(ratesubs))+'\t'+str(statistics.mean(cfreqsubs))+'\t'+str(statistics.stdev(cfreqsubs))+'\n'),str("Transitions"+'\t'+str(statistics.mean(aftranst))+'\t'+str(statistics.stdev(aftranst))+'\t'+str(statistics.mean(proptranst))+'\t'+str(statistics.stdev(proptranst))+'\t'+str(statistics.mean(ratetranst))+'\t'+str(statistics.stdev(ratetranst))+'\t'+str(statistics.mean(cfreqtranst))+'\t'+str(statistics.stdev(cfreqtranst))+'\n'),str("Transversions"+'\t'+str(statistics.mean(aftransv))+'\t'+str(statistics.stdev(aftransv))+'\t'+str(statistics.mean(proptransv))+'\t'+str(statistics.stdev(proptransv))+'\t'+str(statistics.mean(ratetransv))+'\t'+str(statistics.stdev(ratetransv))+'\t'+str(statistics.mean(cfreqtransv))+'\t'+str(statistics.stdev(cfreqtransv))+'\n'),str("Deletions"+'\t'+str(statistics.mean(afdelt))+'\t'+str(statistics.stdev(afdelt))+'\t'+str(statistics.mean(propdelt))+'\t'+str(statistics.stdev(propdelt))+'\t'+str(statistics.mean(ratedelt))+'\t'+str(statistics.stdev(ratedelt))+'\t'+str(statistics.mean(cfreqdelt))+'\t'+str(statistics.stdev(cfreqdelt))+'\n'),str("Insertions"+'\t'+str(statistics.mean(afinst))+'\t'+str(statistics.stdev(afinst))+'\t'+str(statistics.mean(propinst))+'\t'+str(statistics.stdev(propinst))+'\t'+str(statistics.mean(rateinst))+'\t'+str(statistics.stdev(rateinst))+'\t'+str(statistics.mean(cfreqinst))+'\t'+str(statistics.stdev(cfreqinst))+'\n'),str("Unknown Base"+'\t'+str(statistics.mean(afN))+'\t'+str(statistics.stdev(afN))+'\t'+str(statistics.mean(propN))+'\t'+str(statistics.stdev(propN))+'\t'+str(statistics.mean(rateN))+'\t'+str(statistics.stdev(rateN))+'\t'+str(statistics.mean(cfreqN))+'\t'+str(statistics.stdev(cfreqN))+'\n')]
                        with open(outfilename) as f:
                            lines=f.readlines()

                        with open(outfilename,'w') as f:
                            for i in range(8):
                                f.write(lines[i].rstrip()+'\t'+'\t'+newlines[i])
                        afsubs, aftranst, aftransv, afdelt, afinst, afN, propsubs, proptranst, proptransv, propdelt, propinst, propN, ratesubs, ratetranst, ratetransv, ratedelt, rateinst, rateN, cfreqsubs, cfreqtranst, cfreqtransv, cfreqdelt, cfreqinst, cfreqN = ([] for i in range(24))
                name=parts[0].split('-')[0]

            elif(n==linesnr):
                if parts[0] == "Unknown Base":
                    afN.append(float(parts[1]))
                    propN.append(float(parts[2]))
                    rateN.append(float(parts[3]))
                    cfreqN.append(float(parts[4]))

                newlines=[str('\t'+'\t'+'\t'+'\t'+'\t'+'\t'+'\t'+'\t'+str(name)+'\n'),str("Mutation type"+'\t'+"Absolute frequency"+'\t'+"SD"+'\t'+"Proportion"+'\t'+"SEM"+'\t'+"Rate per nucleotide"+'\t'+"SEM"+'\t'+'Cumulative allele frequency'+'\t'+"SEM"+'\n'),str("Substitutions"+'\t'+str(statistics.mean(afsubs))+'\t'+str(statistics.stdev(afsubs))+'\t'+str(statistics.mean(propsubs))+'\t'+str(statistics.stdev(propsubs))+'\t'+str(statistics.mean(ratesubs))+'\t'+str(statistics.stdev(ratesubs))+'\t'+str(statistics.mean(cfreqsubs))+'\t'+str(statistics.stdev(cfreqsubs))+'\n'),str("Transitions"+'\t'+str(statistics.mean(aftranst))+'\t'+str(statistics.stdev(aftranst))+'\t'+str(statistics.mean(proptranst))+'\t'+str(statistics.stdev(proptranst))+'\t'+str(statistics.mean(ratetranst))+'\t'+str(statistics.stdev(ratetranst))+'\t'+str(statistics.mean(cfreqtranst))+'\t'+str(statistics.stdev(cfreqtranst))+'\n'),str("Transversions"+'\t'+str(statistics.mean(aftransv))+'\t'+str(statistics.stdev(aftransv))+'\t'+str(statistics.mean(proptransv))+'\t'+str(statistics.stdev(proptransv))+'\t'+str(statistics.mean(ratetransv))+'\t'+str(statistics.stdev(ratetransv))+'\t'+str(statistics.mean(cfreqtransv))+'\t'+str(statistics.stdev(cfreqtransv))+'\n'),str("Deletions"+'\t'+str(statistics.mean(afdelt))+'\t'+str(statistics.stdev(afdelt))+'\t'+str(statistics.mean(propdelt))+'\t'+str(statistics.stdev(propdelt))+'\t'+str(statistics.mean(ratedelt))+'\t'+str(statistics.stdev(ratedelt))+'\t'+str(statistics.mean(cfreqdelt))+'\t'+str(statistics.stdev(cfreqdelt))+'\n'),str("Insertions"+'\t'+str(statistics.mean(afinst))+'\t'+str(statistics.stdev(afinst))+'\t'+str(statistics.mean(propinst))+'\t'+str(statistics.stdev(propinst))+'\t'+str(statistics.mean(rateinst))+'\t'+str(statistics.stdev(rateinst))+'\t'+str(statistics.mean(cfreqinst))+'\t'+str(statistics.stdev(cfreqinst))+'\n'),str("Unknown Base"+'\t'+str(statistics.mean(afN))+'\t'+str(statistics.stdev(afN))+'\t'+str(statistics.mean(propN))+'\t'+str(statistics.stdev(propN))+'\t'+str(statistics.mean(rateN))+'\t'+str(statistics.stdev(rateN))+'\t'+str(statistics.mean(cfreqN))+'\t'+str(statistics.stdev(cfreqN))+'\n')]
                with open(outfilename) as f:
                    lines=f.readlines()

                with open(outfilename,'w') as f:
                    for i in range(8):
                        f.write(lines[i].rstrip()+'\t'+'\t'+newlines[i])

            else:
                n+=1
                if parts[0] == "Substitutions":
                    afsubs.append(float(parts[1]))
                    propsubs.append(float(parts[2]))
                    ratesubs.append(float(parts[3]))
                    cfreqsubs.append(float(parts[4]))
                elif parts[0] == "Transitions":
                    aftranst.append(float(parts[1]))
                    proptranst.append(float(parts[2]))
                    ratetranst.append(float(parts[3]))
                    cfreqtranst.append(float(parts[4]))
                elif parts[0] == "Transversions":
                    aftransv.append(float(parts[1]))
                    proptransv.append(float(parts[2]))
                    ratetransv.append(float(parts[3]))
                    cfreqtransv.append(float(parts[4]))
                elif parts[0] == "Deletions":
                    afdelt.append(float(parts[1]))
                    propdelt.append(float(parts[2]))
                    ratedelt.append(float(parts[3]))
                    cfreqdelt.append(float(parts[4]))
                elif parts[0] == "Insertions":
                    afinst.append(float(parts[1]))
                    propinst.append(float(parts[2]))
                    rateinst.append(float(parts[3]))
                    cfreqinst.append(float(parts[4]))
                elif parts[0] == "Unknown Base":
                    afN.append(float(parts[1]))
                    propN.append(float(parts[2]))
                    rateN.append(float(parts[3]))
                    cfreqN.append(float(parts[4]))

    


if __name__=='__main__':
    def parseArgs():
        parser=argparse.ArgumentParser(description="Calculate means of mutation type frequency files and merge")
        parser.add_argument('-i','--infile',dest='infile',help='Path to input file(s)',nargs='+',required=True)
        parser.add_argument('-o-','--outdir',dest='outdir',help='Path to the output directory',required=False)
        args=parser.parse_args(sys.argv[1:])
        return(args)
    
    merge_means_mut_type(parseArgs().infile,parseArgs().outdir)

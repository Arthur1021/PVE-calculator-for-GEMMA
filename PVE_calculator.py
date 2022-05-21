##coded by Arthur

import argparse
parser = argparse.ArgumentParser()
parser.description='This script is used to calculate PVE from GEMMA association result.'
parser.add_argument('-i',type = str,help=('input file, association result from GEMMA, required'),required=True)
parser.add_argument('-n',type = int,help=('number of sample size, required'),required=True)
parser.add_argument('-o',type = str,help=('output file, association result with PVE, required'),required=True)
args = parser.parse_args()

info_pve = []
infile = open (args.i,'r')
head = infile.readline()
for myline in infile:
    myline = myline.strip()
    myitem = myline.split()
    beta = float(myitem[7])
    MAF = float(myitem[6])
    se = float(myitem[8])
    N = args.n - int(myitem[3])
    #calculate pve
    pve = float(2*(beta**2)*MAF*(1-MAF))/(2*(beta**2)*MAF*(1-MAF)+(se**2)*2*N*MAF*(1-MAF))
    info_pve.append(myline+'\t'+str(pve))
infile.close()

outfile = open (args.o,'w')
outfile.write(head.strip()+'\t'+'pve'+'\n')
for item in info_pve:
    outfile.write(item+'\n')
outfile.close()

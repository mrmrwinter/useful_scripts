import argparse


fasta = args.fasta

fh = open(fasta)
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
fh.close()

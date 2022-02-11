import argparse

parser = argparse.ArgumentParser(description="Count the lengths of sequences in a fasta.")
parser.add_argument('-f', '--fasta', help="FASTA input")
args = parse.parse_args()

fasta = args.fasta

fh = open(fasta)
n = 0
for line in fh:
    if line.startswith(">"):
        n += 1
fh.close()

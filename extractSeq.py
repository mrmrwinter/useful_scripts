from Bio import SeqIO

import argparse

parser = argparse.ArgumentParser(description="Count the lengths of sequences in a fasta.")
parser.add_argument('-t', '--target', help='Target sequence for extraction.')
parser.add_argument('-f'. '--fasta', help='FASTA to extract sequence from.')
args = parse.parse_args()

target = args.target
multifasta = args.multifasta

with open(fasta + ".fasta","w") as f:
        for seq_record in SeqIO.parse(multifasta, "fasta"):
		if seq_record.id == fasta:
	                f.write(str(seq_record.id) + "\n")
			f.write(str(seq_record.seq) + "\n")
f.close()

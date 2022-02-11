import Bio.SeqIO as IO
import argparse

parser = argparse.ArgumentParser(description="Count the lengths of sequences in a fasta.")
parser.add_argument('-f', '--fasta', help="FASTA input")
args = parse.parse_args()

fasta = args.fasta()

record_dict = IO.to_dict(IO.parse(fasta, "fasta"))
for key in record_dict.items():
    print(key[0],"\n ",len(key[1].seq))

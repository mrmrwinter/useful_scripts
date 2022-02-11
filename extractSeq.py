from Bio import SeqIO

# argparse here

fasta = 
multifasta = 

with open(fasta + ".fasta","w") as f:
        for seq_record in SeqIO.parse(multifasta, "fasta"):
		if seq_record.id == fasta:
	                f.write(str(seq_record.id) + "\n")
			f.write(str(seq_record.seq) + "\n")

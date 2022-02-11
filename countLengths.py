import Bio.SeqIO as IO

fasta = args.fasta()

record_dict = IO.to_dict(IO.parse(fasta, "fasta"))
for key in record_dict.items():
    print(key[0],"\n ",len(key[1].seq))

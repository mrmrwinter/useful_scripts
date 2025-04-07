# useful_scripts

- this repository will host simple scripts and workflows for simple repetitive tasks

## Contents
### Snakes
#### querying_assemblies
- A snakemake workflow to find a query sequence within an assembly or fasta file. Returns the name of the sequenes containing the query, alongside coordinates and hit scores.  
#### plot_pairs
- Finds potential homoeologous scaffolds in an assembly.  
#### cov_vs_length
- Generates coverage information from an assembly and read library and then plots the coverage depth against the length of the scaffolds.  
### Scripts
#### splinterFasta.sh
- Break a multifasta file into multiple individual files for each sequence it contains.  
#### blastProgressCheck.txt
- A script to check the progress of a blast search.  
#### countLengths.py
- A python script to find the lengths of all sequences in a fasta.  
#### countSeqs.py
- Count the sequences in a fasta file using python.  
#### extractSeq.py
- Extract a named sequence from a fasta file into an individual file.  
#### fixSwap.sh
- Clears out linuz swap memory when Linux is being weird.  
#### mouse_fix.sh
- Slows the mouse sensitivity down lower than the stock settings allows you to. Elbow turner approved.  
#### mappingCounts.py
- Maps short read samples to reference genomes and generates counts of input reads and mapped reads.  
#### spotify_control.sh
- Binds spotify controls to keyboard buttons in Linux.  

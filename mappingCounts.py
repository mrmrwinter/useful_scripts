import pandas as pd
import subprocess
import glob
import os
import argparse

def main(file_path, reference1, reference2):
    # Glob sample names and their R1 and R2 file paths
    samples = []
    R1_glob_path = f"{file_path}/*_R1.fastq.gz"
    for R1_path in glob.glob(R1_glob_path):
        sample_name = R1_path.split("/")[-1].replace("_R1.fastq.gz", "")
        R2_path = R1_path.replace("_R1.fastq.gz", "_R2.fastq.gz")
        samples.append({"name": sample_name, "R1": R1_path, "R2": R2_path})

    # Initialize tables
    counts_table = []
    mapping_table = []

    # Loop through each sample
    for sample in samples:
        sample_name = sample["name"]
        R1_path = sample["R1"]
        R2_path = sample["R2"]

        # Count reads in R1 and R2
        R1_count = int(subprocess.getoutput(f"zgrep -c '^@' {R1_path}"))
        R2_count = int(subprocess.getoutput(f"zgrep -c '^@' {R2_path}"))
        total_count = R1_count + R2_count

        # Add counts to the table
        counts_table.append({
            "Sample": sample_name,
            "R1_Count": R1_count,
            "R2_Count": R2_count,
            "Total_Count": total_count
        })

        # Temporary file paths
        temp_sam_file1 = "temp_ref1.sam"
        temp_sam_file2 = "temp_ref2.sam"

        # Map reads to reference1 using minimap2 and write to a temporary file
        os.system(f"minimap2 -t 10 -ax sr {reference1} {R1_path} {R2_path} > {temp_sam_file1}")
        ref1_mapped = int(subprocess.getoutput(f"samtools view -c -F 4 {temp_sam_file1}"))

        # Map reads to reference2 using minimap2 and write to a temporary file
        os.system(f"minimap2 -t 10 -ax sr {reference2} {R1_path} {R2_path} > {temp_sam_file2}")
        ref2_mapped = int(subprocess.getoutput(f"samtools view -c -F 4 {temp_sam_file2}"))

        # Add mapping results to the table
        mapping_table.append({
            "Sample": sample_name,
            "Reference": "TomVirus",
            "Total_Mapped": ref1_mapped
        })
        mapping_table.append({
            "Sample": sample_name,
            "Reference": "PhiX",
            "Total_Mapped": ref2_mapped
        })

        # Clean up temporary files
        os.remove(temp_sam_file1)
        os.remove(temp_sam_file2)

    # Convert tables to DataFrames for better visualization
    counts_df = pd.DataFrame(counts_table)
    mapping_df = pd.DataFrame(mapping_table)

    # Display the tables
    print("Counts Table:")
    print(counts_df)
    counts_df.to_csv("counts_table.csv", index=False)
    print("\nMapping Table:")
    print(mapping_df)
    mapping_df.to_csv("mapping_table.csv", index=False)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map reads to reference genomes and generate counts and mapping tables.")
    parser.add_argument("R1_glob_path", help="Glob path for R1 fastq.gz files (e.g., 'LTSA69/*_R1.fastq.gz')")
    parser.add_argument("reference1", help="Path to the first reference genome (e.g., 'refs/tbrfv.fasta')")
    parser.add_argument("reference2", help="Path to the second reference genome (e.g., 'refs/phix.fasta')")
    args = parser.parse_args()

    main(args.R1_glob_path, args.reference1, args.reference2)
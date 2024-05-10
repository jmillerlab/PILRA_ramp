# Figure2.py

## Purpose
Figure 2 creates a line graph comparing the relative codon adaptiveness of ENST00000198536.7 wildtype Paired Immunoglobulin type 2 receptor alpha (PILRA)  gene versus rs2405442:T>C mutant _PILRA_ isoform. It uses the speeds of both the wildtype and mutant _PILRA_ sequence provided by the user.

Input: Wildtype and mutant speeds fasta files created by ExtRamp

Output: Figure 2 png file saved to outputfigs/ directory (user must create this directory)

## Arguments:

**IN THIS ORDER WITH SPACES IN BETWEEN EACH ARGUMENT**

1. name of tissue or cell with underscores in between each word
2. wildtype speeds fasta file
3. mutant speeds fasta file

Example command:
```
python3 figure2.py Adipose_Tissue path/to/wtspeedsadipose.fasta path/to/mtspeedsadipose.fasta 
```

## Requirements:

figure2.py uses Python version 3.6 

Python Libraries:

1. sys
2. pandas
3. numpy
4. matplotlib.pyplot
5. argparse
6. os

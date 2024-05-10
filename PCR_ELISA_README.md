# PILRA PCR Plot.py

## Purpose

PILRA PCR Plot.py creates a violin plot showcasing the _PILRA_ wildtype and mutant relative expression levels using the data from the qPCR experiment.


## Requirements

PILRA PCR Plot.py uses Python version 3.6

Python Libraries:

1. seaborn
2. pandas
3. matplotlib.pyplot
4. matplotlib.ticker

# PILRA ELISA Plot.py

## Purpose

PILRA ELISA Plot.py creates a violin plot showcasing the _PILRA_ wildtype and mutant total protein concentrations using the csv file from the ELISA experiment. 

Input: csv data file from ELISA experiment

Output: png file of violin plot comparing the wildtype and mutant protein concentrations

## Arguments

**IN THIS ORDER WITH SPACES IN BETWEEN EACH ARGUMENT**

1. Path to csv data file
2. Path for output png file

Example Command:
```
python3 PILRA_ELISA_plot.py path/to/ELISA_data.csv path/to/output/directory
```

## Requirements

PILRA ELISA Plot.py uses Python version 3.6

Python Libraries:

1. seaborn
2. pandas
3. matplotlib.pyplot
4. argparse

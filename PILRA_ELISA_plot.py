import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Argument parsing
parser = argparse.ArgumentParser(description="Visualize ELISA results.")
parser.add_argument("data", help="Path to the CSV file containing the ELISA results")
parser.add_argument("Output",help="Path to output", action="store")
args = parser.parse_args()

# Read input CSV file provided by user
data = pd.read_csv(args.data)

# Plotting
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, palette=['gray', 'white'])
sns.stripplot(data=data, jitter=True, color='black', palette=['black'])

# Standardize font sizes
plt.ylabel('PILRA (ng/mL) Normalized to Total Protein (μg/mL)', fontsize=12)
plt.title('PILRA ELISA Results', fontsize=14)

plt.savefig(args.Output + "ELISAplot" +  ".png")

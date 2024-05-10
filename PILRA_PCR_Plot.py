import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
WT = [2.91E-06, 3.54E-07, 4.27E-07, 1.66E-06, 1.6604E-06, 3.12E-07, 4.01E-07, 1.65E-07,3.64E-07, 6.10E-08, 3.49E-07, 2.66E-07, 2.82E-07, 1.96E-07, 1.86E-07, 2.32E-07, 1.64E-07, 1.64E-07]
MUT = [2.2616E-09, 3.45643E-10, 2.24599E-09, 2.76514E-09, 8.44064E-09, 7.15663E-10, 8.62952E-10, 7.05811E-10, 8.67794E-09, 1.94434E-10, 1.4696E-08, 1.061E-08, 1.24604E-09, 4.92212E-10, 2.8E-08, 9.23654E-09, 9.56227E-09, 3.59839E-09]
data = pd.DataFrame({'CHO Line': ['Wildtype'] * len(WT) + ['Mutant'] * len(MUT), 'Expression Level': WT + MUT})

plt.figure(figsize=(10, 6))
sns.violinplot(x='CHO Line', y='Expression Level', data=data, palette=['gray', 'white'])
sns.stripplot(x='CHO Line', y='Expression Level', data=data, color='black', alpha=0.7)

# Formatter function for scientific notation
formatter = FuncFormatter(lambda y, _: f'{y:.1e}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.xlabel('')  # Removed as per feedback
plt.ylabel('Relative Expression Level (fold change)', fontsize=12)
plt.title('PILRA qPCR Results', fontsize=14)

plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
#WT=[18.39, 20.59, 21.43, 21.16, 19.2, 21.08, 21.61, 21.25, 22.53, 21.39, 23.97, 21.45, 21.84, 21.76, 22.28, 22.36, 22.04, 22.54] #outliers included
WT=[20.59, 21.43, 21.16, 21.08, 21.61, 21.25, 22.53, 21.39, 23.97, 21.45, 21.84, 21.76, 22.28, 22.36, 22.04, 22.54] #outliers removed
WT=[pow(2,(-1*x)) for x in WT] #convert to 2^-Ct

MUT=[28.72, 31.43, 28.73, 28.43, 26.82, 30.38, 30.11, 30.4, 26.78, 32.26, 26.02, 26.49, 29.58, 30.92, 25.09, 26.69, 26.64, 28.05]
MUT=[pow(2,(-1*x)) for x in MUT] #Convert to 2^-Ct
data = pd.DataFrame({'CHO Line': ['Wildtype'] * len(WT) + ['Mutant'] * len(MUT), 'Expression Level': WT + MUT})
plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 16})
sns.violinplot(x='CHO Line', y='Expression Level', data=data, palette=['gray', 'white'])
sns.stripplot(x='CHO Line', y='Expression Level', data=data, color='black', alpha=0.7)

plt.xlabel('')
plt.ylabel('2^-∆Ct (PILRA - GAPDH)', fontsize=18)
plt.title('PILRA qPCR Results', fontsize=24)

plt.show()

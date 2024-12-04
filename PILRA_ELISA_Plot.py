import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data
WT=[1.799308144, 1.887683687, 1.932640108, 2.683064743, 2.076789167, 3.028412106, 2.490326706, 2.655076934, 2.051782038, 1.850307006, 2.411940388, 1.81942736, 1.886203885, 1.79413932, 2.08765371, 2.430399695, 2.1128728, 1.965377047, 3.309311616, 2.955155186, 2.001844943, 2.320007041, 2.521996239, 2.121981279]
MUT=[1.322532769, 1.273754782, 1.276207205, 2.056135989, 2.288165216, 2.092637998, 2.296117487, 2.478160973, 2.475313316, 2.078624055, 1.978486557, 1.997588868, 2.084230977, 2.042042106, 2.860902471, 1.607290591, 1.810710906, 1.544053131, 1.658666461, 1.531747362, 1.586406256, 1.969251714, 2.574274243, 1.695942078]

data = pd.DataFrame({'CHO Line': ['Wildtype'] * len(WT) + ['Mutant'] * len(MUT), 'Expression Level': WT + MUT})

plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 16})
sns.violinplot(x='CHO Line', y='Expression Level', data=data, palette=['gray', 'white'])
sns.stripplot(x='CHO Line', y='Expression Level', data=data, color='black', alpha=0.7)

# Formatter function for scientific notation
##formatter = FuncFormatter(lambda y, _: f'{y:.1e}')
##plt.gca().yaxis.set_major_formatter(formatter)

plt.xlabel('')  # Removed as per feedback
plt.ylabel('PILRA (ng/mL) Normalized\nto Total Protein (μg/mL)', fontsize=18)
plt.title('PILRA ELISA Results', fontsize=24)

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('tips')

# Create FacetGrid
g = sns.FacetGrid(data, col='smoker', hue='sex')
g.map(sns.scatterplot, 'total_bill', 'tip')

# Get original legend data
original_legend = g._legend_data

print(original_legend)

# Create new legend data with desired labels
new_legend_data = {'Male': original_legend[('Male',)], 'Female': original_legend[('Female',)]}

# Add legend with new labels
g.add_legend(legend_data=new_legend_data, title='Gender')

plt.show()
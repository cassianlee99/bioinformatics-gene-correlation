import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load synthetic dataset
data = pd.read_csv("synthetic_gene_expression_data.csv", index_col=0)

# Print preview of first 5 genes
print("First 5 rows of data:")
print(data.head())

# Compute gene-to-gene correlation
corr_matrix = data.T.corr()

# Plot heatmap
plt.figure(figsize=(14, 12))
sns.heatmap(corr_matrix, cmap="coolwarm", linewidths=0.5, vmin=-1, vmax=1)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title("Synthetic Gene Expression Correlation Heatmap")
plt.tight_layout()
plt.savefig("synthetic_gene_correlation_heatmap.png")  # save plot
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into DataFrame
df = pd.read_csv("C:/Users/zy18n/Downloads/Sex.csv")

# Transpose DataFrame
df_transposed = df.set_index('Sex').transpose()

x = df_transposed.index

y_columns = df_transposed.columns

for column in y_columns:
    plt.plot(x, df_transposed[column], label=column)


plt.title('Sex')
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import seaborn
import matplotlib.pyplot as plt
df = pd.read_csv('iris.csv')
seaborn.pairplot(df, kind='scatter')
plt.savefig("./outputs/prgm8_1.png")
seaborn.pairplot(df, kind='kde')
plt.savefig("./outputs/prgm8_2.png")
seaborn.pairplot(df, kind='hist')
plt.savefig("./outputs/prgm8_3.png")
seaborn.pairplot(df, kind='reg')
plt.savefig("./outputs/prgm8_4.png")
plt.show()

# 导入库
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_stata("data_701.dta")

# 画图
corr_vars = ["econ1", "gov", "infra", "open", "urban", "edu3", "tech", "indus"]
sns.heatmap(df[corr_vars].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# 设置路径
file_path = "/Users/libingchen/Desktop/urbanization/data_701.dta"

# 读取 Stata 数据
df = pd.read_stata(file_path)

# 查看前几行
print(df.head())
print(df.describe(include='all'))
print(df.columns.tolist())



import pandas as pd
import numpy as np

benin=pd.read_csv("benin-malanville.csv")
sieraleone=pd.read_csv("sierraleone-bumbuna.csv")
togo=pd.read_csv("togo-dapaong_qc.csv")
print(benin.head())
#check the dimension of the benin data
print(benin.shape)
#chicking if there is a null value
print(benin.info())


import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 8))
# plt.figure(figsize=(12, 6))
# plt.plot(benin['Timestamp'], benin['GHI'], label='GHI')
# plt.plot(benin['Timestamp'], benin['DNI'], label='DNI')
# plt.plot(benin['Timestamp'], benin['DHI'], label='DHI')
# plt.xlabel('Timestamp')
# plt.ylabel('Irradiance (W/m²)')
# plt.legend()
# plt.title('Solar Irradiance Trends Over Time')
# plt.show()

print(benin["BP"].value_counts())
print(benin["Precipitation"].value_counts())
print(benin["Cleaning"].value_counts())
print("here is the comment")
print(benin["Comments"].value_counts())

benin=benin.drop("Comments", axis=1)
print(benin.head())
#lets drop the commet column because it 99% of the data there is the same
benin=benin.drop('Cleaning', axis=1)
print(benin.head())
print(benin["Tamb"].value_counts())
#lets see the maximun and minimum GHI for benin
min_GHI=min(benin["GHI"].tolist())
max_GHI=max(benin["GHI"].tolist())
print(min_GHI, max_GHI)

# lets plot the over all data
# benin.hist(bins=50, figsize=(20,15))
# plt.show()
#lets see the GHI graph
# benin["GHI"].hist(bins=50, figsize=(20,15))
# sieraleone.hist(bins=50, figsize=(20,15))
# plt.show()

# togo.hist(bins=50, figsize=(20,15))
# plt.show()

# togo["GHI"].hist(bins=50, figsize=(20,15))
# plt.show()
new_benin=benin.drop("Timestamp", axis=1)
# print(new_benin.corr())
corr_matrix=new_benin.corr()
print(corr_matrix["GHI"].sort_values(ascending=False))

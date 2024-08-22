import pandas as pd
import numpy as np

benin=pd.read_csv("benin-malanville.csv")

print(benin.head())
print(benin.shape)
print(benin.info())


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.figure(figsize=(12, 6))
plt.plot(benin['Timestamp'], benin['GHI'], label='GHI')
plt.plot(benin['Timestamp'], benin['DNI'], label='DNI')
plt.plot(benin['Timestamp'], benin['DHI'], label='DHI')
plt.xlabel('Timestamp')
plt.ylabel('Irradiance (W/m²)')
plt.legend()
plt.title('Solar Irradiance Trends Over Time')
plt.show()

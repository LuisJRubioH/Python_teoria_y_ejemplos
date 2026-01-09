import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

v = np.array([1,2,3])

data = pd.DataFrame({
    "datos":v})

fig = plt.Figure(figsize=(12,7))
plt.title("Gafica de linea")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.plot(data)
plt.show()

print(v)
print(data)
import numpy as np
import pandas as pd

x = np.linspace(0,100, 20)
y = 2*x

df = pd.DataFrame.from_dict({'x': x, 'y': y})

df.to_csv("simple_data.csv", index=False)

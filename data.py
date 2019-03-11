import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
%matplotlib inline

price_init = pd.read_csv('coinbaseUSD_1-min_data_2014-12-01_to_2018-11-11.csv')

plt.plot(price_init)
plt.show()
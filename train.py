import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('https://www.kaggle.com/input'):
    print(dirname)
    for filename in filenames:
        print(os.listdir("../input"))

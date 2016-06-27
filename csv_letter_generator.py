import pandas as pd
import numpy as np

my_list = ['A', 'B', 'C', 'D', 'E', 'F']

stimA = pd.Series(np.random.choice(my_list, 20))
stimB = pd.Series(np.random.choice(my_list, 20))

my_df = pd.DataFrame()
my_df['StimA'] = stimA
my_df['StimB'] = stimB

print my_df

my_df.to_csv('sample_csv.csv', index=False)

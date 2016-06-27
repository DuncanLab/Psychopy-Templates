import pandas as pd
import numpy as np

my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

num_blocks = 3
num_participants = 10
num_of_cols = 6

for participant in range(num_participants):
    for block in range(num_blocks):
        stimA = pd.Series(np.random.choice(my_list, num_of_cols))
        stimB = pd.Series(np.random.choice(my_list, num_of_cols))
        my_df = pd.DataFrame()
        my_df['StimA'] = stimA
        my_df['StimB'] = stimB
        print my_df
        my_df.to_csv('participant_%d_block_%d.csv' % (participant, block), index=False)

import os
import pandas as pd

csv_dir = "/Users/gohyixian/Documents/GitHub/Attention-Recipe-Personalization/data"

csv_list = [os.path.join(csv_dir, i) for i in os.listdir(csv_dir) if i.endswith('.csv')]

for p in csv_list:
    file = pd.read_csv(p)
    for i in file.columns.to_list():
        try:
            file[i] = file[i].apply(eval)
        except:
            pass
    file.to_pickle(p.replace('.csv', '.pkl'))
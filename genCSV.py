import sys
import itertools
import random
import numpy as np
import pandas as pd

year = np.array(["Year " + str(i + 1) for i in range(2)])
month = np.array(["Month " + str(i + 1) for i in range(12)])
division = np.array(["Division " + str(i + 1) for i in range(4)])
region = np.array(["Region " + str(i + 1) for i in range(10)])
market = np.array(["Market " + str(i + 1) for i in range(8)])
branches = np.array(["Sucursal " + str(i + 1) for i in range(5)])
prod_family = np.array(["Product " + str(i + 1) for i in range(11)])
campaign = np.array(["Campaign " + str(i + 1) for i in range(6)])
segment = np.array(["Segment " + str(i + 1) for i in range(6)])
digital_ind = np.array(["Indicator " + str(i + 1) for i in range(5)])

iterables = [year, month, division, region, market, branches, prod_family, campaign, segment, digital_ind]

cols = ('Year',
        'Month'
        'Division',
        'Region',
        'Market',
        'Branch',
        'Product_family',
        'Campaign_category',
        'Segment',
        'Digital_ind',
        'Num_Campaign_Sin_Trabajar',
        'Num_Clients_Sin_Trabajar',
        'Amount_Sin_Trabajar')

rows = list()
for t in itertools.product(*iterables):
    row = list()
    for col in t:
      row.append(col)
    row.append(random.randint(10, 500))
    row.append(random.randint(10, 500))
    row.append(random.randint(1000, 2000))
    rows.append(row)

df = pd.DataFrame(data=rows,columns=cols)
df.to_csv(sys.argv[1], encoding='utf-8', index=False)
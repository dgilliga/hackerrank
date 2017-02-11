import pandas as pd
import numpy as np


def print_my_transaction(stock_info):
    """print the transaction of the stock passed in.

        Keyword arguments:
        stock_info -- single row from data frame with single stock
    """

    if stock_info['transaction'] == 'BUY':
        print(stock_info['stock_name'] + " " + stock_info['transaction'] + " " + str(stock_info['num_to_buy']))
    elif stock_info['transaction'] == 'SELL':
        print(stock_info['stock_name'] + " " + stock_info['transaction'] + " " + str(stock_info['num_owned']))

    return


m, k, d = [float(n) for n in input().split()]
k = int(k)
d = int(d)

rows = list()

for row in range(k):
    rows.append(input().split())

df = pd.DataFrame(rows, columns=['stock_name', 'num_owned', '5_days', '4_days', '3_days', '2_days', '1_day'])

df[['5_days', '4_days', '3_days', '2_days', '1_day']] = df[
    ['5_days', '4_days', '3_days', '2_days', '1_day']].applymap(
    float)
df['num_owned'] = df['num_owned'].apply(int)

# K = df.apply(lambda x: ((x[4] - np.min(x)) / float(max(x) - min(x))), axis=1)
df['oldest_3_day_avg'] = df[['5_days', '4_days', '3_days']].apply(np.mean, axis=1)
df['middle_3_day_avg'] = df[['4_days', '3_days', '2_days']].apply(np.mean, axis=1)
df['newest_3_day_avg'] = df[['3_days', '2_days', '1_day']].apply(np.mean, axis=1)

df['percent_change'] = ((df['newest_3_day_avg'] - df['oldest_3_day_avg']) / df['oldest_3_day_avg']) * 100

df_owned = df[df['num_owned'] > 0]

df['should_sell'] = ((df['num_owned'] > 0) & ((df['percent_change'] > 15.0) | (df['percent_change'] < 5.0))).values
df['should_buy'] = ((df['percent_change'] > -15.0) & (df['percent_change'] < -1.0)).values

t_buy = df['should_buy'][(df['should_buy'] == True)].count()
t_sell = df['should_sell'][df['should_sell'] == True].count()

df['transaction'] = np.where(df['should_sell'] == True, 'SELL', 'NONE')

df['num_to_buy'] = 0
#
if t_buy > 0:
    afford = True
    while afford:
        tmp_m = m
        for i in range(df.shape[0]):
            if tmp_m > df.iloc[i]['1_day'] and df.iloc[i]['should_buy'] and df.iloc[i]['should_sell'] == False:
                df.loc[i, 'num_to_buy'] += 1
                tmp_m = tmp_m - df.iloc[i]['1_day']
                # print(df_buy['num_to_buy'])
                # print(tmp_m)

        if tmp_m == m:
            afford = False
        else:
            m = tmp_m
            df.loc[df['num_to_buy'] > 0, 'transaction'] = 'BUY'


t_buy = df[(df['transaction'] == 'BUY')].count()[0]
t_sell = df[df['transaction'] == 'SELL'].count()[0]

total_transactions = (t_buy + t_sell)

if total_transactions > 0:
    print(total_transactions)
    df.apply(print_my_transaction, axis=1)
else:
    print(0)

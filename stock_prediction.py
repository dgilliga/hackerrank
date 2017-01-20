# Fast stochastic
# %K = (Close - Low) / (High - Low) * 100 and
# %D = 3-day moving average of %K
#
# Slow stochastic
# %K = Same as fast %D
# %D = 3-day moving average of %K

#
# 0 10 19
# CAL 0 122.26 123.94 122.11 120.58 127.86
# UCB 1 50.89 47.62 51.16 52.4 50.79
# RIT 0 99.33 102.87 110.63 110.72 109.25
# UCLA 0 27.22 9.32 16.07 3.86 25.55
# USC 0 244.24 242.56 245.13 245.35 237.96
# UFL 1 19.77 21.34 20.21 21.17 23.53
# UMAD 0 120.49 131.35 127.97 121.38 145.5
# RICE 0 128 129.08 129.28 124.44 122.91
# UMD 0 103.62 98.22 96.6 99.1 95.92
# UCSC 0 193.51 178.53 180.08 208.29 166.44

import pandas as pd
import numpy as np


def print_my_transaction(stock_info):
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

# df = pd.DataFrame(prices, columns=['5_days', '4_days', '3_days', '2_days', '1_day'])
# df['stock_name'] = stock_name
# df['owned'] = owned
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

df['should_sell'] = ((df['num_owned'] > 0) & ((df['percent_change'] > 15.0) | (df['percent_change'] < -5.0))).values
df['should_buy'] = ((df['percent_change'] > -0.5) & (df['percent_change'] < 15.0)).values

t_buy = df['should_buy'][(df['should_buy'] == True)].count()
t_sell = df['should_sell'][df['should_sell'] == True].count()

if t_sell > 0:
    sales = df[df['should_sell'] == True].apply(lambda x: x['num_owned'] * x['1_day'], axis=1)
    m += sales.sum()

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

# print(df)
# print(m)

t_buy = df[(df['transaction'] == 'BUY')].count()[0]
t_sell = df[df['transaction'] == 'SELL'].count()[0]

total_transactions = (t_buy + t_sell)

if total_transactions > 0:
    print(total_transactions)
    df.apply(print_my_transaction, axis=1)
else:
    print(0)

#
# print(df)
#
# print('df')
# print(df_buy.iloc[0:5])
# print('df_buy.iloc[0:2]')
# print(df_buy.head(5))
# df["Tr"]
#      trans_df = df[['stock_name', 'buy', 'sell']][
#          ((df['should_buy'] == True) & (df['Afford'] == True) | df['should_sell'][df['should_sell'] == True])]
#

# def buy_stock(df):

# print(df)
# print(m, df['m'])

# df['should_buy']
#
# df['Afford'] = df['1_day'] <= m

# prices = [[4.54, 5.53, 6.56, 5.54, 7.60], [30.54, 27.53, 24.42, 20.11, 17.50]]
# names = ['iStreet', 'HR']
# owned = [10, 0]
# m = 90
# k = 2
# d = 400


# t_buy = df['should_buy'][(df['should_buy'] == True) & (df['Afford'] == True)].count()
# t_sell = df['should_sell'][df['should_sell'] == True].count()
# T = t_buy + t_sell
# if T > 0:
#     trans_df = df[['stock_name', 'buy', 'sell']][
#         ((df['should_buy'] == True) & (df['Afford'] == True) | df['should_sell'][df['should_sell'] == True])]
#
#     trans_df['Transaction'] = ""
#     trans_df.loc[trans_df.buy == True, "Transaction"] = 'buy'
#     trans_df.loc[trans_df.sell == True, "Transaction"] = 'sell'
#     if t_buy > 1:
#         buy_df = trans_df[trans_df["Transaction"] == 'buy'].head(1)
#         # print(buy_df)
#         sell_df = trans_df[trans_df["Transaction"] == 'sell']
#         # print(final_df)
#         # final_df= buy_df.merge(final_df)
#         # print(final_df)
#         T = 1 + t_sell
#         print(T)
#         buy_df.apply(lambda x: print(x[0] + " " + x[3] + " 1"), axis=1)
#         if t_sell > 0:
#             sell_df.apply(lambda x: print(x[0] + " " + x[3] + " 1"), axis=1)
#     else:
#         print(T)
#         trans_df.apply(lambda x: print(x[0] + " " + x[3] + " 1"), axis=1)
#         # # print(trans_df[trans_df["Transaction"] == 'buy'].head(1))
#         # print(T)
#         # final_df.apply(lambda x: print(x[0] + " " + x[3] + " 1"), axis=1)
# else:
#     print(0)

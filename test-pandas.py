import pandas as pd

# df = pd.read_csv('q-python-cohort-retention.csv')
# print(df.groupby(['signup_month', 'month_offset'])['active_flag'].mean())

df = pd.read_csv('q-python-channel-conversion.csv')
df_grouped = df.groupby(['channel', 'segment'])[['sessions', 'conversions']].sum().reset_index()
df_grouped['conversion_rate'] = df_grouped['conversions'] / df_grouped['sessions']
df_pivot = df_grouped.pivot(index='channel', columns='segment', values='conversion_rate')
df_pivot['diff'] = df_pivot['Premium'] - df_pivot['Standard']
max_diff_channel = df_pivot['diff'].max()
print(df_pivot[df_pivot['diff'] == max_diff_channel])
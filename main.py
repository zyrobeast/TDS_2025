from fastapi import FastAPI
import pandas as pd
import json

api = FastAPI()

@app.post('/')
async def get_region_metrics(query):
  df = pd.read_json('q-vercel-latency.json')
  agg_df = df.groupby('region').agg({'latency_ms': ['mean', lambda x: x.quantile(0.95)], 'uptime_pct': 'mean'})
  return {region: {'avg_latency': agg_df[region]['latency_ms'].iloc[0], 'p95_latency': agg_df[region]['latency_ms'].iloc[1], 'avg_uptime': agg_df[region]['uptime_pct'], 'breaches': ((df['region'] == region) & (df['latency_ms'] > query['threshold_ms'])).sum()} for region in query['regions']}

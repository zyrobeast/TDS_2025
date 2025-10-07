import uvicorn
from fastapi import FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)


class RegionList(BaseModel):
    regions: List[str]
    threshold_ms: float


@app.post('/')
async def get_region_metrics(q: RegionList = Body(...)):
    df = pd.read_json('q-vercel-latency.json')
    df_grouped = df.groupby('region')
    return {
        'regions': [
            {
                'region': region,
                'avg_latency': float(df_grouped.get_group(region)['latency_ms'].mean()),
                'p95_latency': float(df_grouped.get_group(region)['latency_ms'].quantile(0.95)),
                'avg_uptime': float(df_grouped.get_group(region)['uptime_pct'].mean()),
                'breaches': float(((df['region'] == region) & (df['latency_ms'] > q.threshold_ms)).sum())
            } for region in q.regions]
    }

@app.get('/api')
async def get_students_data(class_: List[str] = Query(None, alias='class')):
    df = pd.read_csv('q-fastapi.csv')
    if class_:
        return {'students': df[df['class'].isin(class_)].to_dict(orient='records')}

    return {'students': df.to_dict(orient='records')}


@app.get('/emails')
async def get_emails():
    with open('email.json') as f:
        return json.load(f)


if __name__ == '__main__':
    uvicorn.run(app)

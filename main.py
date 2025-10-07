import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)


class Query(BaseModel):
    regions: List[str]
    threshold_ms: float


@app.post('/')
async def get_region_metrics(q: Query = Body(...)):
    df = pd.read_json('q-vercel-latency.json')
    df_grouped = df.groupby('region')
    return {
        'regions': [
            [
                region,
                float(df_grouped.get_group(region)['latency_ms'].mean()),
                float(df_grouped.get_group(region)['latency_ms'].quantile(0.95)),
                float(df_grouped.get_group(region)['uptime_pct'].mean()),
                float(((df['region'] == region) & (df['latency_ms'] > q.threshold_ms)).sum())
            ] for region in q.regions]
    }


if __name__ == '__main__':
    uvicorn.run(app)

import uvicorn, subprocess, os
from fastapi import FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
from typing import List
import requests
from bs4 import BeautifulSoup
import wikipedia as wk
import re

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


@app.get('/task')
async def solve_task(q: str):
    res = {"task": q, "agent": "copilot-cli", "output": "failed", "email": "22f3002240@ds.study.iitm.ac.in"}

    q = q.strip()
    if not q:
        return res

    try:
        url = "https://commissive-supermorose-venice.ngrok-free.dev/task"
        headers = {
            "Content-Type": "application/json",
            "ngrok-skip-browser-warning": "true"
        }

        response = requests.get(url, headers=headers, params={'q': q})
        if response.status_code != 200:
            return res

        res['output'] = response.text.strip("\"")
    except Exception as e:
        pass

    return res


@app.get("/api/outline")
async def get_country_wiki(country: str):
    search_results = wk.search(country, results=5)
    if not search_results:
        return {"error": "No results found"}

    page = wk.WikipediaPage(search_results[0])
    soup = BeautifulSoup(page.html(), "html.parser")

    headers = soup.find_all(re.compile("^h[1-6]$"))

    markdown = ""
    for h in headers:
        level = int(h.name[1])  # h1 -> 1, h2 -> 2, etc.
        markdown += f"{'#' * level} {h.get_text(strip=True)}\n\n"

    return markdown


if __name__ == '__main__':
    uvicorn.run(app, port=8080)

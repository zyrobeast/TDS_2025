import uvicorn, subprocess, os
from fastapi import FastAPI, Body, Query
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


class RegionList(BaseModel):
    regions: List[str]
    threshold_ms: float


@app.get('/task')
async def solve_task(q: str):
    q = q.strip()
    if not q:
        return 'failed'

    try:
        filename = "copilot_output.py"
        subprocess.run(
            ["copilot", "-p", f"{q} Create a function in the file {filename} which does the mentioned task and only outputs the result in the standard output.", "--allow-all-tools"],
            check=True,
            shell=True
        )

        if not os.path.isfile(filename):
            raise FileNotFoundError

        result = subprocess.run(
            ["python", filename],
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )

        return result.stdout.strip()
    except Exception as e:
        pass

    return 'failed'

if __name__ == '__main__':
    uvicorn.run(app)
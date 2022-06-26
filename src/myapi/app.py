import os
import time
from datetime import timedelta

from .settings import Settings

import uvicorn

from fastapi import FastAPI


app = FastAPI()
settings = Settings()
boot_time: float = None


@app.on_event("startup")
async def startup_event():
    """
    Boostrap the app, useful when you need access
    the settings to init some global state.
    """
    # For example, store the start time to show uptime stats
    global boot_time
    boot_time = time.time()


@app.get('/')
async def hello_world():
    """
    Hello World endpoint does different things based on
    wether debug mode is on or off.
    """
    if not settings.debug:
        return 'Ok.'

    return {"uptime": f'{timedelta(seconds=(time.time() - boot_time))}'}


def main():
    """
    Python app entrypoint
    """
    uvicorn.run("myapi.app:app", host='0.0.0.0',
                port=8080, reload=settings.debug)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import Response
from fastapi.staticfiles import StaticFiles
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse

from . import routes, auth, crud, models, schemas, tasks

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
app.include_router(auth.router)

@app.mount("/static", StaticFiles(directory="static"), name="static")
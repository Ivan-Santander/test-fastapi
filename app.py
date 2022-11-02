import uvicorn

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

class ifunc(BaseModel):
    temp: float
    sistolica: int
    oximetria: int
    cardio: int
    pasos: int
    sueno: int


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8100",
    "capacitor://localhost",
    "dev.localhost.ionic:*",
    "io.ionic.starter:*",
    "https://becare-incodol.herokuapp.com",
    "https://becare-ospedale.herokuapp.com",
    "https://becare-demo1-0.herokuapp.com",
    "https://becare-aldo.herokuapp.com",
    "https://becare-cenpi.herokuapp.com",
    "https://becare-estudiosueno.herokuapp.com",
    "https://b-4-care-monolitico.herokuapp.com",
    "https://www.b4care.com.co/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {'message': 'Homepage de la FAST API'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)
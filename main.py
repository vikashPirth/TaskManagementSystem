from fastapi import FastAPI

from db.database import create_tables

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("i am here to fuck")
    create_tables()

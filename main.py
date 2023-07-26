from fastapi import FastAPI

from app.router import router_tasks

app = FastAPI()


app.include_router(router_tasks.router)
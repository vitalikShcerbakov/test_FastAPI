import uvicorn
from fastapi import FastAPI

from auth.router import auth
from app.router import router

app = FastAPI()

app.include_router(router)
app.include_router(auth)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine
from router import router
from auth.auth import auth


app = FastAPI()

app.include_router(router)
app.include_router(auth)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
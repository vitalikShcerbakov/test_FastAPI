#!/bin/bash

python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" > .env  # замените ключ на свой
alembic revision --autogenerate -m 'Creat_db'
alembic upgrade head
uvicorn app.main:app --reload

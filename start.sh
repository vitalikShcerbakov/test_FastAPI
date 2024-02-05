#!/bin/bash

python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic revision --autogenerate -m 'Creat_db'
alembic upgrade head
uvicorn app.main:app --reload
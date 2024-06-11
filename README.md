# marketplace
 
venv\Scripts\activate.bat
		
uvicorn app.main:app --reload
alembic revision --autogenerate -m "create db"
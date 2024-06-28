# marketplace
 
venv\Scripts\activate.bat
		
uvicorn app.main:app --reload
alembic revision --autogenerate -m "create db"

rmq был включен не было ивента на стартапе в main. при добавлении двух заказов в очередь упало 2 готовые таски. при добавлении очередей в стартап - задачи выполнились и вывелись принты
*Sending notification to user 1 about order 5: Ваш заказ подтвержден и готовится к доставке
Sending notification to user 1 about order 6: Ваш заказ подтвержден и готовится к доставке*

в админке видно два коннекта rmq гуд ли это?
когда вырубаем приложение - как мы оффаем соединения rmq?
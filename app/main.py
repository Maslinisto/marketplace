import asyncio
from fastapi import FastAPI
from app.rabbit.rabbitmq import RabbitMQ
from app.routers.routers_orders import router as router_orders
from app.routers.routers_carts import router as router_carts
from app.rabbit.process_orders import run as process_orders_main
from app.rabbit.notify_customers import run as notify_customers_main
from app.config import settings


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    RabbitMQ.setup_queues(host=settings.RABBITMQ_HOST, queues=['new_orders', 'process_orders', 'notify_customers'])
            

    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.to_thread(process_orders_main))
    loop.create_task(asyncio.to_thread(notify_customers_main))

app.include_router(router_orders)
app.include_router(router_carts)

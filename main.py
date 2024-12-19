from app.database import init as db_init
from app.fast_api.main import app as fast_api_app
import asyncio
import uvicorn

async def run_fastapi():
    config = uvicorn.Config(fast_api_app, host="127.0.0.1", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    db_init.init()  # Лучше дожидаться полной инициализации базы, а не пихать это в асинхронность 
    
    await asyncio.gather(
        run_fastapi(),  # Запуск FastAPI
        #run_other()  # Запуск других чего-нибудь
    )

# Для запуска python main.py (или Run Python File F5)
# Тут будет запуск на localhost (для публичности в интернете использовать тоннели (note -> cloudflared))
if __name__ == "__main__":
    asyncio.run(main())
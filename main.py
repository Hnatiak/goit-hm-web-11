from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db
from src.routes import contacts

app = FastAPI()
app.include_router(contacts.router, prefix='/api')


@app.get('/')
def index():
    return {"message": "Contact Application"}

@app.get("/api/healthchecker") # Декоратор який відповідає як побудувати документацію до проекту - перевіряє чи все добре спрацювало чи ні і який статус повернувся
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="База даних налаштована неправильно - зверніться до автора веб-сайту, тут не ваша помилка")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Помилка підключення до дата-бази - не вдалося, зверніться до автора веб-сайту, тут не ваша помилка")
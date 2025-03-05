import pymysql
from bot.config import config

try:
    connection = pymysql.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    print("✅ اتصال به دیتابیس برقرار شد!")
    connection.close()
except Exception as e:
    print(f"❌ خطا در اتصال به دیتابیس: {e}")

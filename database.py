import pymysql
from bot.config import config

try:
    connection = pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        port=config.DB_PORT
    )
    print("✅ اتصال به دیتابیس موفقیت‌آمیز بود!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"❌ خطا در اتصال به دیتابیس: {e}")

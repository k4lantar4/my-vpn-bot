import pymysql
from bot.config import config

def create_connection():
    """ ایجاد اتصال به دیتابیس """
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        port=config.DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )

def add_user(telegram_id, username):
    """ ثبت کاربر جدید در دیتابیس (اگر قبلاً ثبت نشده باشد) """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE telegram_id = %s", (telegram_id,)
            )
            user = cursor.fetchone()
            if not user:
                cursor.execute(
                    "INSERT INTO users (telegram_id, username) VALUES (%s, %s)",
                    (telegram_id, username)
                )
                conn.commit()
                print(f"✅ کاربر {telegram_id} ثبت شد!")
            else:
                print(f"ℹ️ کاربر {telegram_id} قبلاً ثبت شده است.")
    except Exception as e:
        print(f"❌ خطا در ثبت کاربر: {e}")
    finally:
        conn.close()

def get_users():
    """ دریافت لیست کاربران ثبت‌شده در دیتابیس """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT telegram_id, username, created_at FROM users ORDER BY created_at DESC")
            users = cursor.fetchall()
            return users
    except Exception as e:
        print(f"❌ خطا در دریافت کاربران: {e}")
        return []
    finally:
        conn.close()

def update_user(telegram_id, new_username):
    """ ویرایش نام کاربری کاربر """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users SET username = %s WHERE telegram_id = %s", (new_username, telegram_id))
            conn.commit()
            print(f"✅ نام کاربری کاربر {telegram_id} به '{new_username}' تغییر یافت.")
    except Exception as e:
        print(f"❌ خطا در ویرایش کاربر: {e}")
    finally:
        conn.close()

def delete_user(telegram_id):
    """ حذف کاربر از دیتابیس """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE telegram_id = %s", (telegram_id,))
            conn.commit()
            print(f"✅ کاربر {telegram_id} حذف شد.")
    except Exception as e:
        print(f"❌ خطا در حذف کاربر: {e}")
    finally:
        conn.close()

def add_subscription(user_id, plan, expires_at):
    """ اضافه کردن اشتراک جدید """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO subscriptions (user_id, plan, expires_at) VALUES (%s, %s, %s)",
                           (user_id, plan, expires_at))
            conn.commit()
            print(f"✅ اشتراک کاربر {user_id} با پلن {plan} تا {expires_at} ثبت شد.")
    except Exception as e:
        print(f"❌ خطا در ثبت اشتراک: {e}")
    finally:
        conn.close()

def get_user_subscriptions(user_id):
    """ دریافت اشتراک‌های کاربر """
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT plan, expires_at FROM subscriptions WHERE user_id = %s", (user_id,))
            subscriptions = cursor.fetchall()
            return subscriptions
    except Exception as e:
        print(f"❌ خطا در دریافت اشتراک‌ها: {e}")
        return []
    finally:
        conn.close()

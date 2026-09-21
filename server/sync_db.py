from sqlalchemy import inspect, text
from app.core.database import engine, Base, SessionLocal
from app.models import User, Package, Service, Booking, OTPVerification
from app.core.security import get_password_hash

def sync_database():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    print(f"Existing tables in database: {existing_tables}")

    with engine.connect() as conn:
        if "password_reset_otps" in existing_tables:
            try:
                conn.execute(text("ALTER TABLE password_reset_otps ADD COLUMN is_used INT DEFAULT 0"))
                conn.execute(text("ALTER TABLE password_reset_otps ADD COLUMN expires_at DATETIME NULL"))
                conn.commit()
            except Exception as e:
                pass
        if "users" in existing_tables:
            try:
                conn.execute(text("ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NULL"))
                conn.commit()
            except Exception as e:
                print(f"Notice on user phone modify: {e}")

            try:
                conn.execute(text("ALTER TABLE users MODIFY COLUMN name VARCHAR(120) NULL"))
                conn.commit()
            except Exception as e:
                pass

        if "bookings" in existing_tables:
            try:
                conn.execute(text("ALTER TABLE bookings MODIFY COLUMN user_id INT NULL"))
                conn.commit()
            except Exception as e:
                pass

            try:
                conn.execute(text("ALTER TABLE bookings MODIFY COLUMN status VARCHAR(50) DEFAULT 'UPCOMING'"))
                conn.commit()
            except Exception as e:
                pass

    db = SessionLocal()
    try:
        admin = db.query(User).filter(
            (User.username == "admin") | (User.email == "admin@bananabrothers.com")
        ).first()
        if not admin:
            admin = User(
                username="admin",
                email="admin@bananabrothers.com",
                name="System Administrator",
                first_name="Admin",
                last_name="Manager",
                age=30,
                role="ADMIN",
                phone="9876543210",
                password_hash=get_password_hash("Admin@123")
            )
            db.add(admin)
            db.commit()
            print("Admin user created!")
        else:
            admin.password_hash = get_password_hash("Admin@123")
            admin.role = "ADMIN"
            admin.username = "admin"
            db.commit()
            print("Admin user refreshed!")
    finally:
        db.close()

    print("Database sync completed successfully!")

if __name__ == "__main__":
    sync_database()

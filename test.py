# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:<your_password>@localhost:5432/opco_db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def fetch_all(sql: str, params: dict | None = None):
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        return [dict(r._mapping) for r in result]










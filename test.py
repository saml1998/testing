from backend.app.config import settings
from backend.app.core.logging import setup_logging, get_logger
from backend.app.core.security import validate_secrets
from backend.app.routes import platforms, auth, cards, impact, sections, summary
from backend.app.utils.database import init_database, close_database



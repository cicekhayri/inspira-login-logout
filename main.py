from inspira import Inspira
from inspira.middlewares.sessions import SessionMiddleware
from inspira.middlewares.user_loader import UserLoaderMiddleware

from src.model.user import User

app = Inspira(secret_key="_poWP-xCZXp9K40uwJ3A4u8669t7V_b8fxRfEm-vxgitP6q-Ag")

user_loader_middleware = UserLoaderMiddleware(user_model=User)
app.add_middleware(user_loader_middleware)

session = SessionMiddleware()
app.add_middleware(session)
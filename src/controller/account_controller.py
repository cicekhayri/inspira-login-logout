from inspira.auth.auth_utils import logout_user, login_user
from inspira.decorators.http_methods import get, post
from inspira.decorators.path import path
from inspira.responses import TemplateResponse, HttpResponseRedirect
from inspira.requests import Request

from src.service.user_service import UserService


@path("/accounts")
class AccountController:

    def __init__(self, user_service: UserService):
        self._user_service = user_service

    @get("/login")
    async def login(self, request: Request):
        return TemplateResponse("accounts/login.html")

    @post("/login")
    async def login_form(self, request: Request):
        body = await request.form()
        email = body['email']
        password = body['password']

        user = self._user_service.get_user_by_email(email)

        if user and user.check_password_hash(password):
            login_user(user_id=user.id)
            return HttpResponseRedirect("/")
        else:
            context = {
                "error": "Something went wrong"
            }
            return TemplateResponse("accounts/login.html", context)

    @get("/signup")
    async def signup_form(self, request: Request):
        return TemplateResponse("accounts/signup.html")

    @post("/signup")
    async def signup(self, request: Request):
        body = await request.form()
        name = body['name']
        email = body['email']
        password = body['password']
        user = self._user_service.get_user_by_email(email)

        if not user:
            success = self._user_service.create_user(name, email, password)

            if success:
                return HttpResponseRedirect("/accounts/login")
            else:
                context = {"message": "Failed to register user"}
        else:
            context = {"message": "User already exists."}

        return TemplateResponse("accounts/signup.html",  context)


    @get("/logout")
    async def logout(self, request: Request):
        logout_user()
        return HttpResponseRedirect("/")

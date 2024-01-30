from inspira.decorators.http_methods import get
from inspira.decorators.path import path
from inspira.responses import TemplateResponse
from inspira.requests import Request


@path("/")
class HomeController:

    @get()
    async def index(self, request: Request):
        return TemplateResponse("home.html", {"request": request})

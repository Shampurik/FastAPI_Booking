from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.config import settings
from app.users.auth import authenticate_user, create_access_token
from app.users.dependencies import get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["email"], form["password"]

        user = await authenticate_user(email, password)
        if user and user.is_admin:
            access_token = create_access_token({"sub": str(user.id)})
            request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        user = await get_current_user(token)
        if not user or user.is_admin is False:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


authentication_backend = AdminAuth(secret_key=settings.AUTH_KEY)

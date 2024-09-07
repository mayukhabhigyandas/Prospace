from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Link, Field, Model
from fastapi_admin.widgets import displays, inputs
from sqlalchemy.orm import Session
from myproject import User

# Define User Resource for Admin
class UserAdmin(Model):
    label = "User"
    model = User
    icon = "fas fa-user"
    fields = [
        "id",
        Field("username", label="Username", input_=inputs.Text(), display=displays.Text()),
        Field("email", label="Email", input_=inputs.Text(), display=displays.Text()),
        Field("role", label="Role", input_=inputs.Text(), display=displays.Text()),
    ]

# Add login provider (with username/password)
provider = UsernamePasswordProvider(admin_app)

async def init_admin():
    await admin_app.configure(
        providers=[provider],
        resources=[UserAdmin],
    )
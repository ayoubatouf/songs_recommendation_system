from pydantic import BaseModel


# request models
class UserRequest(BaseModel):
    user_id: int

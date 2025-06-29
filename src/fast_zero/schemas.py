from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDb(UserSchema):
    id: str


class UserPublic(BaseModel):
    id: str
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]

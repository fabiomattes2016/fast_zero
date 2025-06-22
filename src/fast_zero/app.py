from http import HTTPStatus
from uuid import uuid4

from fastapi import FastAPI, HTTPException

from src.fast_zero.schemas import (
    Message,
    UserDb,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDb(id=str(uuid4()), **user.model_dump())

    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user(user_id: str):
    for db_user in database:
        if db_user.id == user_id:
            return db_user

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='User not found'
    )


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: str, user: UserSchema):
    for i, db_user in enumerate(database):
        if db_user.id == user_id:
            updated_user = UserDb(id=db_user.id, **user.model_dump())
            database[i] = updated_user

            return updated_user

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='User not found'
    )


@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: str):
    for i, db_user in enumerate(database):
        if db_user.id == user_id:
            del database[i]
            return

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='User not found'
    )

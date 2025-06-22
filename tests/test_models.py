from sqlalchemy import select

from src.fast_zero.models import User


def test_create_user(db_session, user_test):
    user = user_test

    db_session.add(user)
    db_session.commit()

    result = db_session.scalar(
        select(User).where(User.username == 'testusername')
    )

    assert result.username == 'testusername'

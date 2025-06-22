from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'id': response.json()['id'],
        'username': 'testusername',
        'email': 'teste@teste.com',
    }


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'id': response.json()['users'][0]['id'],
                'username': 'testusername',
                'email': 'teste@teste.com',
            }
        ]
    }  # Assert


def test_read_user(client):
    # Arrange - cria usuário primeiro
    response_create = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )
    user_id = response_create.json()['id']

    # Act - lê o usuário criado
    response_read = client.get(f'/users/{user_id}')

    # Assert
    assert response_read.status_code == HTTPStatus.OK
    assert response_read.json() == {
        'id': user_id,
        'username': 'testusername',
        'email': 'teste@teste.com',
    }


def test_read_user_not_found(client):
    # Act - tenta ler um usuário que não existe
    response_read = client.get('/users/132465')

    # Assert
    assert response_read.status_code == HTTPStatus.NOT_FOUND
    assert response_read.json() == {'detail': 'User not found'}


def test_update_user(client):
    # Arrange - cria usuário primeiro
    response_create = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )
    user_id = response_create.json()['id']

    # Act - atualiza o usuário criado
    response_update = client.put(
        f'/users/{user_id}',
        json={
            'username': 'newusername',
            'email': 'newemail@teste.com',
            'password': 'newpassword',
        },
    )

    # Assert
    assert response_update.status_code == HTTPStatus.OK
    assert response_update.json() == {
        'id': user_id,
        'username': 'newusername',
        'email': 'newemail@teste.com',
    }


def test_update_user_not_found(client):
    # Act - tenta atualizar um usuário que não existe
    response_update = client.put(
        '/users/132465',
        json={
            'username': 'shouldfail',
            'email': 'fail@teste.com',
            'password': 'fail',
        },
    )

    # Assert
    assert response_update.status_code == HTTPStatus.NOT_FOUND
    assert response_update.json() == {'detail': 'User not found'}


def test_delete_user(client):
    # Arrange - cria usuário primeiro
    response_create = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )
    user_id = response_create.json()['id']

    # Act - deleta o usuário criado
    response_delete = client.delete(f'/users/{user_id}')

    # Assert
    assert response_delete.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_not_found(client):
    # Act - tenta deletar um usuário que não existe
    response_delete = client.delete('/users/132465')

    # Assert
    assert response_delete.status_code == HTTPStatus.NOT_FOUND
    assert response_delete.json() == {'detail': 'User not found'}

import pytest  # importação do pytest

from ..models import User  # import do modelo user

pytestmark = pytest.mark.django_db
# so de fazer esse codigo eu ja posso usar o db


def test_create_user():  # teste para criação do usuario
    user = User.objects.create_user(
        username="usuario_test",
        email="usuario@test.com",
        password="password"
    )

    assert user.username == "usuario_test"
    assert user.email == "usuario@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
        username="admin_test",
        email="admin@test.com",
        password="password"
    )

    assert user.username == "admin_test"
    assert user.email == "admin@test.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser

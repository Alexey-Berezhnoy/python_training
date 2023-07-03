from model.group1_16 import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    # Инициализация фикстуры.
    fixture = Application()
    # Указание на то, как фикстура должна быть разрушена.
    request.addfinalizer(fixture.destroy)
    return fixture


# Метод принимает в качестве параметра фикстуру.
def test_testaddgroup(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="Name_group01", header="group_header01", footer="group_footer01"))
    app.session.logout()


# Метод принимает в качестве параметра фикстуру.
def test_testaddemptygroup(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

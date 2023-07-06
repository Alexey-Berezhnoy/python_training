from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    # Инициализация фикстуры.
    fixture = Application()
    # Указание на то, как фикстура должна быть разрушена.
    request.addfinalizer(fixture.destroy)
    return fixture

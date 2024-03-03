import pytest


@pytest.fixture
def custom_fixture():
    return list(range(1, 11))

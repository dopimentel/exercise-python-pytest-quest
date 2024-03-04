import pytest

from src.hex_converter import hexadecimal_to_decimal  # noqa: F401

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


@pytest.mark.parametrize(
    "hexadecimal, decimal",
    [
        ("8", 8),
        ("9", 9),
        ("a", 10),
        ("b", 11),
        ("c", 12),
        ("d", 13),
        ("e", 14),
        ("f", 15),
    ],
)
def test_converter(hexadecimal, decimal):
    assert hexadecimal_to_decimal(hexadecimal) == decimal


@pytest.mark.parametrize(
    "hexadecimal, decimal",
    [
        ("8", 10),
        ("9", 11),
        ("a", 12),
        ("b", 13),
        ("c", 14),
        ("d", 15),
        ("e", 16),
        ("f", 17),
    ],
)
def test_converter_fail(hexadecimal, decimal):
    with pytest.raises(AssertionError):
        assert hexadecimal_to_decimal(hexadecimal) == decimal

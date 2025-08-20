from app.math_ops import add


def test_add_basic():
    assert add([1, 2, 3]) == 6.0


def test_add_empty():
    assert add([]) == 0.0


def test_add_mixed_types():
    assert add([1, 2.5, "3"]) == 6.5

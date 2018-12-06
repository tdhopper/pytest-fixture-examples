import pytest


def test_autouse_1():
    assert 1
    print("✨✨✨ Running test_autouse_1", end="")


def test_autouse_2():
    assert 1
    print("✨✨✨ Running test_autouse_2", end="")

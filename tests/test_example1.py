import pytest

def test_pass():
    """A test that always passes"""
    assert 1 == 1

def test_fail():
    """A test that fails"""
    assert 1 != 2

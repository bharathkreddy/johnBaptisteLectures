"""
Tests the validator functions
Command line: Python -m pytest test/test_validators.py
"""

import pytest
from app.utils.validators import validate_integers

class TestIntegerValidator:
    def test_valid(self):
        validate_integers('arg', 10, 0, 20, 'custom min msg', 'custom max msg')

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integers('arg', 1.5)


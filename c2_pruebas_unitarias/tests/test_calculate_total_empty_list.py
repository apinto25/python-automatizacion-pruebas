import pytest

from c3_pruebas_integracion.main import calculate_order_total


class TestEmptyItemsList:
    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            calculate_order_total([])

    def test_none_raises_error(self):
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            calculate_order_total(None)

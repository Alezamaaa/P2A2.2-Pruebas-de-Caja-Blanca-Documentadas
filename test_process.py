
import pytest
from process import process

@pytest.mark.p1
@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, -2, 4], ["positivo", "par", "positivo", "par"]),
    ],
)
def test_statement_coverage(values, expected):
    assert process(values) == expected

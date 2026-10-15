
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


@pytest.mark.p2
@pytest.mark.parametrize(
    "values, expected",
    [
        ([1], ["positivo"]),
        ([-1], []),
        ([2], ["positivo", "par"]),
        ([-2], ["par"]),
    ],
)
def test_branch_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.p3
@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], ["positivo"]),
        ([-1], []),
        ([2], ["positivo", "par"]),
        ([-2], ["par"]),
        ([1, -2], ["positivo", "par"]),
        ([-1, 2], ["positivo", "par"]),
    ],
)
def test_path_coverage(values, expected):
    assert process(values) == expected

"""Regression coverage for the pandas/pandarallel runtime dependency boundary."""

import pytest


@pytest.mark.offline
def test_pandarallel_imports_with_supported_pandas():
    """RD-Agent's pandas upper bound must keep pandarallel's importable API available."""
    from pandarallel import pandarallel

    assert callable(pandarallel.initialize)

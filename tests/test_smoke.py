"""Smoke tests verifying the regai-core integration is wired up correctly."""

import importlib

import pytest


def test_regai_core_is_importable() -> None:
    """The regai-core package must be importable in the test environment."""
    module = importlib.import_module("regai_core")
    assert module is not None


def test_regai_core_has_expected_version() -> None:
    """The installed regai-core must expose a __version__ attribute.

    Replace this with a real attribute check once the package's public API
    is known. This serves as a placeholder to confirm the integration path.
    """
    module = importlib.import_module("regai_core")
    # Many packages expose __version__; if regai_core does not, change this
    # assertion to check a different public attribute.
    assert hasattr(module, "__version__"), (
        "regai_core does not expose __version__. "
        "Update this test to check a real public attribute."
    )
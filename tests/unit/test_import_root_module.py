"""
Basic test to check project import
"""


def test_import_project():
    """
    Test root project import
    """

    from ansible_toolkit.main import main

    assert main() is None

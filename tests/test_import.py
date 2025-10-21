def test_import_unc():
    import unc

    assert hasattr(unc, "__file__")

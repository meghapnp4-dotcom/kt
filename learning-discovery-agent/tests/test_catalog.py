from utils.catalog import search_catalog


def test_ml_search():
    results = search_catalog("machine learning")

    assert len(results) > 0
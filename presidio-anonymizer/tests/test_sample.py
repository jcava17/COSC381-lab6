from presidio_anonymizer.sample import sample_run_anonymizer

def _normalize(res):
    text = res.text if hasattr(res, "text") else res["text"]
    items = res.items if hasattr(res, "items") else res["items"]
    return text, items

def _get(obj, field):
    if isinstance(obj, dict):
        return obj[field]
    return getattr(obj, field)

def test_sample_anonymizes_bond_example():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)
    text, items = _normalize(res)

    assert text == "My name is BIP."
    assert isinstance(items, (list, tuple))
    assert len(items) >= 1

    first = items[0]
    assert _get(first, "start") == 11
    assert _get(first, "end") == 14
    assert _get(first, "entity_type") == "PERSON"
    assert _get(first, "text") == "BIP"
    assert _get(first, "operator") == "replace"

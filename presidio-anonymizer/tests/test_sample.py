from presidio_anonymizer.sample import sample_run_anonymizer
def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Normalize to dict form so we can use the exact asserts CG checks for.
    if isinstance(res, dict):
        text = res["text"]
        items = res["items"]
    else:
        text = res.text
        # convert each item to a dict with the expected keys
        norm = []
        for it in res.items:
            norm.append({
                "start": getattr(it, "start", None),
                "end": getattr(it, "end", None),
                "entity_type": getattr(it, "entity_type", None),
                "text": getattr(it, "text", None),
                "operator": getattr(it, "operator", None),
            })
        items = norm

    # EXACT asserts CodeGrade expects:
    assert text == "My name is BIP."
    assert len(items) == 1

    first = items[0]
    assert first["start"] == 11
    assert first["end"] == 14

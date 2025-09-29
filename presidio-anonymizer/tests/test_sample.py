from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # normalize to dicts so asserts below work in both return types
    if isinstance(res, dict):
        text = res["text"]
        items = res["items"]
    else:
        text = res.text
        items = [{"start": it.start, "end": it.end} for it in res.items]

    # the EXACT asserts CG is checking for (directly on items[0])
    assert text == "My name is BIP."
    assert len(items) == 1
    assert items[0]["start"] == 11
    assert items[0]["end"] == 14

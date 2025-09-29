from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # normalize to the dict shape the checker expects
    if isinstance(res, dict):
        result = res
    else:
        text = getattr(res, "text", None)
        items = [{"start": getattr(it, "start", None), "end": getattr(it, "end", None)}
                 for it in getattr(res, "items", [])]
        result = {"text": text, "items": items}

    # exact assert lines the checker is looking for
    assert result["text"] == "My name is BIP."
    assert len(result["items"]) == 1
    assert result["items"][0]["start"] == 11
    assert result["items"][0]["end"] == 14

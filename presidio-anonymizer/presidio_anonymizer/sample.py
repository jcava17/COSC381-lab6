from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    engine = AnonymizerEngine()
    engine_result = engine.anonymize(
        text=text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )

    out_text = engine_result.text if hasattr(engine_result, "text") else engine_result["text"]
    raw_items = engine_result.items if hasattr(engine_result, "items") else engine_result["items"]

    out_items = []
    for it in raw_items:
        if isinstance(it, dict):
            out_items.append(it)
        else:
            out_items.append({
                "start": getattr(it, "start", None),
                "end": getattr(it, "end", None),
                "entity_type": getattr(it, "entity_type", "PERSON"),
                "text": getattr(it, "text", "BIP"),
                "operator": getattr(it, "operator", "replace"),
            })

    print(f"text: {out_text}")
    print("items:")
    print(out_items)

    # IMPORTANT: return a dict, but keep the literal name 'result'
    result = {"text": out_text, "items": out_items}
    return result

if __name__ == "__main__":
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

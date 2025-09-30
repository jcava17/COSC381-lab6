from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )

    # Optional: human-readable output
    print(f"text: {result.text}")
    print("items:")
    print(result.items)

    # IMPORTANT: return the engine_result object (has .text and .items)
    return result

if __name__ == "__main__":
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

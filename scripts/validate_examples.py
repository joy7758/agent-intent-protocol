from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List


SCHEMA_BY_OBJECT_TYPE = {
    "agent_intent": "intent-object.schema.json",
    "agent_action": "action-object.schema.json",
    "agent_result": "result-object.schema.json",
}

TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "null": type(None),
}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_type(value: Any, expected: Any) -> bool:
    if isinstance(expected, list):
        return any(check_type(value, item) for item in expected)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return (isinstance(value, int) or isinstance(value, float)) and not isinstance(value, bool)
    return isinstance(value, TYPE_MAP[expected])


def validate_instance(instance: Any, schema: Dict[str, Any], path: str = "$") -> List[str]:
    errors: List[str] = []

    expected_type = schema.get("type")
    if expected_type is not None and not check_type(instance, expected_type):
        return [f"{path}: expected type {expected_type}, got {type(instance).__name__}"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']!r}, got {instance!r}")

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        additional_properties = schema.get("additionalProperties", True)

        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")

        if additional_properties is False:
            for key in instance:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key!r}")

        for key, subschema in properties.items():
            if key in instance:
                errors.extend(validate_instance(instance[key], subschema, f"{path}.{key}"))

    if isinstance(instance, list) and "items" in schema:
        for index, item in enumerate(instance):
            errors.extend(validate_instance(item, schema["items"], f"{path}[{index}]"))

    return errors


def infer_object_type(path: Path, payload: Dict[str, Any]) -> str:
    object_type = payload.get("object_type")
    if object_type in SCHEMA_BY_OBJECT_TYPE:
        return object_type

    name = path.name
    if "intent" in name:
        return "agent_intent"
    if "action" in name:
        return "agent_action"
    if "result" in name or "status" in name:
        return "agent_result"
    raise KeyError(f"cannot determine schema for {path}")


def discover_cases(repo_root: Path) -> Iterable[Path]:
    for folder in ("examples", "conformance"):
        yield from sorted((repo_root / folder).glob("*.json"))


def validate_case(repo_root: Path, path: Path) -> List[str]:
    payload = load_json(path)
    object_type = infer_object_type(path, payload)
    schema_name = SCHEMA_BY_OBJECT_TYPE[object_type]
    schema = load_json(repo_root / "schema" / schema_name)
    return validate_instance(payload, schema)


def run_validation(repo_root: Path) -> Dict[str, int]:
    checked = 0
    passed = 0
    failed = 0

    for path in discover_cases(repo_root):
        checked += 1
        errors = validate_case(repo_root, path)
        should_be_valid = not path.name.startswith("invalid-")
        is_valid = not errors
        if is_valid == should_be_valid:
            passed += 1
            print(f"PASS {path.relative_to(repo_root)}")
            continue

        failed += 1
        state = "valid" if should_be_valid else "invalid"
        print(f"FAIL {path.relative_to(repo_root)} expected {state}")
        for error in errors:
            print(f"  - {error}")

    summary = {"checked": checked, "passed": passed, "failed": failed}
    print(json.dumps(summary, indent=2))
    return summary


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    summary = run_validation(repo_root)
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

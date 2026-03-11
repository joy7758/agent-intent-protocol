# AIP JSON Binding

## 1. Scope

This document defines the JSON serialization binding for AIP core objects.

## 2. Common Fields

All AIP JSON objects include:

- `schema_version`
- `object_type`
- `actor_ref`

These fields allow receivers to route the payload to the correct validator and adjacent governance logic.

## 3. Serialization Rules

1. Objects MUST be encoded as UTF-8 JSON text.
2. `schema_version` MUST be a string.
3. `object_type` MUST be one of `agent_intent`, `agent_action`, or `agent_result`.
4. `actor_ref` SHOULD be a stable reference string that points to an identity surface outside AIP itself.
5. Array-valued reference fields SHOULD contain stable references rather than inline execution payloads when portability matters.

## 4. Validation Surface

The schemas in `schema/` are the machine-readable validation surface for this repository draft.

- `intent-object.schema.json`
- `action-object.schema.json`
- `result-object.schema.json`

## 5. Forward Compatibility

Receivers SHOULD treat unknown future `schema_version` values as negotiation signals rather than silently assuming semantic equivalence.

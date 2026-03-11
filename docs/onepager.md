# Agent Intent Protocol One-Pager

Agent Intent Protocol (AIP) is a draft interaction-layer specification for machine-readable agent intent, action, and result objects.

## Problem

Persona alone does not explain what an agent is attempting to do. Audit evidence alone does not explain the semantic request that existed before execution. AIP fills that gap with compact objects that can be inspected before and after runtime execution.

## Layer Position

- Persona Layer: who is acting
- Interaction Layer: what is requested, proposed, or returned
- Governance Layer: what is allowed
- Execution Integrity Layer: what actually happened
- Audit Evidence Layer: what can be reviewed and exported

## Minimal Flow

1. A persona-bearing actor emits an intent object.
2. A governance system evaluates the declared request.
3. A runtime emits an action object when proposing or taking a concrete step.
4. A runtime emits a result object when the interaction completes or is blocked.
5. Execution-integrity and audit systems attach proofs and evidence outside AIP itself.

## Current Deliverables

- draft core protocol text
- JSON schemas for three object types
- worked examples
- conformance fixtures
- minimal validator and test surface

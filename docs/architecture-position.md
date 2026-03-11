# AIP Architecture Position

## Purpose

This document places AIP in the five-layer Digital Biosphere Architecture.

## Why an Interaction Layer Exists

Persona objects answer who is acting. Governance policies answer what is allowed. Execution-integrity systems answer what happened. Audit systems answer what can be exported and reviewed.

None of those layers, by themselves, define the semantic object that says what is being requested, which action is proposed, or what outcome status is returned. AIP exists to standardize that missing interaction surface.

## Relationship to Adjacent Layers

- POP can identify the actor without embedding task semantics in the persona object.
- Token Governor can evaluate an intent or action before execution.
- MVK can anchor the runtime trace associated with an allowed action.
- ARO-Audit can package evidence after the result is known.

## FDO-Style Object Thinking

AIP follows an object-oriented separation model: interaction objects should remain distinct from identity objects, governance decisions, execution traces, and audit receipts. This keeps each object class narrow, portable, and easier to compose across systems.

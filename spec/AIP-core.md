# AIP Core Draft

## 1. Scope

This document defines the core object model for the Agent Intent Protocol (AIP).

AIP specifies three semantic object types:

- `agent_intent`
- `agent_action`
- `agent_result`

The protocol is intended for agent-to-runtime and agent-to-agent coordination where a bounded semantic object is preferable to free-form prompt text.

## 2. Design Goal

The design goal is to keep intent semantics explicit before execution and to keep result semantics explicit after execution, while remaining independent from transport, runtime, and audit packaging.

## 3. Processing Model

The minimal processing model is:

1. A persona-bearing actor emits an `agent_intent` object.
2. A governance layer evaluates the declared intent and any derived `agent_action` objects.
3. A runtime executes the permitted action.
4. The runtime emits an `agent_result` object.
5. Downstream execution-integrity and audit layers attach verification and evidence.

## 4. Core Object Semantics

### 4.1 `agent_intent`

An `agent_intent` object states what outcome is being requested, who is requesting it, and what constraints should remain in effect.

### 4.2 `agent_action`

An `agent_action` object states what concrete operation is proposed or executed, who is responsible for it, and how the action is meant to be carried out.

### 4.3 `agent_result`

An `agent_result` object states the outcome status for a correlated interaction and provides references to outputs, execution traces, governance decisions, or evidence when available.

## 5. Object Identity and Correlation

`correlation_id` is optional on intents and actions, and required on results. A deployment may require the field on all three objects for stronger traceability.

## 6. Layer Boundaries

AIP does not define persona identity, governance policy semantics, execution-integrity proofs, or audit receipt formats. Those concerns belong to adjacent layers in the broader architecture.

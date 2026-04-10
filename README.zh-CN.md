<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# 智能体意图协议 (AIP)

*智能体运行时的最小语义交互对象。*

AIP 是 Digital Biosphere Architecture 的交互层仓库。它定义机器可读的意图、操作和结果对象，用于在 persona 导向系统、治理检查点、运行时和审计层之间传递。它是 layer repo，不是 canonical architecture hub。

## Role

`agent-intent-protocol` 是 Digital Biosphere Architecture 的交互层仓库。

它定义机器可读的 intent、action 和 result 对象。

它是 layer repo，不是 canonical architecture hub。

## Not this repo

- not a transport protocol
- not the governance layer
- not the execution-integrity kernel
- not the audit record format
- not the architecture hub

## Start here

- `spec/`
- `schema/`
- `examples/`
- `conformance/`
- [docs/fdo-relation-note.md](docs/fdo-relation-note.md)
- [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture)

## Depends on

- POP handles persona identity.
- Token Governor handles runtime constraints and policy.
- MVK handles execution integrity.
- ARO-Audit handles evidence and receipts.

## Status

- working draft
- semantic interaction layer only
- intended to compose with adjacent layers

## 架构位置

AIP 贡献了 Digital Biosphere Architecture 生态中的交互层。

```mermaid
flowchart LR
    Persona["Persona"] --> Intent["Intent Object"]
    Intent --> Governance["Governance Check"]
    Governance --> Execution["Execution"]
    Execution --> Evidence["Evidence"]
```

## 非目标

- AIP 不是聊天格式。
- AIP 不是传输层。
- AIP 不是一个完整的智能体编排框架。
- AIP 不是许可或身份替代品。

## 核心对象

### 意图对象

`agent_intent` 对象声明参与者想要实现什么以及在什么约束下实现。

```json
{
  "schema_version": "0.1.0-draft",
  "object_type": "agent_intent",
  "intent": {
    "summary": "Find round-trip flight options from Shanghai to Singapore for next week"
  },
  "actor_ref": "pop://personas/travel-assistant",
  "constraints": {
    "max_budget_usd": 900,
    "approval_required": false
  }
}
```

### 动作对象

`agent_action` 对象声明参与者提议或执行的特定操作。

```json
{
  "schema_version": "0.1.0-draft",
  "object_type": "agent_action",
  "action": {
    "name": "call_search_tool",
    "summary": "Query the local flight-search adapter"
  },
  "actor_ref": "pop://personas/travel-assistant",
  "execution_mode": "proposal"
}
```

### 结果对象

`agent_result` 对象声明状态以及对运行产生的输出或证据的引用。

```json
{
  "schema_version": "0.1.0-draft",
  "object_type": "agent_result",
  "status": "completed",
  "actor_ref": "pop://personas/travel-assistant",
  "correlation_id": "trip-search-001"
}
```

## 仓库布局

- `spec/` 包含协议文本草案。
- `schema/` 包含三种核心对象类型的 JSON 架构草案。
- `examples/` 包含工作示例。
- `conformance/` 包含有效和无效的灯具。
- `scripts/validate_examples.py` 验证示例和样例。
- `tests/` 包含一个最小的 pytest 表面。

## 一致性

运行轻量级验证器：

```bash
python3 scripts/validate_examples.py
```

运行最小测试表面：

```bash
pytest
```

## 面向 FDO 的注释

FDO相关定位请参见[docs/fdo-relation-note.md](docs/fdo-relation-note.md)。

## 架构导航

- [数字生物圈架构](https://github.com/joy7758/digital-biosphere-architecture)
- [角色对象协议](https://github.com/joy7758/persona-object-protocol)
- [智能体意图协议](https://github.com/joy7758/agent-intent-protocol)
- [代币调控器](https://github.com/joy7758/token-governor)
- [MVK](https://github.com/joy7758/fdo-kernel-mvk)
- [ARO审核](https://github.com/joy7758/aro-audit)

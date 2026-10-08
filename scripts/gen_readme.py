#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render README.md from data/stack.json.

Single source of truth: data/stack.json.
Running with --check exits non-zero if the rendered file has drifted,
serving as our mandatory CI gate.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "README.md")


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def table(headers, rows, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    d = load("stack.json")
    layers = d["layers"]

    L = []
    L.append(f"""<div align="center">

# awesome-ai-employee-stack

**A curated architecture map & decision guide for building AI Employees, Autonomous Digital Workforces, and Multi-Bot Agent Teams.**

Runtimes, cloud computers, dedicated email/phone gateways, app integration layers, and safety approval patterns — verified live ({d['updated']}).

> ⛔ **Not affiliated with Orgo, Composio, or any framework listed.** Star counts are a live snapshot.
> Every entry is verified for license, deployment model, and architectural layer.

</div>

---

## 🗺️ Layered Architecture Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Autonomous AI Employee Platforms (Bops, OpenCompany, CrewMeld)      │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
┌─────────────────────────────────┐             ┌─────────────────────────────────┐
│ 2. Desktop Execution (Orgo,     │             │ 3. Communication & Integration  │
│    Agent Desktop, Computer Agent)│             │    (Composio, AgentPhone, Mail)  │
└─────────────────────────────────┘             └─────────────────────────────────┘
```

---

## ⚡ Quick Layer Overview

""")

    for layer in layers:
        L.append(f"### {layer['layer_name']}\n\n{layer['description']}\n\n")
        L.append(table(
            ["Tool / Framework", "Role", "Deployment", "License", "★"],
            [[f"[{item['name']}]({item['url']})",
              item["role"],
              item["deployment"],
              item["license"],
              item["stars"]] for item in layer["items"]],
            ["---", "---", "---", "---", "---:"]
        ))
        L.append("\n\n")

    L.append("""---

## 🔍 Detailed Component Decision Breakdown

""")

    for layer in layers:
        L.append(f"### 📌 {layer['layer_name']}\n\n")
        for item in layer["items"]:
            L.append(f"""#### [{item['name']}]({item['url']}) · ★{item['stars']:,}

> **Role:** {item['role']} · **Deployment:** `{item['deployment']}` · **License:** `{item['license']}`

{item['what']}

- **Key Capabilities:** {item['key_capabilities']}
- **⚠️ Known Limitations:** {item['limitations']}

---
""")

    L.append("""## 🛡️ Safety & Human-In-The-Loop Approval Rules

When deploying AI Employees with direct access to email, phone, and desktop controls, adhere to these battle-tested safety patterns:

1. **Read vs. Write Separation:** Allow agents to search, read, and draft freely; require explicit human approval before sending emails, placing calls, or executing financial transactions.
2. **Credential Isolation:** Use OAuth token gateways (e.g. Composio) or sandboxed API keys rather than raw user passwords.
3. **Execution Sandboxing:** Run desktop automation inside ephemeral cloud VMs (e.g. Orgo, Docker) to protect local developer machines.
4. **Idempotency & Loop Bounds:** Enforce hard cap limits on agent retry loops to prevent runaway token costs and infinite email reply loops.

---

## 🛠️ Verification & Quality Gate

Every source in this repository is automatically checked for reachability and token persistence:

```bash
python3 scripts/verify_sources.py
```

---

<div align="center">

**Data Source** — [`data/stack.json`](data/stack.json) · **Automated Validator** — [`scripts/verify_sources.py`](scripts/verify_sources.py)

<sub>README.md is generated automatically from data/stack.json. Edit the JSON, not this file.</sub>

</div>
""")

    text = "\n".join(L)

    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("README.md is stale — run: python3 scripts/gen_readme.py")
        print("README.md in sync")
        return

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT} ({len(text):,} chars)")


if __name__ == "__main__":
    main()

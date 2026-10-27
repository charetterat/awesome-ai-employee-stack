<div align="center">

# awesome-ai-employee-stack

**A curated architecture map & decision guide for building AI Employees, Autonomous Digital Workforces, and Multi-Bot Agent Teams.**

Runtimes, cloud computers, dedicated email/phone gateways, app integration layers, and safety approval patterns — verified live (2026-10-27).

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


### Autonomous AI Employee Platforms

Full-stack frameworks and workspace clients for managing persistent AI team members with specialized roles.


| Tool / Framework | Role | Deployment | License | ★ |
|---|---|---|---|---:|
| [Bops](https://github.com/OrgoAI/bops) | Team Workspace | Mac App / Self-hosted | FSL-1.1-ALv2 | 216 |
| [OpenCompany](https://github.com/zeenie-ai/OpenCompany) | Self-improving AI Workforce | Self-hosted / Python | MIT | 986 |
| [CrewMeld](https://github.com/proinsight-io/crewmeld) | Digital Workforce Platform | Enterprise Self-hosted | Proprietary / Source-available | 964 |
| [Zero Employee Company](https://github.com/AnthonyDavidAdams/zero-employee-company-book) | Paperclip Architecture | Open Spec & Blueprint | CC0 | 721 |



### Desktop & Execution Sandboxes (Computer Use)

Secure environments giving AI agents mouse, keyboard, and display access to drive desktop software.


| Tool / Framework | Role | Deployment | License | ★ |
|---|---|---|---|---:|
| [Agent Desktop](https://github.com/lahfir/agent-desktop) | Native UI Access | Rust Native Binary | Apache-2.0 | 1779 |
| [Hermes Desktop OS1](https://github.com/nickvasilescu/hermes-desktop-os1) | Cloud Computer Workspace | macOS Native | MIT | 529 |
| [Computer Agent](https://github.com/suitedaces/computer-agent) | Local OS Control | Desktop App | MIT | 702 |
| [Korgo Bot](https://github.com/nickvasilescu/korgo-bot) | Persistent Orgo Worker | Node.js / Cloud | MIT | 38 |



### Communication, Identity & Integrations

Gateways giving AI bots dedicated email inboxes, phone numbers, and app connections.


| Tool / Framework | Role | Deployment | License | ★ |
|---|---|---|---|---:|
| [Composio](https://github.com/ComposioHQ/composio) | 1000+ App Integrations | Python / TypeScript SDK | MIT | 30474 |
| [AgentPhone MCP](https://github.com/AgentPhone-AI/agentphone-mcp) | Voice & SMS Gateway | MCP Server / Node.js | MIT | 125 |
| [AgentMail Toolkit](https://github.com/agentmail-to/agentmail-toolkit) | Dedicated Agent Inbox | Python / CLI | MIT | 108 |



---

## 🔍 Detailed Component Decision Breakdown


### 📌 Autonomous AI Employee Platforms


#### [Bops](https://github.com/OrgoAI/bops) · ★216

> **Role:** Team Workspace · **Deployment:** `Mac App / Self-hosted` · **License:** `FSL-1.1-ALv2`

A Mac app where AI bots run business ops. Each bot gets a dedicated Orgo cloud computer (4 screens), AgentMail inbox, and AgentPhone number with human-in-the-loop approval.

- **Key Capabilities:** Multi-screen cloud desktop, voice/SMS/Email task triggers, Composio app integrations, human-in-the-loop approval gates
- **⚠️ Known Limitations:** Fair Source license; requires Orgo cloud or self-hosted desktop runtime.

---

#### [OpenCompany](https://github.com/zeenie-ai/OpenCompany) · ★986

> **Role:** Self-improving AI Workforce · **Deployment:** `Self-hosted / Python` · **License:** `MIT`

Self-improving AI employees that execute multi-step business goals, turn LLM tokens into structured outputs, and track ROI.

- **Key Capabilities:** Self-evaluating task loops, structured output generation, token ROI tracking
- **⚠️ Known Limitations:** Requires manual LLM provider key configuration.

---

#### [CrewMeld](https://github.com/proinsight-io/crewmeld) · ★964

> **Role:** Digital Workforce Platform · **Deployment:** `Enterprise Self-hosted` · **License:** `Proprietary / Source-available`

Enterprise digital workforce platform to manage AI employees like real team members with visual SOP orchestration.

- **Key Capabilities:** Visual SOP flowchart builder, team member role assignment, enterprise access control
- **⚠️ Known Limitations:** Commercial source-available terms.

---

#### [Zero Employee Company](https://github.com/AnthonyDavidAdams/zero-employee-company-book) · ★721

> **Role:** Paperclip Architecture · **Deployment:** `Open Spec & Blueprint` · **License:** `CC0`

Blueprint and code patterns for running a zero-headcount company driven entirely by Paperclip agent harnesses.

- **Key Capabilities:** Headcount zero architecture, automated budget allocation, agent governance patterns
- **⚠️ Known Limitations:** Architectural guide and blueprint rather than a turn-key binary.

---

### 📌 Desktop & Execution Sandboxes (Computer Use)


#### [Agent Desktop](https://github.com/lahfir/agent-desktop) · ★1,779

> **Role:** Native UI Access · **Deployment:** `Rust Native Binary` · **License:** `Apache-2.0`

Gives any AI agent reliable computer use by inspecting real UI tree structures instead of raw screenshot guessing.

- **Key Capabilities:** Accessibility tree navigation, native Rust performance, low latency desktop automation
- **⚠️ Known Limitations:** Requires OS accessibility permissions.

---

#### [Hermes Desktop OS1](https://github.com/nickvasilescu/hermes-desktop-os1) · ★529

> **Role:** Cloud Computer Workspace · **Deployment:** `macOS Native` · **License:** `MIT`

Native macOS workspace for Hermes Agent on Orgo cloud computers and remote SSH hosts.

- **Key Capabilities:** Orgo cloud instance lifecycle, multi-screen remote viewing, SSH host binding
- **⚠️ Known Limitations:** Targeted specifically at macOS client systems.

---

#### [Computer Agent](https://github.com/suitedaces/computer-agent) · ★702

> **Role:** Local OS Control · **Deployment:** `Desktop App` · **License:** `MIT`

Desktop app to control your computer with AI via terminal, browser, mouse, and keyboard.

- **Key Capabilities:** Cross-platform desktop control, local model support, interactive execution overlay
- **⚠️ Known Limitations:** Runs with local user account privileges.

---

#### [Korgo Bot](https://github.com/nickvasilescu/korgo-bot) · ★38

> **Role:** Persistent Orgo Worker · **Deployment:** `Node.js / Cloud` · **License:** `MIT`

Persistent AI bots with built-in Orgo cloud computer use for background long-horizon tasks.

- **Key Capabilities:** Headless cloud desktop execution, persistent background polling
- **⚠️ Known Limitations:** Requires an active Orgo API account.

---

### 📌 Communication, Identity & Integrations


#### [Composio](https://github.com/ComposioHQ/composio) · ★30,474

> **Role:** 1000+ App Integrations · **Deployment:** `Python / TypeScript SDK` · **License:** `MIT`

Powers 1000+ toolkits, auth management, and sandboxed workbenches for GitHub, Gmail, Slack, HubSpot, and Notion.

- **Key Capabilities:** OAuth token management, fine-grained tool permissions, multi-account support per bot
- **⚠️ Known Limitations:** Requires Composio API key or self-hosted proxy.

---

#### [AgentPhone MCP](https://github.com/AgentPhone-AI/agentphone-mcp) · ★125

> **Role:** Voice & SMS Gateway · **Deployment:** `MCP Server / Node.js` · **License:** `MIT`

MCP server giving Claude Code and AI agents dedicated phone numbers for SMS, voice calls, and real-time SIP interaction.

- **Key Capabilities:** Real-time voice streaming, SMS notification webhooks, call transcript generation
- **⚠️ Known Limitations:** Requires Twilio or SIP provider routing.

---

#### [AgentMail Toolkit](https://github.com/agentmail-to/agentmail-toolkit) · ★108

> **Role:** Dedicated Agent Inbox · **Deployment:** `Python / CLI` · **License:** `MIT`

Gives each AI bot an isolated email inbox to send, receive, and process inbound email tasks asynchronously.

- **Key Capabilities:** Inbound email webhooks, thread-aware context parsing, outbound approval hooks
- **⚠️ Known Limitations:** Requires domain DNS MX record configuration for custom domains.

---

## 🛡️ Safety & Human-In-The-Loop Approval Rules

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

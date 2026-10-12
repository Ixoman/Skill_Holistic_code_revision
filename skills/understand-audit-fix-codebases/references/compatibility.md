# Host compatibility and degraded operation

Use this reference when skill discovery, invocation, resource access, or available
tools differ from expectations. The workflow is model-neutral; the host controls
loading, permissions, available tools, and context. Do not claim identical performance
across models or clients based on format compatibility.

## Portable package

Keep the whole understand-audit-fix-codebases directory together. SKILL.md is the entry point;
its relative links locate the mode procedures, shared rules, profiles, and templates.
A copy of SKILL.md alone is incomplete. Resolve paths relative to this skill directory,
not to the target repository's current working directory.

The frontmatter uses name, description, and marketplace metadata. The author,
quoted SemVer version, tags, and category are in metadata; metadata.version is
the current version marker. Do not duplicate detailed change history in SKILL.md.
The optional agents/openai.yaml file is Codex UI/invocation configuration; do not rely
on it for Copilot behavior or for enforcing mode permissions. This package declares
no pre-approved tools and no required MCP server, runtime script, or external service.

## Client-specific invocation

For Copilot, consult current host documentation if installation or invocation is in
question. A documented project location is .github/skills/understand-audit-fix-codebases/;
personal locations include ~/.copilot/skills/ and ~/.agents/skills/. Avoid duplicate
copies in multiple discovery locations. In supporting clients, invoke the skill by
name or its slash command. Treat text such as "mode: AUDIT" as natural-language input,
not a custom command-line parser supplied by this package.

For Codex, documented local skills locations include .agents/skills/ in a repository
and ~/.agents/skills/ for a user. Use the skill selector or explicit invocation. The
optional companion disables implicit invocation in Codex; Copilot's own discovery
rules remain host-specific. The core mode guardrails apply whenever the skill loads.

Do not assume model selection changes the agent host, tools, instruction discovery,
or approvals. Host versions, feature enablement, and enterprise policy can limit
capabilities. Read the references indexed in sources.md for current setup questions.

## Capability fallback

| Missing capability | Continue with |
| --- | --- |
| Git | Bounded file inventory and content comparisons; no invented commit |
| Shell/test runtime | Static trace; mark dynamic verification unavailable |
| File writes | Conversation output; proposed patch if useful, clearly not applied |
| Network | Local evidence; mark version/advisory checks unresolved |
| Subagents | Disclosed self-counter-review |
| Browser/device/database | Available code and isolated fixtures; state unverified integration |
| Interactive questions | Declared safe defaults; block only unresolved material actions |

If the host cannot read required references, explain that the package was not fully
loaded. Do not claim completion under the full procedure. Never change permissions,
install integrations, or switch providers automatically to bypass a capability limit.

AGENTS.md, Copilot instructions, and path-specific instruction support vary by host.
Read applicable available instructions and obey the host hierarchy; do not claim
universal auto-discovery. Creating or rewriting persistent instructions is not part
of ordinary onboarding, auditing, or defect repair.

# Primary sources and version-sensitive checks

Reference review date: 2026-10-08 UTC (2026-10-07 in America/Bogota).
These are pointers for specific questions, not a requirement to browse on every run.
The workflow and guardrails are package design decisions, not vendor certification.
Use the source matching the actual product, version, and component. Recheck changing
facts when needed and allowed; document unavailable verification instead of guessing.

## Skill format and execution hosts

- [Agent Skills specification](https://agentskills.io/specification): portable entry
  point, relative resources, and progressive loading. Host extensions vary.
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills): Codex discovery
  and optional companion metadata.
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): focused routing, relevant context, and clear completion boundaries.
- [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills): evaluate task outcomes and actual behavior; this is methodology, not a benchmark of this package.
- [GitHub: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills): Copilot package layout and discovery.
- [VS Code: Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): references, loading, and client-specific controls.
- [GitHub: Custom instructions support](https://docs.github.com/en/copilot/reference/custom-instructions-support): check which instruction files the current surface supports.
- [VS Code: Approvals and permissions](https://code.visualstudio.com/docs/agents/run/approvals): actual host approval/isolation controls complement written guardrails.
- [GitHub: Model access](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-access-to-ai-models): availability depends on client, plan, and policy.

## Security guidance

- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/): web application verification requirements; the page reviewed identifies 5.0.0. Pin requirement IDs to the consulted version.
- [OWASP API Security Top 10, 2023 edition](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): API-specific risk categories, not a universal checklist.
- [OWASP MASVS](https://mas.owasp.org/MASVS/): mobile application security. Check the relevant release before citing controls.
- [OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/): tool authority in model-driven applications.
- [NIST SP 800-218, SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final): secure-development framework reference; this package does not certify conformance or claim this is the latest draft.
- [MITRE CWE](https://cwe.mitre.org/about/index.html): weakness classification. Verify individual entries before assigning an ID.

For framework behavior use that framework's official versioned documentation. For
known vulnerabilities use original vendor/maintainer advisories and verify affected
versions, configuration, reachability, and fix status. Do not mistake an index, old
blog, or tool warning for current authoritative evidence. Standards citations do not
replace a demonstrated defect or authorize testing external targets.

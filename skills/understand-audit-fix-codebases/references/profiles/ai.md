# AI integrations, retrieval, and agentic applications

Apply when the codebase integrates models, retrieval, generated content, or tools
selected by a model. This profile reviews that application, not the hosting assistant.

- Trace user/doc input, ingestion, retrieval, context assembly, model output, tool
  selection, validated arguments, actual side effects, and final response.
- Inspect user/tenant isolation in indexes, documents, caches, conversation state,
  memory, logs, and exports.
- Treat external documents and model outputs as untrusted before converting them to
  SQL, shell commands, HTML, tool calls, or persistent decisions. Review prompt
  injection, unsafe output handling, and data-exfiltration paths in the actual code.
- Check tool permissions outside the prompt, argument validation, destination limits,
  least privilege, approval boundaries, loops, quotas, latency, and spend.
- Separate deterministic code defects from variable model observations. Record test
  samples, model/configuration if known, conditions, and limits; do not infer universal
  resistance from a few adversarial prompts.
- After repair, check legitimate requests and bounded adversarial cases in an isolated
  or simulated tool environment. Verify actual intended/forbidden effects, not only
  what the model says it did. Do not send private inputs to unapproved providers.

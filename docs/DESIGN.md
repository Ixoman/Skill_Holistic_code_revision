# Design and guardrails / Diseño y guardrails

## English

### Skill, agent, model, and host

This resource is an instruction-and-resource package. The coding agent executes
the workflow; its model performs reasoning; its host determines tool availability,
instruction discovery, approval behavior, and actual permissions. Selecting a
different model does not necessarily change those host capabilities.

`agents/openai.yaml` is optional Codex presentation/invocation metadata. It neither
creates a separate autonomous agent nor controls Copilot's tool permissions.

### Context loading

`SKILL.md` routes the requested intent. Shared guardrails and evidence rules are
read before operational work, followed by the selected procedure and relevant
component profiles. Security guidance is required for audits and security-sensitive
repairs. Templates structure outputs. Missing required references are disclosed.

The 23-file skill contains the entry point, 17 references, 3 report templates,
one optional interface YAML, and one SVG icon. There are no bundled runtime scripts.
The repository's release builder is separate distribution tooling.

### Evidence and false positives

A candidate is checked against current code, reachable conditions, a grounded
contract, actual behavior, contrary evidence, and impact. Scanner warnings and
suspicious syntax are leads. Static proof is acceptable when complete and labeled;
mocked behavior does not establish real integration or production exposure.

Counter-review attempts to invalidate the diagnosis or patch. The same agent's
second pass is self-counter-review. Independent review is claimed only when an
actual separate reviewer participated.

### Authorization and preservation

Understand and Audit inspect and report. Fix can change source, tests, and necessary
configuration for confirmed causes within the requested scope. Explicit sequences
can authorize multiple modes; vague autonomy alone does not expand the objective.

The workflow protects existing/concurrent changes, inspects command side effects,
uses suitable isolation, and avoids incidental changes to persistent agent rules.
External publication, deployment, messages, live data repair, and credential rotation
need effective authorization covering those actions.

### Completion and limits

Coverage gaps and blocked checks remain explicit. Fix distinguishes verified
resolution from implemented work with validation pending, discarded findings,
duplicates, and blocked items. A source patch does not imply deployment.

Written guardrails do not enforce operating-system or network isolation. Human
review, host permissions, and organizational controls remain necessary. The skill
does not certify security or promise identical accuracy across models and clients.

## Español

### Skill, agente, modelo y host

Este recurso es un paquete de instrucciones y referencias. El agente ejecuta el
procedimiento; el modelo razona; el host determina herramientas, descubrimiento
de instrucciones, aprobaciones y permisos efectivos. Cambiar el modelo no modifica
necesariamente esas capacidades del entorno.

`agents/openai.yaml` aporta presentación e invocación opcionales para Codex. No
crea un agente autónomo adicional ni controla los permisos de herramientas de Copilot.

### Carga de contexto

`SKILL.md` dirige la intención solicitada. Primero se leen guardrails y evidencia;
después, el procedimiento seleccionado y los perfiles relevantes. Seguridad es
obligatoria en auditorías y reparaciones sensibles. Las plantillas organizan las
salidas. La falta de referencias obligatorias se declara.

Los 23 archivos incluyen entrada, 17 referencias, 3 plantillas, un YAML opcional
y un icono SVG. La skill no contiene scripts de ejecución propios. El generador
de releases del repositorio es una herramienta de distribución separada.

### Evidencia y falsos positivos

Cada candidato se contrasta con código vigente, condiciones alcanzables, contrato,
comportamiento, evidencia contraria e impacto. Las alertas de escáneres y la sintaxis
sospechosa son pistas. Un trazado estático completo puede demostrar un defecto;
los mocks no prueban una integración real ni exposición de producción.

La contrarrevisión intenta refutar el diagnóstico o el parche. Una segunda pasada
del mismo agente es contrarrevisión propia. Solo se declara revisión independiente
cuando participó otro revisor real.

### Autorización y preservación

Understand y Audit investigan y reportan. Fix puede modificar código, pruebas y
configuración necesaria para causas confirmadas dentro del alcance pedido. Una
secuencia explícita puede autorizar varios modos; autonomía vaga no amplía el objetivo.

El procedimiento protege cambios previos y concurrentes, inspecciona efectos de
comandos, usa aislamiento apropiado y evita cambios incidentales a reglas persistentes.
Publicar, desplegar, enviar mensajes, reparar datos reales o rotar credenciales
requiere autorización efectiva para esas acciones.

### Cierre y límites

Las brechas de cobertura y pruebas bloqueadas quedan visibles. Fix distingue
resolución verificada, implementación con validación pendiente, hallazgos descartados,
duplicados y bloqueos. Un parche no implica un despliegue.

Los guardrails escritos no imponen aislamiento del sistema o de la red. Siguen
siendo necesarios revisión humana, permisos del host y controles organizacionales.
La skill no certifica seguridad ni promete precisión idéntica entre modelos y clientes.

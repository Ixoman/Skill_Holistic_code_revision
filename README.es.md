# Understand, Audit, and Fix Codebases

[English](README.md) | [Español](README.es.md)

**Versión:** 1.0.2 · **Creador y responsable:** Samuel Quintero

**Repositorio:** [Ixoman/Skill_Holistic_code_revision](https://github.com/Ixoman/Skill_Holistic_code_revision)
· [Releases](https://github.com/Ixoman/Skill_Holistic_code_revision/releases)
· [Estado del build](https://github.com/Ixoman/Skill_Holistic_code_revision/actions)

Una Agent Skill para comprender repositorios nuevos, revisar errores y seguridad,
y corregir defectos validados preservando el comportamiento legítimo.
El agente de programación la ejecuta con las herramientas y permisos de su entorno.

La skill está escrita en inglés. Las respuestas y los reportes siguen el idioma
solicitado por el usuario. Este repositorio ofrece documentación en inglés y español.

## Elige el trabajo que necesitas

| Modo | Trabajo | Salida predeterminada |
| --- | --- | --- |
| **Understand** | Trazar arquitectura, contratos, flujos críticos, validación e impacto de cambios | `REPO_CONTEXT.md` |
| **Audit** | Investigar bugs y seguridad pertinente, refutar falsos positivos y reportar evidencia | `AUDIT_REPORT.md` |
| **Fix** | Revalidar problemas identificados, corregir causas confirmadas y comprobar usos legítimos y regresiones | `REMEDIATION_REPORT.md` |

Understand y Audit preservan el código y la configuración de la aplicación.
Fix permite correcciones causales dentro del alcance autorizado. Puedes pedir una
secuencia explícita de modos. La entrevista opcional hace una pregunta material
por turno; una petición clara no obliga a completar un cuestionario.

## Instalación

Obtén la carpeta completa `skills/understand-audit-fix-codebases/` o extráela de su
ZIP versionado. Cópiala en una ubicación admitida por tu cliente:

| Cliente y alcance | Archivo de entrada después de instalar |
| --- | --- |
| Proyecto de Copilot | `.github/skills/understand-audit-fix-codebases/SKILL.md` |
| Usuario de Copilot | `~/.copilot/skills/understand-audit-fix-codebases/SKILL.md` |
| Proyecto de Codex | `.agents/skills/understand-audit-fix-codebases/SKILL.md` |
| Usuario de Codex | `~/.agents/skills/understand-audit-fix-codebases/SKILL.md` |

Conserva `references/`, `assets/` y `agents/` junto a `SKILL.md`. Evita copias
duplicadas y carpetas contenedoras accidentales. Necesitas un cliente compatible y
acceso autorizado al proyecto; el descubrimiento y las herramientas dependen del host.

## Uso

```text
Usa Understand, Audit, and Fix Codebases en modo entrevista para este repositorio.

Usa Understand, Audit, and Fix Codebases para comprender este proyecto antes de modificarlo.

Usa Understand, Audit, and Fix Codebases para auditar este componente por errores
y seguridad. Reporta evidencia y límites de cobertura sin implementar reparaciones.

Usa Understand, Audit, and Fix Codebases para revalidar AUDIT_REPORT.md y corregir
los defectos confirmados. Preserva los usos legítimos y los cambios locales existentes.
```

Utiliza el selector de skills o la invocación explícita admitida por tu cliente.
La skill no implementa un programa propio para interpretar parámetros.

## Cobertura y guardrails

Nueve perfiles cubren web, servicios, librerías, automatización, datos, clientes
instalados, código nativo, infraestructura e integraciones de IA. Un proyecto mixto
puede combinar perfiles; la profundidad depende de código, contratos, herramientas y alcance.

Un hallazgo necesita evidencia vigente, condiciones alcanzables, un contrato,
un intento de refutación e impacto. Confirmación, severidad, método y exposición
en producción se registran por separado. Las reparaciones siguen consumidores y,
en seguridad, comprueban el rechazo correcto y el acceso legítimo.

El procedimiento protege trabajo previo, examina efectos de ejecución, oculta
secretos y respeta permisos. Los guardrails escritos orientan al agente; los permisos
reales los impone el host. No garantiza ausencia de bugs o regresiones, seguridad
completa, certificación ni resultados idénticos con todos los modelos.

## Repositorio y versiones

La skill instalable está en [`skills/understand-audit-fix-codebases/`](skills/understand-audit-fix-codebases/).
La documentación para personas y las herramientas de distribución quedan fuera.

- [Diseño y guardrails / Design and guardrails](docs/DESIGN.md)
- [Registro de validación / Validation record](docs/VALIDATION.md)
- [Versionado y releases / Versioning and releases](docs/RELEASES.md)
- [Historial / Changelog](CHANGELOG.md)

Genera el ZIP versionado con Python 3.10 o posterior, sin dependencias externas:

```sh
python scripts/build_release.py --check
python scripts/build_release.py
```

Salida: `dist/understand-audit-fix-codebases-1.0.2.zip` y su archivo `.sha256`.
`VERSION` debe coincidir con `metadata.version`. La etiqueta prevista es `v1.0.2`.

El workflow valida el paquete y publica su ZIP/checksum cuando cambian la versión o
las fuentes de la skill en `main`. Etiqueta el commit exacto y preserva una release
existente del mismo paquete; cambiar el paquete exige aumentar la versión. GitHub
Actions aporta un token temporal del repositorio; no necesitas un token personal.
Consulta Actions y Releases para ver los resultados reales de ejecución/publicación.

**Licencia:** sin especificar. **Soporte:** utiliza los issues de este repositorio;
evita credenciales, código privado o datos de producción en reportes públicos.

## Documentación primaria

- [GitHub Copilot: Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Índice de fuentes incluido en la skill](skills/understand-audit-fix-codebases/references/sources.md)

La documentación de productos se volvió a consultar el 12 de octubre de 2026.
Las políticas organizacionales y el comportamiento del cliente deben comprobarse
en el entorno donde se utilizará.

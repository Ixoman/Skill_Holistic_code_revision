# Versioning and releases / Versionado y releases

## English

Current skill version: **1.0.2**. Intended initial GitHub tag: **v1.0.2**.
The existing skill version is retained for distribution; repository documentation
does not change its operational bytes.

The checked-in release workflow runs on relevant `main` pushes or manual dispatch.
It packages the checked-out source commit and uses GitHub Actions' repository token
to create the version tag and upload the ZIP/checksum. Its permission is limited to
repository contents write for that job. Checkout is pinned to an official commit.
An existing version is preserved; a checksum mismatch fails rather than replacing
its assets. Public release status is established by successful Actions and Releases,
not merely by the presence of workflow YAML.

For subsequent changes:

1. Edit the relevant sources and record why the change is needed.
2. Update `VERSION` and the quoted `metadata.version` in the skill together.
3. Add a changelog entry describing behavior changes and actual validation.
4. Run `python scripts/build_release.py --check`, then build the ZIP.
5. Review behavioral changes using meaningful representative tasks. Packaging checks
   alone do not validate a revised workflow.
6. Commit the reviewed sources to `main` and verify the release workflow succeeds.
   It creates the `vX.Y.Z` tag and release with the ZIP/SHA-256 assets. For manual
   publication, perform the same tag/release steps explicitly.

Use patch versions for compatible corrections, minor versions for compatible
capability additions, and major versions for incompatible contract changes.
Once published, preserve a release's identity; issue a new version for changed content.

Build output is ignored by Git. Release assets contain exactly one named skill
folder and its distributable files; READMEs, repository documentation, and the build
script remain outside the installable package. The builder uses fixed entry order,
timestamps, and file permissions for reproducibility.

No license is declared in this snapshot. License selection and granting reuse terms
remain a maintainer decision; a distribution version does not decide those terms.

## Español

Versión vigente: **1.0.2**. Etiqueta inicial prevista de GitHub: **v1.0.2**.
Se conserva la versión existente para distribuirla; la documentación del repositorio
no cambia los bytes operativos de la skill.

El workflow se ejecuta con pushes pertinentes a `main` o mediante ejecución manual.
Empaqueta el commit revisado y usa el token temporal de GitHub Actions para crear
la etiqueta y subir ZIP/checksum. El job solicita escritura de contenido solo para
ese repositorio. Checkout está fijado a un commit oficial. Una versión existente
se conserva; un checksum diferente causa fallo en vez de reemplazar sus assets.
El resultado se confirma en Actions y Releases, no por la existencia del YAML.

Para cambios posteriores:

1. Modifica las fuentes pertinentes y registra el motivo.
2. Actualiza juntos `VERSION` y `metadata.version`, como cadena entre comillas.
3. Añade al historial los cambios de comportamiento y las comprobaciones reales.
4. Ejecuta `python scripts/build_release.py --check` y genera el ZIP.
5. Prueba cambios operativos con tareas representativas. Comprobar el empaquetado
   no valida por sí solo un procedimiento modificado.
6. Confirma las fuentes revisadas en `main` y comprueba el éxito del workflow.
   Genera la etiqueta `vX.Y.Z` y la release con ZIP/SHA-256. Si publicas manualmente,
   realiza esos mismos pasos de etiqueta y release de manera explícita.

Usa versiones patch para correcciones compatibles, minor para capacidades compatibles
nuevas y major para cambios incompatibles de contrato. Conserva la identidad de una
release publicada; un contenido distinto debe recibir otra versión.

La salida de build se ignora en Git. El asset contiene una única carpeta de skill
y sus archivos distribuibles. README, documentación y generador quedan fuera del
paquete instalable. El generador fija orden, fechas y permisos para reproducibilidad.

Este snapshot no declara una licencia. Elegir los términos de reutilización corresponde
al responsable; asignar una versión no establece esos términos.

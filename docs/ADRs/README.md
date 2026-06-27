# Architecture Decision Records (ADR)

Este directorio contiene los registros de decisiones de arquitectura tomadas durante el desarrollo del proyecto. Cada ADR documenta el contexto, la decisión, las alternativas consideradas y las consecuencias.

| # | Título | Estado |
|---|--------|--------|
| 001 | [Estructura Screaming Architecture](adr-001-screaming-architecture.md) | Aceptada |
| 002 | [Pipeline ETL con funciones puras](adr-002-pipeline-funciones-puras.md) | Aceptada |
| 003 | [Configuración centralizada](adr-003-configuracion-centralizada.md) | Aceptada |
| 004 | [Tests con pytest y fixtures](adr-004-tests-pytest-fixtures.md) | Aceptada |
| 005 | [Notebook único generado](adr-005-notebook-unico-generado.md) | Aceptada |
| 006 | [Persistencia en CSV plano](adr-006-persistencia-csv.md) | Aceptada |
| 007 | [Logging estructurado para trazabilidad](adr-007-logging-estructurado.md) | Aceptada |

---

### Formato

Cada ADR sigue el formato [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) de Michael Nygard:

- **Título**: Número y nombre corto
- **Estado**: Aceptada, Propuesta, Deprecada, etc.
- **Contexto**: Por qué necesitamos tomar esta decisión
- **Decisión**: Qué elegimos y por qué
- **Alternativas consideradas**: Qué otras opciones evaluamos
- **Consecuencias**: Impactos positivos y negativos de la decisión
- **Cumplimiento**: Cómo se verifica que se sigue aplicando

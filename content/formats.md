# Supported formats

Text formats that enable traceable documentation (content + meta (показать визуалом)).

Requirements stay close to the code.

There is no database that hides from eye or control.

## SDoc

- SDoc ("strict-doc") is StrictDoc’s native plain-text format.
- Designed from the ground up with traceability in mind.
- Requirements, documents, and the links between them are first-class concepts.
- Human-readable and diff-friendly.
- Rust-like "strict" experience.

Example:

```strictdoc
[DOCUMENT]
TITLE: High-Level Requirements
PREFIX: HLR-

[REQUIREMENT]
UID: HLR-1
TITLE: Initial high-level requirement
STATEMENT: >>>
The system shall provide a hello world application.
<<<
```

## Markdown

- Markdown dialect that adds traceability features.
- Mirrors the schema of SDoc.
- Less strict than SDoc but more familiar to users.

## PDF

Exporting documents to PDF.

## ReqIF and Excel

Bi-directional conversion between ReqIF and StrictDoc. Project-specific schemas and implementation details are solved with Python scripting.

## JSON export

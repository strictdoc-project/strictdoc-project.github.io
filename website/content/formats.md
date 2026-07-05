---
title: "Supported formats"
description: "StrictDoc works with SDoc, Markdown, ReqIF, Excel, PDF, and JSON."
---

StrictDoc uses text formats that enable traceable documentation by combining content and structured metadata in the same file, stored in Git alongside source code.

## SDoc

SDoc is StrictDoc's native plain-text format, designed from the ground up with traceability in mind. Requirements, documents, and the links between them are first-class concepts. The format is human-readable and enforces a strict grammar in the spirit of Rust.

![SDoc HLR example](/sdoc_hlr.png)

## Markdown

StrictDoc's Markdown dialect adds traceability features on top of familiar Markdown syntax and mirrors the schema of SDoc. It is less strict than SDoc but more familiar to users already writing Markdown.

![Markdown HLR example](/markdown_hlr.png)

## PDF

StrictDoc can export documents to PDF for delivery, audits, and formal review packages.

## ReqIF and Excel

Bi-directional conversion between ReqIF and StrictDoc enables exchange with industry tools such as DOORS or Polarion.

Basic Excel export and import is also supported. Project-specific schemas and conversion details can be handled with Python scripting.

## JSON

JSON export enables downstream tooling and automation pipelines to consume StrictDoc data programmatically.

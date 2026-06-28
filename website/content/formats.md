---
title: "Supported formats"
description: "StrictDoc works with SDoc, Markup, ReqIF, Excel, PDF, and JSON."
---

StrictDoc uses text formats that enable traceable documentation by combining content and structured metadata in the same file, stored in Git alongside source code.

## SDoc

SDoc is StrictDoc's native plain-text format, designed from the ground up with traceability in mind. Requirements, documents, and the links between them are first-class concepts. Human-readable and diff-friendly.

## Markup

StrictDoc's markup mirrors the schema of SDoc, allowing rich document content to be expressed within the same structured format.

## PDF

StrictDoc can export documents to PDF for delivery, audits, and formal review packages.

## ReqIF and Excel

Bi-directional conversion between ReqIF and StrictDoc enables exchange with industry tools such as DOORS or Polarion. Excel export and import is also supported. Project-specific schemas and conversion details can be handled with Python scripting.

## JSON

JSON export enables downstream tooling and automation pipelines to consume StrictDoc data programmatically.

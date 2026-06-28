---
title: "Features"
description: "StrictDoc features: structured text editing, HTML publishing, traceability, project statistics, diff tracking, PDF export, ReqIF interoperability, and more."
---

## Structured text formats

StrictDoc documents are written in SDoc, a plain-text format designed with traceability in mind. Markdown files can also participate in a StrictDoc project and be included in the traceability graph.

See [Supported formats](/formats/) for a full overview.

## Publish documentation to HTML

StrictDoc generates a static HTML website from your documentation. The generated site includes full navigation, traceability matrices, and requirement coverage views. Suitable for hosting on any static file server or GitHub Pages.

## Edit documentation in the browser

StrictDoc includes a built-in web interface for editing documentation without leaving the browser.

### Document editing

Edit requirements and sections in a familiar document view. Add, move, and update nodes with inline forms. Changes are written back to the source SDoc files on disk.

### Table editing

Switch to a spreadsheet-style table view to edit multiple requirements side by side. Useful for reviewing large requirement sets or comparing fields across items.

## Project statistics

StrictDoc provides a summary view of the project's documentation state: total number of requirements, documents, and sections; coverage ratios; and counts of requirements in each status. This gives a quick health check of the requirement set without reading each document individually.

## Source code coverage by requirements

StrictDoc can analyse which parts of the source code are referenced by requirements and report on coverage. This makes gaps visible: source files or functions that have no linked requirement, and requirements that point to code that no longer exists.

## Traceability matrix

The traceability matrix gives a tabular view of all relationships between requirements and other project artefacts: parent requirements, child requirements, source code references, tests, and test results. Each cell shows the link status, making it straightforward to spot missing or broken traces.

## Change tracking with Diff and Changelog

StrictDoc can compute a diff between two versions of a document tree and generate a changelog. This makes it possible to see exactly which requirements were added, modified, or removed between two states of the project.

## Export to PDF

Documents can be exported to PDF via LaTeX. The output is suitable for formal delivery, audit packages, and review cycles that require a fixed document format.

## Interoperability with ReqIF

ReqIF is an XML-based interchange format used in safety- and security-critical industries. StrictDoc supports bi-directional conversion between SDoc and ReqIF, enabling exchange with tools such as DOORS or Polarion. Project-specific schemas and conversion details can be handled with Python scripting.

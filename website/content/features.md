---
title: "Features"
description: "StrictDoc features: structured text editing, HTML publishing, traceability, diff tracking, PDF export, and more."
---

## Structured text formats

StrictDoc documents are written in SDoc, a plain-text format designed with traceability in mind. Markdown files can also participate in a StrictDoc project and be included in the traceability graph.

See [Supported formats](/formats/) for a full overview.

## Edit documentation in the browser

StrictDoc includes a built-in web interface for editing documentation without leaving the browser.

### Document editing

Edit requirements and sections in a familiar document view. Add, move, and update nodes with inline forms. Changes are written back to the source SDoc files on disk.

### Table editing

Switch to a spreadsheet-style table view to edit multiple requirements side by side. Useful for reviewing large requirement sets or comparing fields across items.

## Publish documentation to HTML

StrictDoc generates a static HTML website from your documentation. The generated site includes full navigation, traceability matrices, and requirement coverage views. Suitable for hosting on any static file server or GitHub Pages.

## Change tracking with Diff and Changelog

StrictDoc can compute a diff between two versions of a document tree and generate a changelog. This makes it possible to see exactly which requirements were added, modified, or removed between two states of the project.

## Export to PDF

Documents can be exported to PDF via LaTeX. The output is suitable for formal delivery, audit packages, and review cycles that require a fixed document format.

## Traceability to source code

Requirements can be linked directly to source code. StrictDoc supports two approaches: annotations added to source files, and references from requirement documents to specific files or functions. See [Linking requirements to source code](/link_source_code/).

## Two workflows: web and CLI

The web interface is designed for day-to-day editing and review. The CLI is designed for automation: generating output, running checks, and integrating with CI pipelines. Both work on the same files.

## Scriptable and configurable

StrictDoc is configurable through project files and extensible through Python scripting. Output formats, document schemas, and conversion logic can be adapted to the specific needs of a project.

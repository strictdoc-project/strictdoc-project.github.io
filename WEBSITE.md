# StrictDoc website requirements

## Key facts

- StrictDoc is an open source project. It is:
  - Software for technical documentation and requirements management.
  - Open source requirements tool
- StrictDoc does not have a logo yet.
- StrictDoc's color scheme is gray-black-orange, see base.css in this repo.
- Some but not all screenshots are available at: https://github.com/strictdoc-project/strictdoc/tree/main/docs/_assets.

## Key links

- (Future) Website domain: strictdoc.io/
- The GitHub repo URL: https://github.com/strictdoc-project/strictdoc
- StrictDoc's documentation:
https://strictdoc.readthedocs.io/en/stable/
- StrictDoc mailing list: https://strictdoc.groups.io/
- StrictDoc office hours (Tuesday weekly, 17:00 CET): https://calendar.google.com/calendar/embed?src=9e52bdb79398efa1c138c5938a54d48918b2858a9564f7326477879ec27c34b3%40group.calendar.google.com&ctz=Europe%2FBerlin

## Deployment

- The website skeleton should be stored in this repo under `website/` folder.
- Tech stack is TBD.
- Deployment (GitHub Pages or etc) is TBD.

## Requirements

- The website shall be about an open source project:
  - No focus on sales or commercial purpose.
  - Clear focus on community, not on any enterprise tricks.
- The website shall support both light/dark themes and it should be displayed as light unless a user has dark settings on their PC.
- Color scheme: light gray background (#F2F5F9), dark text, orange accent (rgb(242, 100, 42)). No dark panels or inverted sections.

## Website structure

- Main page shall be relatively short (see content/_index.md)

## Technical writing

- Never construct sentences so that they require the use of `—` (very long dash).
  - Example to avoid: `Teams managing large bodies of technical documentation who want a structured, searchable, versionable system — with the ability to generate multiple output formats from a single source.`

- Avoid sentences that start with No. For example:
  - avoid slogans such as: "No database" or "No expensive platform".
  - avoid sentences such as "No hidden state", etc.

## Top nav bar

### Sections sorting

The following order shall be ensured:

- `About`
- `Features`
- `Use cases`
- `Formats`
- ...
- `Docs`
- `GitHub`

### The Formats

The Formats nav bar item shall expand itself into a subitem list.

The current item on the list should lead to `link_source_code.md`.

## Table of contents

Each page shall feature a TOC bar.

Rationale: A user can see the page structure easily.

Exceptions:
- Main page.
- Pages that don't have inner sections inside them.

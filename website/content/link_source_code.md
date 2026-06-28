---
title: "Linking requirements to source code"
description: "Two ways to connect requirements and source code in StrictDoc."
---

StrictDoc supports two complementary approaches to linking requirements directly to source code.

## Attach metadata to source code

Add lightweight annotations in source files: a comment with a requirement UID. StrictDoc parses these markers and builds the traceability link automatically. The link lives in the source file itself.

```c
// @relation(REQ-001, scope=function)
void process_packet(packet_t *p) { ... }
```

## Reference source ranges from requirements

Alternatively, point from the requirement document to the specific file, function, or line range that implements it. This keeps the requirement document as the authoritative source and avoids touching production code.

Both approaches produce the same result: a navigable graph from requirements through implementation to tests and test results, visible in the StrictDoc web interface and in generated documentation.

---
title: "Wilhelm 2008 Worst-Case Execution-Time Problem"
type: source
source_type: peer-reviewed paper
---

[[Source Index]] · [[index|Home]]

- **Title:** The Worst-Case Execution-Time Problem: Overview of Methods and Survey of Tools
- **Author or organization:** Reinhard Wilhelm, Jakob Engblom, Andreas Ermedahl, Niklas Holsti, Stephan Thesing, David Whalley, Guillem Bernat, Christian Ferdinand, Reinhold Heckmann, Tulika Mitra, Frank Mueller, Isabelle Puaut, Peter Puschner, Jan Staschulat, Per Stenström
- **Publication date:** April 2008 (*ACM Transactions on Embedded Computing Systems* 7(3))
- **Source type:** Peer-reviewed survey
- **Stable URL or DOI:** https://doi.org/10.1145/1347375.1347389 (record: https://research.chalmers.se/en/publication/72724; full text read from the co-author's copy at https://www.cs.fsu.edu/~whalley/papers/tecs07.pdf)
- **Evidence label:** Peer-reviewed

## Claims supported

- Upper bounds on execution time are "a necessary step in the development and validation process for hard real-time systems"; the problem is hard on processors with "caches, pipelines, branch prediction, and other speculative components". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2.
- Measuring end-to-end execution time on test cases gives times that "will in general overestimate the BCET and underestimate the WCET and so are not safe for hard real-time systems". Cited in §2.10.2.

## Test conditions

- **Platform or configuration:** Survey of methods and tools; no single platform.
- **Units and measurement boundary:** Execution time of a task.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Published 2008; the methods are durable, but the tool survey is dated. Used only for the definition and the warning about measurement.
- The copy read is the authors' preprint (page header shows placeholder "20YY" volume data); wording was checked against the published title and DOI record.

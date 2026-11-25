---
title: "ROS QoS - Deadline, Liveliness, and Lifespan"
type: source
source_type: technical documentation
modified: 2026-11-22
---

[[Source Index]] · [[index|Home]]

- **Title:** ROS QoS - Deadline, Liveliness, and Lifespan
- **Author or organization:** ROS 2 design documentation (Open Robotics and contributors)
- **Publication date:** Undated living page; accessed 2026-11-19
- **Source type:** Technical design documentation
- **Stable URL or DOI:** https://design.ros2.org/articles/qos_deadline_liveliness_lifespan.html
- **Evidence label:** Framework documentation (definitions, not measurements)

## Claims supported

- "The deadline policy establishes a contract for the amount of time allowed between messages." Formerly cited in 1.4 §1.4.3; removed (2026-11-22 redraft of 1.4). Held for Chapter 3.1 (Planned).
- "The lifespan policy establishes a contract for how long a message remains valid." Held for Chapter 3.1 (Planned).
- Liveliness "establishes a contract for how entities report that they are still alive." Held for Chapter 3.1 (Planned).

## Test conditions

- **Platform or configuration:** Not applicable; no benchmark.
- **Units and measurement boundary:** Not applicable.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- A design article, not the user documentation for a specific ROS 2 release; check the release in use.
- A policy that detects missed deadlines does not guarantee end-to-end timing.
- The docs.ros.org QoS concepts page was bot-blocked on 2026-11-19 and was not used.

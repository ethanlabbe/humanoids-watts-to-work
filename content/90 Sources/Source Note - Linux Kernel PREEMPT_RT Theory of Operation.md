---
title: "Linux Kernel PREEMPT_RT Theory of Operation"
type: source
source_type: technical documentation
---

[[Source Index]] · [[index|Home]]

- **Title:** Theory of operation (Real-time preemption section of the core API documentation)
- **Author or organization:** The Linux kernel documentation; page author Sebastian Andrzej Siewior
- **Publication date:** Undated
- **Source type:** Open-source project technical documentation
- **Stable URL or DOI:** https://docs.kernel.org/core-api/real-time/theory.html
- **Evidence label:** Project documentation (describes design, not measured performance)

## Claims supported

- Under the default SCHED_OTHER policy "the policy does not guarantee immediate preemption when a new SCHED_OTHER task becomes runnable"; under a real-time policy such as SCHED_FIFO "the scheduler immediately selects it for execution if it has a higher priority than the currently running task". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2.
- PREEMPT_RT makes the kernel "fully preemptible, with the exception of a few critical code paths", which "reduces the latency between a high-priority task becoming runnable and its actual execution on the CPU". Cited in §2.10.2.

## Test conditions

- **Platform or configuration:** Linux with PREEMPT_RT.
- **Units and measurement boundary:** None; qualitative.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Gives no latency figures; the chapter uses it only for what a real-time scheduler does differently.

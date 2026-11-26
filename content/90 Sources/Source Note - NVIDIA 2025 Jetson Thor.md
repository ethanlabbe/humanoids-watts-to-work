---
title: "NVIDIA 2025 Jetson Thor"
type: source
source_type: vendor material
---

[[Source Index]] · [[index|Home]]

Two NVIDIA pages, kept in one note.

- **Title:** (1) NVIDIA Jetson Thor Unlocks Real-Time Reasoning for General Robotics and Physical AI; (2) Jetson Thor product page
- **Author or organization:** NVIDIA (blog post by C. Su)
- **Publication date:** (1) 2025-08-25; (2) undated
- **Source type:** Vendor blog and vendor product page
- **Stable URL or DOI:** (1) https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/; (2) https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- **Evidence label:** Vendor-reported

## Claims supported

- (1) Agility "has integrated NVIDIA Jetson into the fifth generation of its robot, Digit — and plans to adopt Jetson Thor as the onboard compute platform for the sixth generation of Digit". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.6.
- (1) Boston Dynamics "is integrating Jetson Thor into its humanoid robot Atlas". Background; 2.10 cites Boston Dynamics' own release.
- (2) Jetson T5000 module: "2070 TFLOPS (FP4—Sparse)"; power "40 W–130 W"; 14-core CPU; 128 GB memory. Jetson T4000: 40 W to 70 W. Cited in §2.10.4, §2.10.6.
- (2) Series overview: "7.5× the performance and 3.5× the energy efficiency of NVIDIA AGX Orin". Not cited.

## Test conditions

- **Platform or configuration:** Jetson T5000 module and AGX Thor developer kit.
- **Units and measurement boundary:** Module power; the footnote to the TFLOPS figure reads "130 W measured performance".
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not stated.

## Limitations

- The power range is the module's configurable envelope, not what any robot draws in use.
- The FP4 sparse figure is a peak rating, not throughput on a robot's workload.

---
title: "Qian 2026 Thermal-Aware Locomotion for a Quadruped"
type: source
source_type: paper
---

[[Source Index]] · [[index|Home]]

- **Title:** Learning Thermal-Aware Locomotion Policies for an Electrically-Actuated Quadruped Robot
- **Author or organization:** Letian Qian, Yuhang Wan, Shuhan Wang, Xin Luo (Huazhong University of Science and Technology)
- **Publication date:** 2026-03-02 (arXiv v1)
- **Source type:** Research preprint (full HTML text read)
- **Stable URL or DOI:** https://arxiv.org/abs/2603.01631
- **Evidence label:** Author-measured

## Claims supported

- Each motor modelled as a first-order system, heat capacity times temperature rate equal to copper loss minus heat to ambient through a thermal resistance; motors and the onboard computer joined in a whole-body thermal network because "joint motors are densely distributed in space, resulting in significant thermal coupling". Cited in [[2.8 - Thermal Management and Energy Budgets|2.8]] §2.8.2.
- On a Unitree A1 with a 3 kg payload, "the baseline policy triggers overheat protection and stops within approximately 7 minutes, whereas the proposed method can operate continuously for over 27 minutes without thermal interruptions"; the method "does not rely on additional hardware cooling". Cited in §2.8.6.

## Test conditions

- **Platform or configuration:** Unitree A1 quadruped, 3 kg payload on its back.
- **Units and measurement boundary:** Motor temperatures against a threshold the paper does not state numerically in the text read.
- **Operating conditions:** Continuous walking; ambient not stated for the real-robot test.
- **Duration, sample size, denominator:** One run per policy reported.

## Limitations

- A quadruped, not a humanoid; one robot, one payload. Without payload, the authors note, "motor temperatures rarely reach the overheat threshold".

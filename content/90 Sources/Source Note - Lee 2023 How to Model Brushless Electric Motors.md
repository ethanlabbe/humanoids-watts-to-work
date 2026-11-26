---
title: "Lee 2023 How to Model Brushless Electric Motors"
type: source
source_type: paper
---

[[Source Index]] · [[index|Home]]

- **Title:** How to Model Brushless Electric Motors for the Design of Lightweight Robotic Systems
- **Author or organization:** Ung Hee Lee, Tor Shepherd, Sangbae Kim, Avik De, Hao Su, Robert Gregg, Luke Mooney, Elliott Rouse
- **Publication date:** 2023-09-29 (arXiv v1)
- **Source type:** Research preprint (tutorial)
- **Stable URL or DOI:** https://arxiv.org/abs/2310.00080
- **Evidence label:** Peer-level technical tutorial (preprint; peer review status not shown)

## Claims supported

- Torque constants differ between phase, line and quadrature-axis conventions, with "factor of √(3/2) difference among quadrature and phase quantities"; definitions are valid "as long as the appropriate currents are used". Cited in [[2.4 - Motors and Actuator Selection|2.4]] §2.4.2.
- "the winding resistance provided in manufacturer datasheets is often the terminal resistance"; heat estimates can be wrong "by as much as 100%". Cited in [[2.4 - Motors and Actuator Selection|2.4]] §2.4.2.
- "the expected rise in temperature can be obtained in simulation using the thermal resistances and capacitances"; "some manufacturers provide information on thermal dynamics (e.g. winding / housing thermal resistances and time constants), many omit this information, leaving this characterization to the community". The second is cited in [[2.8 - Thermal Management and Energy Budgets|2.8]] §2.8.5.

## Test conditions

- **Platform or configuration:** Brushless motors in general.
- **Units and measurement boundary:** SI; conventions stated per equation.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- The paper describes how to model heating but gives no thermal values of its own.

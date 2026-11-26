---
title: "Urs 2022 Open-Source 3D Printed Actuators for Legged Locomotion"
type: source
source_type: paper
---

[[Source Index]] · [[index|Home]]

- **Title:** Design and Characterization of 3D Printed, Open-Source Actuators for Legged Locomotion
- **Author or organization:** Karthik Urs, Challen Enninful Adu, Elliott J. Rouse, Talia Y. Moore (University of Michigan)
- **Publication date:** 2022-02-24 (arXiv v1)
- **Source type:** Research preprint (full PDF text read)
- **Stable URL or DOI:** https://arxiv.org/abs/2202.12395
- **Evidence label:** Author-measured

## Claims supported

- Stator winding temperature "must be kept below 100 °C to avoid premature winding thermal failure", and is "typically the limiting factor for actuator torque". Cited in [[2.8 - Thermal Management and Energy Budgets|2.8]] §2.8.2, §2.8.4, §2.8.6.
- Two-node thermal model, fitted values (Table 3), fan on and off: winding to housing 0.828 and 1.09 °C/W; housing to air 1.44 and 6.68 °C/W; winding capacity 15.9 and 18.4 J/°C; housing capacity 146 and 138 J/°C; total resistance with fans 2.27 °C/W. Cited in §2.8.2, §2.8.4.
- Fans give "approximately 3.5× cooling advantage"; the reduction "nearly doubles the amount of continuous current that can be safely dissipated". A standing leg holds torque without turning, so "dedicated fans are necessary". Cited in §2.8.3, §2.8.6.
- "A 9.2 A peak may be sustained for 20s or a 22 A peak may be sustained for 2s without exceeding temperature limits." Cited in §2.8.2.
- Winding resistance rose 0.51% per °C, against "common values for pure copper ... of 0.43%/°C"; the motor used as its own thermometer. Cited in §2.8.2.
- Actuator masses 482 g (7.5:1) and 536 g (15:1). Used to scale heat capacity in §2.8.4.

## Test conditions

- **Platform or configuration:** 3D-printed quasi-direct-drive actuators, 7.5:1 planetary and 15:1 Wolfrom, with two 30 x 10 mm centrifugal fans each.
- **Units and measurement boundary:** Winding temperature inferred from line-to-line resistance, calibrated against a thermal camera; ambient 25 °C.
- **Operating conditions:** Random voltage steps held 20 s, one hour from cold, fans on and off.
- **Duration, sample size, denominator:** One actuator per test; a 57 h life test on two actuators.

## Limitations

- A small, plastic research actuator; values do not transfer directly to metal humanoid joints. 2.8 uses them only as a scale reference.

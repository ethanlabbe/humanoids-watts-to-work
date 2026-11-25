---
title: "Nandor 2021 Transmission Comparison for Cooperative Robotic Applications"
type: source
source_type: paper
modified: 2026-11-24
---

[[Source Index]] · [[index|Home]]

- **Title:** Transmission Comparison for Cooperative Robotic Applications
- **Author or organization:** Mark J. Nandor, Maryellen Heebner, Roger Quinn, Ronald J. Triolo, Nathaniel S. Makowski; Case Western Reserve University
- **Publication date:** 2021-08-25 (*Actuators* 10(9), 203); accessed 2026-11-24
- **Source type:** Peer-reviewed journal paper (open access, CC BY)
- **Stable URL or DOI:** https://doi.org/10.3390/act10090203
- **Evidence label:** Author-measured research prototypes

## Claims supported

- Two actuators with the same motor and brake, each 231.8 × 108 × 76.7 mm and 2.1 kg: one with a 50:1 harmonic drive (1:1 chain input), one with a custom two-stage planetary gearbox (5.17:1 and 4.33:1, with a 2.11:1 chain stage, 47.3:1 overall). Cited in [[2.5 - Transmissions and Joint Modules|2.5]] §2.5.3, §2.5.6.
- Isometric torque "3.39 Nm/A" for the planetary against "2.07 Nm/A" for the harmonic; maximum passive resistance 4 N m against 6.5 N m; "the planetary actuator approximately doubled the mechanical efficiency of the harmonic actuator". Cited in §2.5.3, §2.5.6.
- The harmonic test "was stopped at 270 deg/sec due to excessive chain vibration"; the planetary reached the 330 deg/s target. Cited in §2.5.3.
- Harmonic drives give "anywhere from 50:1 to 150:1" and are favoured for "compact design and low backlash"; they need more robust input and output bearings. Background for §2.5.3.

## Test conditions

- **Platform or configuration:** Exoskeleton joint actuators for hybrid gait restoration, not a humanoid.
- **Units and measurement boundary:** Output torque against a fixed load cell (JR3) at zero speed; passive resistance from motor current with the output arm removed.
- **Operating conditions:** Currents 1 to 8 A for isometric tests, extrapolated to the 15 A peak; motor controller 5 A continuous, 15 A peak for 3 to 5 s.
- **Duration, sample size, denominator:** One build of each actuator.

## Limitations

- One build of each design; the harmonic actuator's input chain and bearing arrangement may have contributed to its vibration, as the authors note.
- Maximum torques were extrapolated because the test rig was not stiff enough at high current.

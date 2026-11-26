---
title: "TI SLLA659 Motor Control in Humanoid Robots"
type: source
source_type: vendor material
---

[[Source Index]] · [[index|Home]]

- **Title:** Motor Control in Humanoid Robots (application brief)
- **Author or organization:** Texas Instruments (TI-branded document; no individual author named)
- **Publication date:** Revision SLLA659A, header span January 2025 to June 2026
- **Source type:** Vendor material (semiconductor supplier application brief)
- **Stable URL or DOI:** https://www.ti.com/document-viewer/lit/html/SLLA659
- **Evidence label:** Vendor-reported

## Claims supported

- "typically using 48V nominal voltage with an operating range of approximately 39V to 54V", depending on battery charge state. Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.4 and §2.2.6.
- "Power levels in a humanoid robot can vary from 4kW to 10W, with most of the drives between 10W and 1.5kW." Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.6.
- "Drives typically function within the SELV voltage range, which is below 60V"; "components that operate up to 100V are preferable". Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.3.
- "position updates occurring at 1-4kHz and current regulation exceeding 10kHz"; algorithm choice "FOC or block commutation"; angle sensor accuracy at most 1° for sinusoidal control against 60° for trapezoidal (Table 2); current-sense options and "Multiple encoders may be required for a single motor".
- MOSFET against GaN comparison (Table 3); "GaN FETs offer advantages in temperature-sensitive systems due to minimal switching losses"; higher switching frequency "requires MCU support for high-resolution PWM signaling"; "Temperature management methods must not include additional cooling such as fans or liquids"; exterior below 55 °C. Table 3 cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.3; the cooling limits in §2.3.6.
- At 39 V "a 4kW drive requires approximately 102 A_rms"; "at least CAT3 PLd safety considerations need to be taken for a humanoid robot". Cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.6.
- The interface "is either CAN-FD or Ethernet-based (including EtherCAT)"; daisy-chained and linear bus topologies (Figures 2 and 3); "the minimum bandwidth requirement of communication systems is approximately 8Mbit/s", rising with "system diagnostic and safety capabilities"; bandwidth depends on "how to split the motor control algorithms between the decentralized motor drive, and the centralized and outer robot motion controller". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2, §2.10.4, §2.10.6.
- Example motor-control microcontrollers "functional safety certified for IEC 61508 SIL 3" (AM261x) and SIL 2 (F28P65x). Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.3.

## Test conditions

- **Platform or configuration:** No named platform; a supplier's description of typical humanoid designs.
- **Units and measurement boundary:** Not stated.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Describes typical designs as the supplier sees them, not measured data from a named robot.
- The SELV figure is the supplier's statement; the IEC standards that define SELV could not be read.
- The SIL ratings are TI's claims for its own products, used only to show that certified microcontrollers exist.

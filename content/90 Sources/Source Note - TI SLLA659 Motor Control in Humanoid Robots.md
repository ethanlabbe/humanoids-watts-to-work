---
title: "TI SLLA659 Motor Control in Humanoid Robots"
type: source
source_type: vendor material
modified: 2026-11-22
---

[[Source Index]] · [[index|Home]]

- **Title:** Motor Control in Humanoid Robots (application brief)
- **Author or organization:** Texas Instruments (TI-branded document; no individual author named)
- **Publication date:** Revision SLLA659A, header span January 2025 to June 2026; accessed 2026-11-22
- **Source type:** Vendor material (semiconductor supplier application brief)
- **Stable URL or DOI:** https://www.ti.com/document-viewer/lit/html/SLLA659
- **Evidence label:** Vendor-reported

## Claims supported

- "typically using 48V nominal voltage with an operating range of approximately 39V to 54V", depending on battery charge state. Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.4 and §2.2.6.
- "Power levels in a humanoid robot can vary from 4kW to 10W, with most of the drives between 10W and 1.5kW." Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.6.
- "Drives typically function within the SELV voltage range, which is below 60V"; "components that operate up to 100V are preferable". Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.3.
- "position updates occurring at 1-4kHz and current regulation exceeding 10kHz"; algorithm choice "FOC or block commutation"; angle sensor accuracy at most 1° for sinusoidal control against 60° for trapezoidal (Table 2); current-sense options and "Multiple encoders may be required for a single motor". Loop rates cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.6; the rest is background only since the 2026-11-22 revision.
- MOSFET against GaN comparison (Table 3); "GaN FETs offer advantages in temperature-sensitive systems due to minimal switching losses"; higher switching frequency "requires MCU support for high-resolution PWM signaling"; "Temperature management methods must not include additional cooling such as fans or liquids"; exterior below 55 °C. Table 3 cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.3; the cooling limits in §2.3.6.
- At 39 V "a 4kW drive requires approximately 102 A_rms"; "at least CAT3 PLd safety considerations need to be taken for a humanoid robot". Cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.6.
- Not cited yet, kept for 2.10 (Planned): the interface "is either CAN-FD or Ethernet-based (including EtherCAT)"; "daisy chained communication systems and linear bus topology"; minimum bandwidth "approximately 8Mbit/s".

## Test conditions

- **Platform or configuration:** No named platform; a supplier's description of typical humanoid designs.
- **Units and measurement boundary:** Not stated.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Describes typical designs as the supplier sees them, not measured data from a named robot.
- The SELV figure is the supplier's statement; the IEC standards that define SELV could not be read.
- The PDF version could not be parsed; the HTML version was read.

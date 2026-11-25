---
title: "TI TIDUDS9B Safe Torque Off Reference Design"
type: source
source_type: vendor material
modified: 2026-11-22
---

[[Source Index]] · [[index|Home]]

- **Title:** Design guide TIDUDS9B (reference design TIDA-01599), section 1 "System Description"
- **Author or organization:** Texas Instruments
- **Publication date:** December 2017, revised November 2022; accessed 2026-11-22
- **Source type:** Vendor material (reference design guide)
- **Stable URL or DOI:** https://ti.com/document-viewer/lit/html/TIDUDS9B/GUID-D45B2C6F-497E-49DC-92C8-8FE46481BAA0
- **Evidence label:** Vendor-reported (engineering guidance)

## Claims supported

- "The IEC 61800-5-2 defines STO as a function that prevents torque-producing power from supplying the motor"; it "corresponds to an uncontrolled stop according to stop category 0 of IEC 60204-1". Cited in [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.2.
- "Removing the supply voltage to the gate driver IC disables" the transistors; a "dual-channel architecture (1oo2) with a hardware fault tolerance of 1". Background for [[2.3 - Motor Drives and Power Electronics|2.3]] §2.3.2, not quoted.
- Not cited: assessed by TÜV SÜD as "generally suitable for SIL 3 and PL e | Cat. 3"; diagnostics run by a SIL 1 microcontroller outside the design.

## Test conditions

- **Platform or configuration:** Industrial IGBT inverter reference design; not a robot.
- **Units and measurement boundary:** Not applicable.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Paraphrases IEC 61800-5-2, which could not be read; the library relies on TI's wording.
- The test-pulse and diagnostic sections were not read in full. A companion document (SFFS422) describing the same mechanism was found but is not cited.

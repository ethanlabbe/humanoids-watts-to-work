---
title: "TI SLVAF35A Pre-Charge Power-Up Sequence"
type: source
source_type: vendor material
modified: 2026-11-22
---

[[Source Index]] · [[index|Home]]

- **Title:** White paper SLVAF35A, section 3 "Power-Up Sequence" (products DRV8714-Q1, TPS2HB16-Q1)
- **Author or organization:** Texas Instruments
- **Publication date:** February 2021, revised July 2024; accessed 2026-11-22
- **Source type:** Vendor material (semiconductor supplier white paper)
- **Stable URL or DOI:** https://ti.com/document-viewer/lit/html/SLVAF35A/GUID-C085775C-2E48-4FBD-A54F-2AD18E308CB1
- **Evidence label:** Vendor-reported (engineering guidance)

## Claims supported

- Discharged capacitors cause "a huge inrush current once the main contactors are closed"; "a pre-charge function is mandatory to limit the inrush current during the power-up procedure". Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.
- Four-step sequence: close the main negative contactor, close the pre-charge contactor, close the main positive contactor when the capacitor voltage reaches "90%–95% of battery pack voltage", then open the pre-charge contactor. Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.
- "A contactor combined with a current-limiting resistor is the simplest implementation of the pre-charge function." Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.

## Test conditions

- **Platform or configuration:** Battery system with main and pre-charge contactors; not a robot.
- **Units and measurement boundary:** Not applicable.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Gives no resistor value, time constant, or sizing method; the sizing in 2.2 §2.2.4 is an illustrative estimate.
- The full document title was not shown in the section read.

---
title: "Invertek Drives Braking and Regeneration"
type: source
source_type: vendor material
---

[[Source Index]] · [[index|Home]]

- **Title:** Braking and Regeneration (iKnow knowledge base, article 14)
- **Author or organization:** Invertek Drives Ltd
- **Publication date:** Undated
- **Source type:** Vendor material (drive maker's technical knowledge base)
- **Stable URL or DOI:** https://invertekdrives.com/support/iknow/selection-and-installation/braking-and-regeneration-14
- **Evidence label:** Vendor-reported (engineering guidance)

## Claims supported

- Regenerated energy "charges the capacitor, so the voltage rises"; the rectifier blocks it from returning to the supply. Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.
- An overvoltage trip is "a symptom of too much regeneration". Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.
- A brake resistor is switched by a transistor; this "'chops' the voltage, so it is sometimes called a braking chopper". Cited in [[2.2 - Power Distribution and Protection|2.2]] §2.2.2.
- Not cited: longer deceleration as the easiest remedy; fully regenerative drives justified above about 200 kW; linking drive DC buses.

## Test conditions

- **Platform or configuration:** Industrial AC variable-frequency drives on mains power, not battery robots.
- **Units and measurement boundary:** Not applicable.
- **Operating conditions:** Not applicable.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Written for mains-fed industrial drives; 2.2 notes where a battery robot differs (the battery can absorb regenerated energy when connected).
- A Siemens document on DC-link overvoltage was also found but could not be read (PDF not parseable); nothing from it is used.

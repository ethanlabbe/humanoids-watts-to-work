---
title: "Beckhoff EtherCAT Distributed Clocks"
type: source
source_type: vendor material
---

[[Source Index]] · [[index|Home]]

- **Title:** EtherCAT Distributed Clocks (EtherCAT system documentation)
- **Author or organization:** Beckhoff Automation
- **Publication date:** Undated
- **Source type:** Vendor technical manual
- **Stable URL or DOI:** https://infosys.beckhoff.com/content/1033/ethercatsystem/2469118347.html
- **Evidence label:** Vendor-reported

## Claims supported

- "The EtherCAT master automatically synchronizes each local clock with the reference clock in the EtherCAT system with a precision of < 100 ns". Cited in [[2.9 - Sensors Calibration and Time Synchronization|2.9]] §2.9.2, §2.9.4.
- Each device adds delay, so offsets are measured per device ("It is therefore not appropriate to simply copy the local time of the reference clock"); drift correction handles each oscillator's own rate. Cited in §2.9.2.
- The < 100 ns figure is also used, through a link to 2.9, in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2 and the bus table in §2.10.3.

## Test conditions

- **Platform or configuration:** EtherCAT networks with distributed-clock devices.
- **Units and measurement boundary:** Clock offset between devices.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not stated.

## Limitations

- Vendor documentation; the precision is a design claim, not an independent measurement.

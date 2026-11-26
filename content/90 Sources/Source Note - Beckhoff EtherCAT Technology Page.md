---
title: "Beckhoff EtherCAT Technology Page"
type: source
source_type: vendor material
---

[[Source Index]] · [[index|Home]]

- **Title:** EtherCAT (product and technology page)
- **Author or organization:** Beckhoff Automation (inventor of EtherCAT)
- **Publication date:** Undated
- **Source type:** Vendor technical page
- **Stable URL or DOI:** https://www.beckhoff.com/en-en/products/i-o/ethercat/
- **Evidence label:** Vendor-reported

## Claims supported

- Each device "reads the data addressed to it 'on the fly' and inserts its data in the frame as the frame is moving downstream"; "a single frame is usually sufficient to send and receive control data to and from all nodes"; the frame "is delayed only by hardware propagation delay times". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2.
- 100 Mbit/s transfer rate; effective data rate "more than 90 %". Cited in §2.10.2, §2.10.3, §2.10.4.
- Plain Ethernet example: the shortest frame "is 84 bytes long (including the Inter FrameGap)", so 4 bytes of process data each way gives "4/84 = 4.8 %". Cited in §2.10.3.
- "Line topology is extended to a ring topology for the sake of cable redundancy". Cited in §2.10.3.
- Not cited: Fail Safe over EtherCAT (FSoE) "fulfills the requirements for SIL3 systems"; line, tree and star topologies without switches.

## Test conditions

- **Platform or configuration:** EtherCAT networks in general.
- **Units and measurement boundary:** Link data rate.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- Written by EtherCAT's inventor and a vendor of EtherCAT products; marketing claims such as "by and large the fastest Industrial Ethernet technology" are not used.
- The 1 µs per-device forwarding delay in 2.10 §2.10.4 is not from this page; it is an illustrative estimate.

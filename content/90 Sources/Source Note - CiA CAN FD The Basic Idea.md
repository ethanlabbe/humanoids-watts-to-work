---
title: "CiA CAN FD The Basic Idea"
type: source
source_type: standard
---

[[Source Index]] · [[index|Home]]

- **Title:** CAN FD (flexible data rate): The basic idea
- **Author or organization:** CAN in Automation (CiA), the CAN users' and manufacturers' association
- **Publication date:** Undated
- **Source type:** Standards-body explainer
- **Stable URL or DOI:** https://can-cia.org/can-knowledge/can-fd-the-basic-idea
- **Evidence label:** Standards body explainer

## Claims supported

- In the arbitration phase "the bit rate depends on the network topology and is limited to 1 Mbit/s; in the data phase the bit rate is limited by the transceiver characteristics". Cited in [[2.10 - Embedded Compute and Real-Time Communications|2.10]] §2.10.2.
- CAN FD can "transmit data faster than with 1 Mbit/s and the payload (data field) is now up to 64 byte long and not limited to 8 byte anymore". Cited in §2.10.2.
- "Using a ratio of 1:8 for the bit rates in the arbitration and data phase leads to an approximately six times higher throughput". Cited in §2.10.2, §2.10.3, §2.10.4.
- Standardized with classic CAN in ISO 11898-1:2024. Background only.

## Test conditions

- **Platform or configuration:** Generic CAN FD network.
- **Units and measurement boundary:** Bit rate and throughput relative to classic CAN.
- **Operating conditions:** Not stated.
- **Duration, sample size, denominator:** Not applicable.

## Limitations

- The six-times figure is for a 1:8 bit-rate ratio; other ratios give other gains. The chapter's "at least three buses" for 30 joints uses it as a rough bound, labelled illustrative.

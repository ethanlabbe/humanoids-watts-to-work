---
title: "Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot"
type: source
source_type: paper
---

[[Source Index]] · [[index|Home]]

- **Title:** Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot
- **Author or organization:** Yufeng Chi, Qiayuan Liao, Junfeng Long, Xiaoyu Huang, Sophia Shao, Borivoje Nikolic, Zhongyu Li, Koushil Sreenath; University of California, Berkeley
- **Publication date:** 2025 (Robotics: Science and Systems XXI; arXiv:2504.17249 v1 posted April 2025)
- **Source type:** Peer-reviewed conference paper
- **Stable URL or DOI:** https://doi.org/10.15607/RSS.2025.XXI.062 (open text: https://arxiv.org/abs/2504.17249)
- **Evidence label:** Author-measured research on a named prototype

## Claims supported

- On a custom dynamometer, "the gearbox exhibits a mechanical efficiency of approximately 90% across most operating conditions. However, at high torque and velocity, efficiency decreases due to heat generation." Cited in [[1.4 - How a Humanoid Works - The Full System Map|1.4]] §1.4.2.
- The paper defines *mechanical efficiency* $\eta_{\text{mech}} = P_{\text{mech}} / \lvert \tau_{\text{cmd}}\, \omega_{\text{cmd}} \rvert$ (representing the cycloidal reducer) separately from *total efficiency* $\eta_{\text{total}} = P_{\text{mech}} / P_{\text{elec}}$, which includes "motor copper losses, driver electrical losses, and mechanical losses". Here $P_{\text{mech}} = \tau \omega$ is measured torque times measured speed.
- Cited in [[2.5 - Transmissions and Joint Modules|2.5]] §2.5.5, §2.5.6 (not in 1.4): a 60-hour durability test lifted a 0.5 kg, 0.5 m pendulum from −45° to +90° at 0.5 Hz. Efficiency "initially declined but later returned to near its original level"; backlash "increased slightly" with wear of 3D-printed parts.

- "The robot weighs 16 kg and stands 0.8 m tall"; "two 5-DOF arms and integrated grippers"; joints driven by two sizes of actuator with 3D-printed cycloidal gearboxes and brushless drone motors. Cited in [[1.2 - What Is a Humanoid Robot|1.2]] §1.2.2, and in [[2.6 - Mechanical Architecture and Structures|2.6]] §2.6.3, §2.6.6 for its largely 3D-printed structure.

- "The M6C12 150KV BLDC drone motor from MAD Components is used to drive the actuator" (larger 6512 actuator); actuator parts cost USD 188 (6512) and USD 136 (5010) at US prices (Tables I, II); total hardware cost under USD 5,000 "(based on U.S. market prices)"; gearbox efficiency about 90% (above). Cited in [[2.4 - Motors and Actuator Selection|2.4]] §2.4.4, §2.4.6.

## Test conditions

- **Platform or configuration:** Berkeley Humanoid Lite actuators (6512 and 5010 motor variants) with 3D-printed cycloidal gearboxes.
- **Units and measurement boundary:** Torque from two load cells; electrical input from supply voltage and current; mechanical power = torque × measured velocity.
- **Operating conditions:** Actuator in torque-control mode against a velocity-controlled damping actuator; three speeds "that correspond to its typical operating range on the robot"; each command held 1 s before measurement.
- **Duration, sample size, denominator:** Efficiency sweep per actuator; durability: one actuator, 60 h, measured hourly for 12 h then every 12 h.

## Limitations

- Low-cost 3D-printed actuators; numbers do not transfer to other actuator designs.
- Steady-state points only; no whole-robot or task-level energy.
- The 60 h test is a component bench test, not field reliability.
- Exact total-efficiency values are in Figure 8 and were not transcribed here.

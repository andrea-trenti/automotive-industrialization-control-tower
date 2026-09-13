# Interview Talking Points

## 1. Problem

A deterministic Gantt/CPM plan can look safe while hiding common-cause risk, supplier slippage, specialist-resource scarcity and commissioning rework. I wanted to test whether a launch commitment still looked credible after modeling those mechanisms explicitly.

## 2. Why deterministic CPM failed

The deterministic network placed SOP at **day 636**. Once I introduced correlated schedule risk, explicit supplier/FAT/SAT failures, renewable-resource constraints and individual specialist calendars, the baseline moved to **P80 = 766 days** with only **70.9%** modeled probability of meeting the committed SOP at day 751.

The important point is not that CPM is “wrong”; it answers a different question. CPM gives the deterministic network plan. The probabilistic model estimates launch-date risk conditional on uncertainty and capacity constraints.

## 3. Technical architecture

The workflow is:

**project network / CPM → correlated Monte Carlo → RCPSP + resource calendars → supplier readiness → FAT/SAT → commissioning state machine + rework → hard readiness gates → mitigation/crashing economics → stress testing + fresh-seed out-of-sample validation.**

The program contains **720 activities, 1,102 dependencies, 42 suppliers, 144 equipment assets and 320 quantified risks**.

## 4. Most important falsification

My first question was whether the deterministic commitment survived a more realistic model. It did not: baseline **P80 reached 766 days**, beyond the committed day 751. I kept that negative result instead of adjusting assumptions to preserve the original plan.

A second useful negative result was that generic resource uplift alone had almost no benefit. The model only improved materially when mitigation targeted supplier/FAT/change-control and high-criticality schedule paths.

## 5. Target+ decision

The final Target+ package reduced **P80 from 766 to 713 days** and raised modeled **P(on-time) from 70.9% to 95.4%** for approximately **€1.58M** incremental synthetic mitigation cost. A fresh-seed unseen-scenario run returned **P80 = 714** and **95.1%** on-time probability, so the decision was not dependent on one random seed.

The largest remaining technical vulnerability is automation debug. A **+35% debug-duration** shock pushes P80 to **823 days** and P(on-time) to **31.5%**. The main modeled driver is software debugging (**36%** of tail exposure), followed by PLC/I-O (**27%**). The first mitigation I would test operationally is pre-commission software emulation/freeze.

## 6. Main limitation

Everything numerical is synthetic. The project demonstrates architecture, methods, falsification and decision logic; it does **not** claim Ferrari/OEM launch experience or empirical plant calibration. Real use would require historical schedule data, named-resource calendars, supplier milestones, FAT/SAT/rework histories, commissioning issues, QMS/CMMS data and finance-approved delay-cost assumptions.

## 60-second version

“I built a synthetic automotive industrialization control tower to test whether a deterministic launch plan stays credible once real launch mechanisms are represented. The program has 720 activities, 1,102 dependencies, 42 suppliers and 144 equipment assets. Deterministic CPM put SOP at day 636, but after correlated risk, supplier/FAT/SAT failures and resource constraints, baseline P80 moved to day 766 and on-time confidence fell to 70.9%. I then evaluated targeted mitigation rather than uniform schedule compression. The final Target+ policy reduced P80 to 713 and raised on-time confidence to 95.4% for about €1.58M modeled incremental cost, and a fresh-seed validation reproduced the result. The largest remaining failure mode was automation debug, which is why I would prioritize pre-commission software emulation and freeze. The key limitation is that the data are synthetic, so I present it as a research-grade engineering study, not as real OEM launch management.”

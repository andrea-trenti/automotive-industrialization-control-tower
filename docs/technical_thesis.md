# New Vehicle Industrialization & Commissioning Control Tower

## Abstract

This report documents a research-grade synthetic automotive industrialization and commissioning study built to test launch-date credibility rather than visualize a project plan. The synthetic program contains 720 activities, 1102 precedence relationships, 42 suppliers, 144 equipment assets and 320 quantified risks. Deterministic CPM places the synthetic SOP at day 636. After correlated schedule risk, explicit supplier/FAT/SAT events, renewable resources and individual specialist calendars are introduced, the baseline shifts to P50/P80/P90 = 723/766/786 days and P(on-time) = 70.9%. A targeted Target+ mitigation policy reduces P80 to 713 days and raises P(on-time) to 95.4% for EUR 1.580m modeled incremental mitigation cost. The final-pass work concentrates on resource-calendar realism, exact subproblem verification, stable Monte Carlo stress testing, automation-debug decomposition, mitigation efficiency, fresh-seed robustness, forecast backtesting, readiness consistency, cost-of-delay sanity and numerical consistency. The framework is synthetic and not empirically calibrated to any OEM plant.

## Research Questions

1. How materially does deterministic CPM understate tail launch risk once common-cause uncertainty and resource scarcity are represented?
2. Which mitigation actions produce the largest increase in on-time launch confidence per unit cost and per expected P80 day saved?
3. Why does automation-debug risk dominate the adverse tail and which technical intervention produces the greatest recovery?
4. Do individual specialist calendars materially change the ranking of launch interventions or merely refine the forecast?
5. Does the probabilistic forecast become better calibrated and more accurate as the program approaches SOP?
6. Can readiness and schedule-risk outputs be governed so that a high aggregate score cannot hide failed launch-stopping gates?

## 1. Automotive Industrialization Context

A new-vehicle industrialization program is not simply a project-management schedule. It is a coupled technical system in which product engineering releases condition tooling and equipment design; supplier tooling and sample-part maturity condition process validation; FAT outcomes condition shipment; installation and utilities condition SAT; commissioning debug conditions capability; quality and workforce readiness condition run-at-rate; and all of those flows condition SOP. The model therefore treats schedule, resources, equipment state, supplier evidence, readiness gates and launch economics as one decision system.

The governing principle is decision usefulness. A method is retained only when it can alter at least one of the following: launch-date forecast, tail risk, mitigation ranking, bottleneck identification, cost exposure, or model credibility. This final-pass rule intentionally removes the incentive to add algorithms for cosmetic sophistication.

## 2. Scope and Synthetic Data Model

The system includes twelve workstreams: Product Engineering, Manufacturing Engineering, Tooling, Equipment, Supplier Industrialization, Facility, Commissioning, Quality, Workforce, Logistics, Ramp-Up and Launch. Activities form a directed acyclic graph. Supplier, equipment, resource and risk tables are separate but connected to the schedule through synthetic keys and risk logic. The data are designed to be structurally plausible rather than statistically representative of Ferrari or any other OEM.

Source provenance is classified conceptually into five classes: A empirical plant data, B external industrial data, C peer-reviewed or standards-based methodology, D engineering assumption, and E purely synthetic scenario parameter. In this repository, most numerical parameters are D or E. Public sources support the methodology, not the numerical values.

## 3. Work Breakdown Structure and Network Logic

The project network is defined as G=(V,E), where V is the set of activities and E the set of precedence relations. Every activity has a workstream, owner, planned duration, cost, risk category and readiness category. The generated network contains exactly 1,102 precedence links and is checked for acyclicity before analysis. This matters because schedule-risk calculations are invalid if hidden loops or orphan logic are present.

For deterministic CPM, earliest start ES_i and earliest finish EF_i are computed recursively. For a predecessor set P(i), ES_i=max(EF_j) for j in P(i), and EF_i=ES_i+d_i. Deterministic makespan to SOP is the maximum finish across activities required by the SOP milestone. Post-SOP stabilization is intentionally excluded from the launch-date objective.

## 4. Deterministic CPM Baseline and Falsification Logic

The deterministic SOP is day 636, while the full post-SOP program closes at day 658. This distinction was explicitly protected by regression tests because an earlier version of the analysis used post-SOP completion as a proxy for launch. That error would have overstated launch risk and contaminated economics. The final release therefore separates launch from stabilization throughout CPM, stochastic simulation and cost calculations.

The deterministic result is not presented as a forecast. It is a logical lower-information baseline. Its role is to be falsified. The central falsification experiment progressively adds uncertainty, common-cause risks, explicit launch failures and resource constraints. The schedule moves from a point estimate that appears fully safe to a tail-risk distribution that makes the commitment non-credible at a P80 confidence level.

## 5. Stochastic Duration and Correlated Risk Model

Activity durations are treated as uncertain rather than fixed. The conceptual implementation is compatible with Beta-PERT-style parameterization using optimistic, most-likely and pessimistic durations. However, the important final-pass issue is not the marginal distribution alone; it is dependence. Engineering-change waves, supplier disruption, software maturity, facility access and commissioning productivity can jointly influence many activities. Assuming independent durations would therefore create false diversification.

The repository represents these common drivers through correlated latent risk factors and explicit discrete events. The ablation results show why the distinction matters. Independent duration uncertainty alone increases P80 only modestly. Correlated latent risk increases the tail more materially. Explicit engineering/supplier/FAT/SAT failures add another step. Renewable resource constraints then create the largest final shift in the baseline.

## 6. Resource-Constrained Scheduling and Individual Calendars

The final improvement pass adds specialist-specific calendars rather than replacing the RCPSP architecture. Resources have skill categories, Monday-Friday working patterns, planned unavailable periods and availability factors. The purpose is not to model every person in a real plant; it is to test whether pooled-capacity assumptions materially understate launch risk.

The result is decision-relevant but controlled. Baseline P80 moves from 761 to 766 days and Target+ from 709 to 713 days. The ranking of mitigation actions does not change. This supports retaining individual calendars while rejecting a more elaborate fatigue/learning/shift micro-model, which would increase parameter burden without changing the launch decision under current synthetic evidence.

## 7. Exact Scheduling Verification Benchmark

The production scheduler is not replaced by a computationally expensive exact model. Instead, a small 14-task, two-resource time-indexed RCPSP is solved with SciPy/HiGHS as a verification benchmark. Binary variable x_it indicates that activity i starts at time t. Each task starts once; precedence constraints enforce start_j >= start_i + d_i; time-indexed resource constraints cap simultaneous consumption. The solver returns an optimal solution with zero MIP gap. This benchmark verifies basic resource-feasibility and optimization logic without claiming that the full 720-activity program is solved exactly.

The exact benchmark is intentionally small because exact time-indexed RCPSP grows rapidly with horizon and task count. Its value is verification, not production-scale planning.

## 8. Supplier Industrialization and Dependency Risk

Supplier readiness is not a simple average score. The model distinguishes supplier risk from supplier criticality. A supplier may have a moderate delay probability but become strategically important if it is single-source, feeds several critical component families or blocks multiple commissioning paths. Conversely, a supplier with weak local metrics may have limited launch consequence if alternatives exist and the affected material has float.

Delay shocks of +2, +4 and +6 weeks are propagated into the schedule and show monotonic deterioration after the final Monte Carlo stability pass. This corrects an earlier noisy ordering and demonstrates that the stress model behaves directionally as engineering judgment would expect.

## 9. FAT, SAT and Commissioning State Physics

Equipment commissioning is modeled as a state machine rather than a checklist. Valid states are Not Delivered, Delivered, Installed, Powered, I/O Checked, Dry Run, SAT, Debug, Capability and Released. Rework loops are permitted where physically meaningful, especially SAT-to-Debug and Debug-to-SAT. Invalid transitions are automatically rejected in tests.

This structure matters because FAT or SAT failure creates actual schedule work: diagnosis, correction, retest and delayed release. Commissioning issues can therefore alter both path timing and resource demand. The model remains synthetic but reproduces the logic necessary for a launch control tower to be operationally credible.

## 10. Automation-Debug Tail-Risk Decomposition

Automation debug is the strongest residual single shock in the final stress screen. A +35% automation-debug duration increases P80 SOP to 823 days and reduces on-time confidence to 31.5%. To make that risk actionable, the final pass decomposes tail exposure into software debugging (36%), PLC/I-O integration (27%), robot integration (18%), vision integration (12%) and mechanical correction (7%).

This decomposition converts a generic commissioning risk into engineering interventions. The strongest modeled response is pre-commission software emulation and release freeze, followed by PLC dry-I/O validation. These interventions are not presented as universal OEM benchmarks; they are scenario-specific decision alternatives whose relative effectiveness can later be calibrated with real issue histories.

## 11. Readiness Architecture and Hard Gates

The aggregate launch-readiness index is 0.755, but status remains RED. This is deliberate. A weighted average is compensatory: excellent training or logistics could numerically offset a failed critical FAT, missing supplier approval or unreleased equipment. That is not acceptable for launch authorization.

The final framework therefore separates continuous readiness evidence from non-compensatory hard gates. Any failed critical gate forces RED. Current failed gates are critical commissioning issues, critical supplier approval and critical equipment release. Tests explicitly verify that even a 0.99 aggregate score remains RED if a hard gate fails.

## 12. Mitigation Frontier and Efficiency

The mitigation frontier compares actions using incremental cost, change in on-time probability and P80 days saved. The baseline is 70.9% on-time with P80 766. Calendar-aware generic resource uplift costs EUR 640k but changes confidence only marginally and saves approximately one P80 day. Supplier mitigation improves confidence and schedule modestly. Early FAT/change control creates the first large gain. Selective crashing then completes Target+.

Two efficiency metrics are reported: probability-point gain per EUR 100k and cost per P80 day saved. These are intentionally transparent and do not claim to be universal economic measures. They depend on the commitment date and chosen risk model. Their purpose is to expose low-value interventions such as indiscriminate resource addition.

## 13. Target+ Out-of-Sample Robustness

The final Target+ schedule uses the same policy structure as the prior release: targeted supplier mitigation, early FAT/change control, commissioning-risk reduction and selective crashing. It is not re-optimized to the final random seed. A fresh-seed check produces P50/P80/P90 = 679/714/735 and P(on-time) = 95.1%, close to the reported release result of 678/713/734 and 95.4%.

This difference is small enough to support robustness while still acknowledging Monte Carlo variability. The fresh-seed estimate includes an on-time probability Monte Carlo standard error of approximately 0.62 percentage points.

## 14. Stress Testing and Resilience Envelope

The final stress screen focuses only on scenarios that can change the launch decision. Supplier delay +2/+4/+6 weeks produces P80 values 726/739/752 and on-time confidence 93.8%/86.4%/79.7%. Critical FAT failure yields P80 761 and 74.6%. A 20% commissioning-resource loss yields P80 744 and 84.2%. Automation debug +35% yields 823 and 31.5%. The combined stress reaches P80 856 with only 17.6% on-time confidence.

Monte Carlo error is recorded for these stress outputs. The purpose is not to claim exact confidence limits from synthetic inputs; it is to demonstrate that scenario ordering is stable enough to support mitigation ranking.

## 15. Ramp-Up and Quality Validation

SOP is not equivalent to nominal production rate. The broader project architecture therefore retains ramp-up, quality stabilization and post-launch monitoring as separate processes after the launch milestone. In a real deployment, run-at-rate would combine throughput, availability, first-pass yield, capability and unresolved critical issue criteria. Process capability metrics such as Cp/Cpk are meaningful only after stability and distribution assumptions are checked. Synthetic MSA is treated as a screening layer rather than validated metrology.

The final release does not add more quality algorithms because they do not alter the current launch mitigation ranking. This is an example of complexity pruning.

## 16. Forecast Backtesting and Probability Calibration

Forecast quality is evaluated at T-24, T-16, T-12, T-8 and T-4 weeks relative to SOP. Synthetic MAE improves from 26.3 to 23.5, 20.7, 15.2 and 9.9 days. Bias decreases from 4.8 to 0.4 days. P80 coverage remains near 81-84%, close to the intended nominal level.

This pattern demonstrates a useful control-tower property: as engineering, supplier and commissioning evidence accumulates, the forecast should become more accurate and less biased. The result is synthetic calibration evidence, not proof that the model would be calibrated on a real OEM launch.

## 17. Cost-of-Delay Sanity and Integrated Economics

The cost model intentionally excludes selling price as a direct delay cost. Selling price is not economic contribution. Conservative, base and stress scenarios instead separate contribution-margin effects, capacity-value effects and expediting/containment effects. The model also tags provenance: some methodology is literature/external, while cost levels and shares are engineering assumptions or purely synthetic parameters.

Target+ is not forced to generate positive expected-cost ROI. Expected total project cost is slightly higher because mitigation is purchased. The economic value is primarily tail-risk reduction: modeled P80 cost decreases, CVaR95 falls from EUR 112.4m to EUR 106.2m and expected delay cost falls from EUR 1.55m to EUR 0.14m. This is a more defensible management framing than claiming that all acceleration spend automatically creates profit.

## 18. Numerical Consistency and Single Source of Truth

All release-level numbers are stored in outputs/core_results.json and supporting CSV tables. The README is tested against those values. The FINAL_QA_REPORT is generated from the same artifacts. This reduces the risk of a common portfolio failure: attractive figures and prose that no longer match the actual model outputs after a late correction.

The final release uses one source tree. FULL is the master archive. GITHUB is derived from it by removing only regenerable large raw data. No manual rewriting of results is permitted between packages.

## 19. Complexity Pruning

The final audit considered, but rejected, additional Tier-2 supplier networks, detailed worker fatigue, deep-learning risk predictors, extra metaheuristics and more elaborate readiness weighting. None had enough synthetic evidence to change the current decision. Adding them would increase identifiability risk and explanation burden while reducing auditability.

The retained model therefore aims to be deep but controlled. Its technical complexity is concentrated where it changes forecast credibility, mitigation choice or validation strength.

## 20. Verification, Validation and VVUQ Boundary

Verification includes DAG validity, CPM logic, SOP versus post-SOP separation, quantile ordering, resource feasibility, commissioning transitions, readiness gates, reproducibility, crashing/economic consistency and numerical consistency. Exact small-RCPSP optimization provides an additional calculation benchmark.

Validation is synthetic. Fresh random seeds, rolling-origin backtests, probability coverage and directional stress behavior test whether the framework behaves consistently with its own data-generating process. No historical OEM launch records are available, so empirical calibration, predictive external validation and decision-performance validation remain open.

## 21. Industrial Data Requirements

A production implementation would require at minimum: actual and planned activity start/finish timestamps; predecessor logic; named-resource skill and calendar data; engineering-change release history; supplier tooling/sample/capacity gates; FAT test dates, failures and rework; shipment/install/SAT timestamps; commissioning issue opening/closure/reopen histories; quality capability and MSA data; training/qualification matrices; run-at-rate measurements; and finance-approved delay-cost definitions.

The highest-value datasets for reducing current epistemic uncertainty are named-resource calendars, automation-debug issue histories, supplier gate slippage, FAT/SAT rework distributions and actual delay-cost decomposition.

## 22. Limitations

The network, distributions, correlations, resources, suppliers, risk rates, costs and mitigation effects are synthetic. They provide a controlled environment for demonstrating methods, not factual evidence about Ferrari or another OEM. The exact benchmark covers a small subproblem only. Stress-test confidence reflects simulation error conditional on assumed parameters, not model-form uncertainty. Readiness weights and economic decomposition still require empirical elicitation. Scientific novelty is limited because the project integrates established methods rather than proposing a new scheduling theory.

## 23. Final Assessment

The strongest supported classification is research-grade synthetic automotive industrialization and commissioning study. The project demonstrates professional industrialization logic, operations research, stochastic schedule risk, commissioning realism, resource constraints, supplier dependencies, risk-based economics, verification and decision-centric reporting. It includes methodological sophistication associated with graduate research but is not a validated plant model and is not a publishable PhD contribution without empirical data and a novel scientific claim.

## Appendix A. Model Ablation

| model                                        |   p50 |   p80 |   p90 |   on_time_probability |
|:---------------------------------------------|------:|------:|------:|----------------------:|
| Deterministic CPM                            |   636 |   636 |   636 |                 1     |
| CPM + independent uncertainty                |   645 |   653 |   657 |                 1     |
| + correlated latent risks                    |   645 |   681 |   701 |                 0.99  |
| + explicit engineering/supplier/FAT/SAT risk |   667 |   709 |   733 |                 0.948 |
| + resource constraints + calendars           |   723 |   766 |   786 |                 0.709 |
| Target+ OOS + calendars                      |   678 |   713 |   734 |                 0.954 |

## Appendix B. Resource Calendar Impact

| scenario                      |   p50 |   p80 |   p90 |   on_time_probability |
|:------------------------------|------:|------:|------:|----------------------:|
| Baseline old pooled calendars |   719 |   761 |   781 |                 0.757 |
| Baseline individual calendars |   723 |   766 |   786 |                 0.709 |
| Target+ old pooled calendars  |   675 |   709 |   730 |                 0.967 |
| Target+ individual calendars  |   678 |   713 |   734 |                 0.954 |

## Appendix C. Mitigation Efficiency

| plan                           |   incremental_cost_eur |   on_time_probability |   p80_sop |   p80_days_saved |   delta_on_time_probability |   probability_points_per_100k |   cost_per_p80_day_saved |
|:-------------------------------|-----------------------:|----------------------:|----------:|-----------------:|----------------------------:|------------------------------:|-------------------------:|
| Baseline                       |                      0 |                 0.709 |       766 |                0 |                       0     |                       nan     |                    nan   |
| Resource calendar-aware uplift |                 640000 |                 0.712 |       765 |                1 |                       0.003 |                         0.047 |                 640000   |
| + Supplier mitigation          |                1040000 |                 0.745 |       758 |                8 |                       0.036 |                         0.346 |                 130000   |
| + Early FAT/change control     |                1560000 |                 0.896 |       731 |               35 |                       0.187 |                         1.199 |                  44571.4 |
| Target+ + selective crashing   |                1579799 |                 0.954 |       713 |               53 |                       0.245 |                         1.551 |                  29807.5 |

## Appendix D. Stable Stress Tests

| stress                       |   p80_sop |   on_time_probability |   p80_mc_se_days |
|:-----------------------------|----------:|----------------------:|-----------------:|
| Supplier delay +2 weeks      |       726 |                 0.938 |              1.4 |
| Supplier delay +4 weeks      |       739 |                 0.864 |              1.6 |
| Supplier delay +6 weeks      |       752 |                 0.797 |              1.8 |
| Critical FAT failure         |       761 |                 0.746 |              1.9 |
| Commissioning resources -20% |       744 |                 0.842 |              1.7 |
| Automation debug +35%        |       823 |                 0.315 |              2.1 |
| Combined stress              |       856 |                 0.176 |              2   |

## Appendix E. Automation Debug Decomposition

| component             |   tail_risk_share |   mitigation_cost_eur |   p80_days_recovered |   delta_on_time_probability |   cost_per_p80_day_recovered |
|:----------------------|------------------:|----------------------:|---------------------:|----------------------------:|-----------------------------:|
| Software debugging    |              0.36 |                240000 |                   22 |                       0.108 |                      10909.1 |
| PLC/I-O integration   |              0.27 |                120000 |                   11 |                       0.056 |                      10909.1 |
| Robot integration     |              0.18 |                150000 |                    8 |                       0.043 |                      18750   |
| Vision integration    |              0.12 |                 90000 |                    5 |                       0.027 |                      18000   |
| Mechanical correction |              0.07 |                 75000 |                    3 |                       0.013 |                      25000   |

## Appendix F. Forecast Backtesting

|   weeks_to_sop |   mae_days |   bias_days |   p80_coverage |
|---------------:|-----------:|------------:|---------------:|
|            -24 |       26.3 |         4.8 |          0.814 |
|            -16 |       23.5 |         3.2 |          0.822 |
|            -12 |       20.7 |         2   |          0.828 |
|             -8 |       15.2 |         1.1 |          0.836 |
|             -4 |        9.9 |         0.4 |          0.824 |

## Appendix G. Financial Results

| scenario   |   expected_total_cost_meur |   p80_cost_meur |   p95_cost_meur |   cvar95_meur |   expected_delay_cost_meur |
|:-----------|---------------------------:|----------------:|----------------:|--------------:|---------------------------:|
| Baseline   |                      89.18 |            95.8 |             106 |         112.4 |                       1.55 |
| Target+    |                      89.24 |            95.2 |             102 |         106.2 |                       0.14 |

## Appendix H. Reproducibility

Run `python pipeline.py` and then `pytest -q`. The release gate requires zero failures. The package manifest records final file hashes.

## Appendix I. Decision Figures

### Schedule-risk distribution

![Baseline versus Target+ schedule-risk distribution](../figures/schedule_risk_distribution.png)

### Mitigation frontier

![Mitigation cost versus on-time probability](../figures/mitigation_frontier.png)

### Automation-debug tail-risk decomposition

![Automation debug risk decomposition](../figures/automation_debug_risk.png)

### Stable stress screen

![P80 under final stress scenarios](../figures/stress_tests.png)

### Rolling forecast backtest

![Forecast MAE versus weeks before SOP](../figures/forecast_backtest.png)

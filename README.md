# New Vehicle Industrialization & Commissioning Control Tower

> **Research-grade synthetic automotive industrialization and commissioning study**  
> **Release:** `v1.0.1` — portfolio presentation polish only; validated model results unchanged.

A quantitative launch-control framework for testing whether an automotive industrialization plan is actually credible once correlated risk, scarce engineering resources, supplier readiness, FAT/SAT rework and commissioning uncertainty are represented.

**Synthetic disclaimer:** no Ferrari or other OEM plant/launch data are used. This is not a digital twin, empirical plant model, or validated OEM forecast.

## 30-second view

| Program scale | Validated release result |
|---|---:|
| Activities | **720** |
| Dependencies | **1,102** |
| Suppliers | **42** |
| Equipment assets | **144** |
| Quantified risks | **320** |
| Deterministic SOP | **636 workdays** |
| Baseline P80 SOP | **766 workdays** |
| Target+ P80 SOP | **713 workdays** |
| P(on-time) | **70.9% → 95.4%** |
| Modeled Target+ mitigation cost | **€1.58M** |

![Launch credibility: deterministic CPM vs stochastic baseline vs Target+](figures/portfolio_hero.png)

**Decision:** which targeted mitigations most efficiently restore launch confidence without pretending that the deterministic CPM date is a probabilistic forecast?

[Technical thesis](docs/technical_thesis.pdf) · [Interview talking points](INTERVIEW_TALKING_POINTS.md) · [CV bullets](docs/cv_bullets.md) · [Final QA](FINAL_QA_REPORT.md) · [GitHub metadata](docs/github_metadata.md)

## Problem

Deterministic CPM captures network logic, but it can materially understate launch risk when activities share common risk drivers, specialist capacity is finite, suppliers slip, FAT/SAT generates rework and commissioning does not follow a perfectly linear path.

The core falsification is deliberate: the deterministic plan places SOP at **day 636**, but the final stochastic, resource-constrained baseline shifts to **P80 = 766**, beyond the synthetic committed SOP at day **751**. The Target+ policy reduces P80 to **713** and raises P(on-time) from **70.9% to 95.4%**.

| Model | P50 | P80 | P90 | P(on-time) |
|---|---:|---:|---:|---:|
| Deterministic CPM | 636 | 636 | 636 | point plan |
| + independent uncertainty | 645 | 653 | 657 | 100.0% |
| + correlated latent risks | 645 | 681 | 701 | 99.0% |
| + explicit engineering/supplier/FAT/SAT risk | 667 | 709 | 733 | 94.8% |
| + resources + individual calendars | **723** | **766** | **786** | **70.9%** |
| Target+ OOS + calendars | **678** | **713** | **734** | **95.4%** |

## Architecture

```text
Synthetic program data
        ↓
Project network / CPM
        ↓
Correlated stochastic schedule risk
        ↓
RCPSP + individual specialist calendars
        ↓
Supplier readiness + equipment FAT/SAT
        ↓
Commissioning state machine + rework
        ↓
Hard launch-readiness gates
        ↓
Crashing / mitigation economics
        ↓
Stress testing + fresh-seed OOS validation
        ↓
Decision-ready launch forecast
```

Repository structure:

```text
src/            quantitative core
data/           synthetic full/sample datasets
configs/        scenario configuration
outputs/        single-source validated decision tables
figures/        recruiter- and decision-facing figures
tests/          unit/integration/invariant/regression tests
docs/           thesis, methodology, validation and governance
dashboard/      lightweight Streamlit control tower
experiments/    provenance and release manifests
```

## Methods and technical credibility

The final model combines:

**Monte Carlo correlated schedule risk** · **RCPSP** · **individual resource calendars** · **supplier/equipment dependencies** · **FAT/SAT rework** · **commissioning state machine** · **hard readiness gates** · **selective crashing / mitigation economics** · **stress testing** · **fresh-seed out-of-sample validation** · **rolling synthetic forecast backtesting**.

A small exact RCPSP subproblem is solved with SciPy/HiGHS as a verification benchmark; it does **not** replace the scalable full-program scheduler. Individual specialist calendars add **5 days** to baseline P80 and **4 days** to Target+ P80 versus pooled calendars, enough to retain but not enough to justify a more elaborate workforce microsimulation.

## Key results

### Target+ decision

The final Target+ configuration reduces P80 by **53 workdays** and improves modeled on-time confidence by **24.5 percentage points**, at approximately **€1.58M** incremental modeled mitigation cost.

Fresh-seed unseen-scenario validation remains close to the release result:

**Target+ fresh seed:** P50 **679**, P80 **714**, P90 **735**, P(on-time) **95.1%**.

### Mitigation efficiency

The project preserves a useful negative result: generic resource uplift by itself creates almost no improvement. The larger gain appears only after targeted supplier, FAT/change-control and selective crashing interventions.

| Plan | Incremental cost | P80 | P80 days saved | P(on-time) |
|---|---:|---:|---:|---:|
| Baseline | €0 | 766 | 0 | 70.9% |
| Resource calendar-aware uplift | €0.64M | 765 | 1 | 71.2% |
| + Supplier mitigation | €1.04M | 758 | 8 | 74.5% |
| + Early FAT/change control | €1.56M | 731 | 35 | 89.6% |
| **Target+ + selective crashing** | **€1.58M** | **713** | **53** | **95.4%** |

![Mitigation frontier](figures/mitigation_frontier.png)

## Stress failure: automation debug

The strongest residual single failure mode is **automation debug +35%**:

**P80 = 823 days** · **P(on-time) = 31.5%**

Modeled tail-risk decomposition:

| Debug component | Tail-risk share |
|---|---:|
| Software debugging | **36%** |
| PLC / I-O integration | **27%** |
| Robot integration | **18%** |
| Vision integration | **12%** |
| Mechanical correction | **7%** |

The highest-value focused intervention is **pre-commission software emulation/freeze**: modeled at **€240k**, approximately **22 P80 days recovered** and **+10.8 pp** on-time confidence in the focused scenario.

![Automation-debug tail risk](figures/automation_debug_risk.png)

## Final stress screen

| Shock | P80 | P(on-time) |
|---|---:|---:|
| Supplier delay +2 weeks | 726 | 93.8% |
| Supplier delay +4 weeks | 739 | 86.4% |
| Supplier delay +6 weeks | 752 | 79.7% |
| Critical FAT failure | 761 | 74.6% |
| Commissioning resources −20% | 744 | 84.2% |
| Automation debug +35% | 823 | 31.5% |
| Combined stress | 856 | 17.6% |

## Forecast quality

Synthetic rolling backtesting shows the forecast tightening as SOP approaches:

| Horizon | MAE | Bias | P80 coverage |
|---|---:|---:|---:|
| T−24 weeks | 26.3 d | +4.8 d | 81.4% |
| T−16 | 23.5 d | +3.2 d | 82.2% |
| T−12 | 20.7 d | +2.0 d | 82.8% |
| T−8 | 15.2 d | +1.1 d | 83.6% |
| T−4 | **9.9 d** | **+0.4 d** | 82.4% |

## Economics

Target+ is not presented as an automatic ROI generator. Expected total cost is slightly higher because mitigation is purchased deliberately. The value is primarily tail-risk reduction: modeled **CVaR95 falls from €112.4M to €106.2M** and expected delay cost from **€1.55M to €0.14M**.

Selling price is explicitly excluded from delay-cost logic. Contribution margin, capacity value and expediting/containment assumptions are separated and provenance-labeled.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python pipeline.py
pytest -q
streamlit run dashboard/app.py
```

Expected smoke-test result for this release: **35 passed, 0 failed**.

## Repository guide

| Resource | Purpose |
|---|---|
| [`docs/technical_thesis.pdf`](docs/technical_thesis.pdf) | Final technical thesis |
| [`docs/technical_thesis.md`](docs/technical_thesis.md) | Source thesis |
| [`INTERVIEW_TALKING_POINTS.md`](INTERVIEW_TALKING_POINTS.md) | Concise recruiter/interview narrative |
| [`docs/cv_bullets.md`](docs/cv_bullets.md) | Two quantified, synthetic-safe CV bullets |
| [`docs/github_metadata.md`](docs/github_metadata.md) | Repository description, topics and pinning guidance |
| [`docs/project_network_methodology.md`](docs/project_network_methodology.md) | CPM/network methodology |
| [`docs/stochastic_schedule_risk.md`](docs/stochastic_schedule_risk.md) | Schedule-risk formulation |
| [`docs/resource_optimization.md`](docs/resource_optimization.md) | Resource/RCPSP logic |
| [`docs/supplier_readiness_framework.md`](docs/supplier_readiness_framework.md) | Supplier dependency/readiness logic |
| [`docs/commissioning_framework.md`](docs/commissioning_framework.md) | FAT/SAT/commissioning state logic |
| [`docs/launch_readiness_methodology.md`](docs/launch_readiness_methodology.md) | Hard-gated readiness |
| [`docs/economic_model.md`](docs/economic_model.md) | Cost and mitigation economics |
| [`docs/validation_report.md`](docs/validation_report.md) | Verification/validation boundary |
| [`docs/industrial_data_requirements.md`](docs/industrial_data_requirements.md) | Data required for real industrial calibration |
| [`FINAL_QA_REPORT.md`](FINAL_QA_REPORT.md) | Release smoke test and package QA |

## Limitations

This is a **research-grade synthetic automotive industrialization and commissioning study**. Code verification, calculation checks, synthetic parameter recovery and unseen-scenario validation are supported; empirical launch calibration is not.

Industrial use would require real scheduling-system histories, PLM engineering changes, named-resource calendars, supplier milestones, FAT/SAT/rework logs, commissioning issue histories, QMS/CMMS evidence and finance-approved delay-cost data. The project demonstrates the engineering framework and decision logic, not actual OEM launch performance.

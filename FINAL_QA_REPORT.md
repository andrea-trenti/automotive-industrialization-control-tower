# FINAL QA REPORT

## Release

**v1.0.1 — portfolio presentation polish**

**Status: PASS — release gate satisfied.**

This release changes presentation, recruiter readability and GitHub usability only. Validated schedule-risk, Target+, stress, readiness and economics results are unchanged from the verified methodological release.

## Repository audit

- Broken local Markdown links: **0**
- Byte-identical duplicate files/documents: **0**
- Filenames containing spaces: **0**
- Python/pytest cache artifacts: **removed from release tree**
- Stale release manifest: **regenerated for v1.0.1**
- Stale numerical result files: **none identified**
- Core quantitative results modified: **no**
- Technical thesis PDF content modified: **no**

No methodology document was removed solely to reduce file count. The short framework documents remain intentionally separate because the README now links them as a navigable technical appendix set.

## Presentation changes

- Reworked README above-the-fold around the launch decision and validated scale/results.
- Added one recruiter-facing hero figure: deterministic CPM → stochastic baseline P80 → Target+ P80.
- Kept automation-debug +35% as the principal technical failure case.
- Added two synthetic-safe quantitative CV bullets.
- Added `INTERVIEW_TALKING_POINTS.md` with a concise technical narrative and 60-second version.
- Added GitHub description/topics/pinning guidance.
- Added `VERSION` and `CHANGELOG.md` for documentation-only versioning.

## Validated core results

- Activities: **720**
- Dependencies: **1,102**
- Suppliers: **42**
- Equipment assets: **144**
- Quantified risks: **320**
- Deterministic SOP: **636 workdays**
- Baseline P50/P80/P90: **723 / 766 / 786**
- Baseline P(on-time): **70.9%**
- Target+ P50/P80/P90: **678 / 713 / 734**
- Target+ P(on-time): **95.4%**
- Fresh-seed Target+: **679 / 714 / 735; 95.1%**
- Modeled Target+ mitigation cost: **€1,579,799**
- Automation debug +35%: **P80 823; P(on-time) 31.5%**

## Smoke-test gates

- `python pipeline.py`: **PASS**
- `pytest -q`: **35 passed, 0 failed**
- README numerical consistency against `outputs/core_results.json`: **PASS**
- Local Markdown-link audit: **PASS**
- Hero figure file/readability check: **PASS**
- Technical thesis PDF retained from validated release: **PASS**
- FULL ZIP integrity: **PASS**
- GITHUB ZIP integrity: **PASS**

## Credibility boundary

This release remains a **research-grade synthetic automotive industrialization and commissioning study**. It demonstrates engineering architecture, probabilistic schedule-risk analysis, resource constraints, commissioning logic, mitigation economics, falsification and decision support. It is not empirically calibrated to a real OEM launch.

Real industrial validation would require historical project schedules, named-resource calendars, PLM engineering changes, supplier milestones, FAT/SAT and commissioning-rework histories, QMS/CMMS evidence and finance-approved delay-cost inputs.

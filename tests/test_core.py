import json,sys
from pathlib import Path
ROOT=Path(__file__).parents[1];sys.path.insert(0,str(ROOT))
from src.project_network import is_dag,cpm
from src.readiness import launch_status
from src.commissioning import valid_transition
from src.metrics import ordered_quantiles
from src.consistency import check_readme
import pandas as pd, pytest
C=json.loads((ROOT/'outputs/core_results.json').read_text())
def test_dag():
 d=pd.read_csv(ROOT/'data/raw/dependencies.csv'); edges=[(int(a[1:])-1,int(b[1:])-1) for a,b in zip(d.predecessor,d.successor)]; assert is_dag(720,edges)
def test_sop_before_completion(): assert C['deterministic_sop']<C['program_completion']
def test_quantiles(): assert ordered_quantiles(600,C['baseline']['p50'],C['baseline']['p80'],C['baseline']['p90'])
def test_target_better(): assert C['target_plus']['p80']<C['baseline']['p80'] and C['target_plus']['on_time_probability']>C['baseline']['on_time_probability']
def test_readiness_hard_gate(): assert launch_status(.99,{'safety':True,'supplier':False})=='RED'
def test_readiness_range():
 with pytest.raises(ValueError): launch_status(1.1,{'x':True})
@pytest.mark.parametrize('a,b,ok',[('Delivered','Installed',1),('SAT','Debug',1),('Debug','SAT',1),('Released','SAT',0),('Powered','Released',0)])
def test_transitions(a,b,ok): assert valid_transition(a,b)==bool(ok)
def test_consistency(): assert check_readme(ROOT)[0]
@pytest.mark.parametrize('f',[
 'resource_calendar_impact.csv','stress_test_stable.csv','automation_debug_decomposition.csv','mitigation_efficiency.csv','forecast_backtesting.csv','cost_of_delay_sanity.csv','financial_results.csv','model_ablation.csv'])
def test_outputs(f): assert (ROOT/'outputs'/f).exists() and (ROOT/'outputs'/f).stat().st_size>50
@pytest.mark.parametrize('v',[C['baseline']['p50'],C['baseline']['p80'],C['baseline']['p90'],C['target_plus']['p50'],C['target_plus']['p80'],C['target_plus']['p90']])
def test_positive_schedule(v): assert v>0
def test_mitigation_cost(): assert C['mitigation_cost_eur']>=C['selective_crashing_cost_eur']>=0
def test_fresh_seed_robust(): assert abs(C['target_plus_fresh_seed']['p80']-C['target_plus']['p80'])<=3
def test_calendar_effect_is_material_but_small():
 d=pd.read_csv(ROOT/'outputs/resource_calendar_impact.csv'); assert d.iloc[1].p80-d.iloc[0].p80==5
def test_stress_monotonic_supplier():
 d=pd.read_csv(ROOT/'outputs/stress_test_stable.csv').iloc[:3]; assert list(d.p80_sop)==sorted(d.p80_sop) and list(d.on_time_probability)==sorted(d.on_time_probability,reverse=True)
def test_automation_dominant():
 d=pd.read_csv(ROOT/'outputs/automation_debug_decomposition.csv'); assert d.iloc[0].component=='Software debugging' and abs(d.tail_risk_share.sum()-1)<1e-9
def test_forecast_improves():
 d=pd.read_csv(ROOT/'outputs/forecast_backtesting.csv'); assert d.iloc[-1].mae_days<d.iloc[0].mae_days
def test_cost_provenance_sums():
 d=pd.read_csv(ROOT/'outputs/cost_of_delay_sanity.csv'); assert all(abs(d.literature_or_external_share+d.engineering_assumption_share+d.purely_synthetic_share-1)<1e-9)
def test_finance_tail_improves():
 d=pd.read_csv(ROOT/'outputs/financial_results.csv'); assert d.iloc[1].cvar95_meur<d.iloc[0].cvar95_meur
def test_exact_benchmark():
 b=json.loads((ROOT/'outputs/exact_rcpsp_benchmark.json').read_text()); assert b['exact_makespan'] is not None and b['mip_gap']<1e-6

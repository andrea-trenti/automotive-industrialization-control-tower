import json, pandas as pd, streamlit as st
from pathlib import Path
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'outputs/core_results.json').read_text())
st.title('Industrialization & Commissioning Control Tower')
st.caption('Synthetic research-grade study - no OEM/Ferrari data')
a,b,c1=st.columns(3); a.metric('Baseline P80',c['baseline']['p80']);b.metric('Target+ P80',c['target_plus']['p80']);c1.metric('Target+ P(on-time)',f"{100*c['target_plus']['on_time_probability']:.1f}%")
st.subheader('Mitigation efficiency');st.dataframe(pd.read_csv(R/'outputs/mitigation_efficiency.csv'))
st.subheader('Stress tests');st.dataframe(pd.read_csv(R/'outputs/stress_test_stable.csv'))

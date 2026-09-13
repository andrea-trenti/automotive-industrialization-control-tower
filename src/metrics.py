def ordered_quantiles(p10,p50,p80,p90): return p10<=p50<=p80<=p90
def mc_se_probability(p,n): return (p*(1-p)/n)**0.5

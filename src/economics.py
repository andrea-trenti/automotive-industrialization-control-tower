def cost_per_day_saved(cost, days):
    return None if days <= 0 else cost/days
def expected_delay_cost(samples_days, cost_per_day):
    return sum(max(0,x)*cost_per_day for x in samples_days)/len(samples_days)

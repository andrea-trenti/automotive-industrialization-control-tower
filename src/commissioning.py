VALID=['Not Delivered','Delivered','Installed','Powered','I/O Checked','Dry Run','SAT','Debug','Capability','Released']
def valid_transition(a,b):
    if a not in VALID or b not in VALID:return False
    ia,ib=VALID.index(a),VALID.index(b)
    return ib==ia+1 or (a=='SAT' and b=='Debug') or (a=='Debug' and b=='SAT') or (a=='Debug' and b=='Capability')

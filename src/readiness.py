def launch_status(index, gates):
    if not 0 <= index <= 1: raise ValueError('readiness outside [0,1]')
    if any(not v for v in gates.values()): return 'RED'
    return 'GREEN' if index >= .9 else 'AMBER'

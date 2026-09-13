from collections import defaultdict, deque

def is_dag(n, edges):
    indeg=[0]*n; g=defaultdict(list)
    for a,b in edges: g[a].append(b); indeg[b]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return seen==n

def cpm(durations, edges):
    n=len(durations); g=defaultdict(list); pred=defaultdict(list); indeg=[0]*n
    for a,b in edges:g[a].append(b);pred[b].append(a);indeg[b]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); order=[]
    while q:
        u=q.popleft();order.append(u)
        for v in g[u]: indeg[v]-=1; q.append(v) if indeg[v]==0 else None
    if len(order)!=n: raise ValueError('cycle')
    es=[0]*n; ef=[0]*n
    for u in order: es[u]=max((ef[p] for p in pred[u]),default=0);ef[u]=es[u]+durations[u]
    return {'es':es,'ef':ef,'makespan':max(ef)}

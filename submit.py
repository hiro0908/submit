graph = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        continue
    a, b, d = (s.strip() for s in line.split(","))
    a, b, d = int(a), int(b), float(d)
    graph.setdefault(a, []).append((b, d))
    graph.setdefault(b, []).append((a, d))  # 路線は双方向

best_dist, best_path = -1.0, []


def dfs(node, dist, path, visited):
    global best_dist, best_path
    if dist > best_dist:
        best_dist, best_path = dist, path[:]
    for nxt, d in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            path.append(nxt)
            dfs(nxt, dist + d, path, visited)
            path.pop()
            visited.remove(nxt)


for start in graph:
    dfs(start, 0.0, [start], {start})

for node in best_path:
    print(node, end="\r\n")
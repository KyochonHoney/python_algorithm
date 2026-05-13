"""
================================================================================
[13] 너비 우선 탐색 (BFS, Breadth-First Search)
================================================================================

## 개념
그래프나 트리에서 시작 노드로부터 가까운 노드를 먼저 탐색하는 방법이에요.
마치 호수에 돌을 던졌을 때 파문이 퍼지는 것처럼 가까운 곳부터 넓게 탐색해요.

## 핵심 자료구조: 큐 (Queue)
  - 먼저 들어온 것이 먼저 나가는(FIFO) 자료구조
  - from collections import deque

## 공식 (알고리즘 단계)
  1. 시작 노드를 큐에 넣고 방문 처리
  2. 큐에서 노드를 꺼낸다
  3. 꺼낸 노드의 인접 노드 중 방문하지 않은 노드를 큐에 넣고 방문 처리
  4. 큐가 빌 때까지 2~3 반복

  from collections import deque
  queue = deque([start])
  visited = {start}
  while queue:
      node = queue.popleft()       # 큐에서 꺼내기
      for neighbor in graph[node]:
          if neighbor not in visited:
              visited.add(neighbor)
              queue.append(neighbor)  # 큐에 추가

## 시간복잡도
  O(V + E)   V: 노드 수, E: 간선 수

## BFS의 특징
  - 최단 경로 보장 (가중치 없는 그래프에서)
  - 두 노드 사이의 최단 거리 구하기에 활용

================================================================================
"""

from collections import deque


# ===== 개념 코드: BFS 탐색 순서 확인 =====

def bfs(graph, start):
    """
    graph: {노드: [인접 노드 리스트]} 형태의 인접 리스트
    start: 시작 노드
    반환값: BFS 탐색 순서 리스트
    """
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 미로 탈출 최단 경로
#       N×M 격자 미로가 주어져요. (1=길, 0=벽)
#       (0,0)에서 출발하여 (N-1, M-1)까지 가는 최단 거리를 구하세요.
#       이동 방향: 상/하/좌/우 (대각선 불가)
#
# 입력: 2차원 리스트 maze (0=벽, 1=길)
# 출력: 최단 거리 (도달 불가능하면 -1)
#
# 예시:
#   maze = [
#       [1, 0, 1, 1, 1],
#       [1, 0, 1, 0, 1],
#       [1, 1, 1, 0, 1],
#       [0, 0, 0, 0, 1],
#       [0, 0, 0, 0, 1]
#   ]
#   최단 거리: 9 (시작점 포함)
# ================================================================================

def shortest_path_maze(maze):
    n = len(maze)
    m = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우

    # (행, 열, 거리) 형태로 큐 시작
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        row, col, dist = queue.popleft()

        if row == n - 1 and col == m - 1:   # 도착!
            return dist

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maze[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

    return -1   # 도달 불가


if __name__ == "__main__":
    print("=== BFS 탐색 순서 ===")
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    print("  그래프 구조 (트리):")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\ / \\")
    print("    4  5 6  7")
    order = bfs(graph, 1)
    print(f"  BFS 탐색 순서: {order}  (가까운 노드 먼저)")

    print()
    print("=== 예제 문제: 미로 최단 경로 ===")
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
    ]
    print("  미로 (1=길, 0=벽):")
    for row in maze:
        print(f"    {row}")
    dist = shortest_path_maze(maze)
    print(f"  (0,0)에서 (4,4)까지 최단 거리: {dist}칸")

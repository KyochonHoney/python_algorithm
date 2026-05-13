"""
================================================================================
[14] 깊이 우선 탐색 (DFS, Depth-First Search)
================================================================================

## 개념
그래프나 트리에서 한 방향으로 갈 수 있는 끝까지 깊이 파고들다가,
더 이상 갈 곳이 없으면 되돌아와 다른 방향을 탐색하는 방법이에요.
미로를 탈출할 때 한 방향으로 끝까지 가다가 막히면 돌아오는 것과 같아요.

## 핵심 자료구조: 스택 (Stack) 또는 재귀 함수
  - 재귀 함수: 함수 호출 스택을 자연스럽게 활용

## 공식 (알고리즘 단계 — 재귀 버전)
  def dfs(node, visited):
      visited.add(node)           # 현재 노드 방문 처리
      처리(node)                   # 원하는 작업 수행
      for neighbor in graph[node]:
          if neighbor not in visited:
              dfs(neighbor, visited)   # 재귀로 깊이 탐색

## 시간복잡도
  O(V + E)   V: 노드 수, E: 간선 수

## BFS vs DFS 비교
  BFS (너비 우선):  가까운 것부터 탐색, 최단 경로 찾기에 유리, 큐 사용
  DFS (깊이 우선):  깊이 탐색, 경로 탐색/연결 확인에 유리, 스택/재귀 사용

## 대표 활용
  - 연결 요소(Connected Component) 개수 세기
  - 사이클 감지
  - 위상 정렬

================================================================================
"""


# ===== 개념 코드: DFS 탐색 =====

def dfs(graph, start, visited=None):
    """
    graph: {노드: [인접 노드 리스트]} 형태의 인접 리스트
    start: 시작 노드
    반환값: DFS 탐색 순서 리스트
    """
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 연결 요소(섬) 개수 세기
#       N×M 격자에서 1은 땅, 0은 바다예요.
#       상하좌우로 연결된 땅의 덩어리를 "섬"이라고 할 때,
#       격자에 있는 섬의 개수를 구하세요.
#
# 입력: 2차원 리스트 grid (0=바다, 1=땅)
# 출력: 섬의 개수
#
# 예시:
#   grid = [
#       [1, 1, 0, 0, 0],
#       [1, 1, 0, 0, 0],
#       [0, 0, 1, 0, 0],
#       [0, 0, 0, 1, 1],
#   ]
#   섬: 왼쪽 위(4칸), 중간(1칸), 오른쪽 아래(2칸) → 3개
# ================================================================================

def count_islands(grid):
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    count = 0

    def dfs_island(row, col):
        # 범위 초과, 바다, 이미 방문한 곳이면 즉시 반환
        if row < 0 or row >= n or col < 0 or col >= m:
            return
        if visited[row][col] or grid[row][col] == 0:
            return

        visited[row][col] = True   # 방문 처리

        # 상하좌우 탐색
        dfs_island(row - 1, col)
        dfs_island(row + 1, col)
        dfs_island(row, col - 1)
        dfs_island(row, col + 1)

    for r in range(n):
        for c in range(m):
            if not visited[r][c] and grid[r][c] == 1:
                dfs_island(r, c)   # 새로운 섬 발견 → DFS로 전체 탐색
                count += 1

    return count


if __name__ == "__main__":
    print("=== DFS 탐색 순서 ===")
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
    order = dfs(graph, 1)
    print(f"  DFS 탐색 순서: {order}  (깊이 먼저)")
    print(f"  BFS 탐색 순서: [1, 2, 3, 4, 5, 6, 7]  (너비 먼저, 참고)")

    print()
    print("=== 예제 문제: 섬의 개수 세기 ===")
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    print("  격자 (1=땅, 0=바다):")
    for row in grid:
        print(f"    {row}")
    islands = count_islands(grid)
    print(f"  섬의 개수: {islands}개")

    print()
    grid2 = [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
    ]
    print("  격자 2:")
    for row in grid2:
        print(f"    {row}")
    print(f"  섬의 개수: {count_islands(grid2)}개")

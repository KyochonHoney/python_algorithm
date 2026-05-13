"""
================================================================================
[12] 백트래킹 (Backtracking)
================================================================================

## 개념
가능한 모든 경우를 탐색하되, 조건에 맞지 않는 경로는 더 이상 탐색하지 않고
이전 상태로 되돌아가는(backtrack) 방법이에요.
"일단 가보다가 막히면 돌아오기"라고 생각하면 돼요.

## 핵심 구조 (재귀 탐색)
  def backtrack(상태):
      if 완료 조건:             # ① 정답 발견
          결과에 추가
          return
      for 선택지 in 가능한 선택들:
          if 유효하지 않으면:   # ② 가지치기 (Pruning)
              continue
          선택 실행              # ③ 선택
          backtrack(다음 상태)  # ④ 재귀 탐색
          선택 취소              # ⑤ 되돌리기 (Backtrack)

## 완전 탐색(Brute Force)과의 차이
  완전 탐색: 모든 경우를 탐색 (느림)
  백트래킹: 불가능한 경로를 조기 차단 (가지치기로 빠름)

## 대표 문제
  - N-Queens (체스판에 N개의 퀸 배치)
  - 순열/조합 생성
  - 미로 탈출

================================================================================
"""


# ===== 개념 코드: N개 중 M개 순서 있게 선택 (순열) =====

def permutations(items, m):
    """items에서 m개를 순서 있게 선택하는 모든 순열을 반환한다."""
    result = []

    def backtrack(current, used):
        if len(current) == m:   # 완료 조건
            result.append(current[:])
            return

        for i, item in enumerate(items):
            if not used[i]:        # 아직 선택하지 않은 항목만
                used[i] = True     # 선택
                current.append(item)
                backtrack(current, used)
                current.pop()      # 되돌리기
                used[i] = False    # 되돌리기

    backtrack([], [False] * len(items))
    return result


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: N-Queens
#       N×N 체스판에 N개의 퀸(Queen)을 서로 공격하지 않도록 배치하는
#       모든 경우의 수와 각 배치를 구하세요.
#       퀸은 같은 행, 같은 열, 대각선 방향으로 공격할 수 있어요.
#
# 입력: 정수 n (체스판 크기)
# 출력: 가능한 배치 수, 각 배치 (queens[i] = i행에서 퀸이 있는 열 번호)
#
# 예시:
#   n=4:
#   .Q..    ..Q.
#   ...Q    Q...
#   Q...    ...Q
#   ..Q.    .Q..
#   → 2가지 배치
# ================================================================================

def n_queens(n):
    results = []
    queens = []   # queens[i] = i행에서 퀸이 있는 열 번호

    def is_valid(row, col):
        for r, c in enumerate(queens):
            if c == col:              # 같은 열
                return False
            if abs(r - row) == abs(c - col):   # 대각선
                return False
        return True

    def backtrack(row):
        if row == n:   # 모든 행에 퀸을 배치 완료
            results.append(queens[:])
            return

        for col in range(n):
            if is_valid(row, col):   # 이 위치에 퀸을 놓을 수 있는지
                queens.append(col)   # 선택
                backtrack(row + 1)   # 다음 행 탐색
                queens.pop()         # 되돌리기

    backtrack(0)
    return results


def print_board(queens):
    """퀸 배치를 체스판으로 시각화한다."""
    n = len(queens)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if queens[row] == col else ". "
        print(f"    {line}")
    print()


if __name__ == "__main__":
    print("=== 백트래킹: 순열 생성 ===")
    items = [1, 2, 3]
    perms = permutations(items, 2)
    print(f"  {items}에서 2개 선택 순열: {perms}  ({len(perms)}가지)")

    print()
    print("=== 예제 문제: N-Queens ===")
    for n in [4, 5]:
        solutions = n_queens(n)
        print(f"  {n}×{n} 체스판: {len(solutions)}가지 배치")
        if n == 4:
            for i, sol in enumerate(solutions):
                print(f"  [배치 {i+1}] 열 번호: {sol}")
                print_board(sol)

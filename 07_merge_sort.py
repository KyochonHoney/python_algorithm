"""
================================================================================
[07] 합병 정렬 (Merge Sort)
================================================================================

## 개념
분할정복을 이용한 정렬이에요.
배열을 반으로 계속 나누고(분할), 각각 정렬한 뒤(정복), 두 정렬된 배열을 합병(통합)해요.

## 공식 (알고리즘 단계)
  1. 분할: 배열을 절반으로 나눈다  →  arr[:mid], arr[mid:]
  2. 정복: 각 절반을 재귀적으로 합병 정렬한다
  3. 합병: 두 정렬된 배열을 비교하며 하나의 정렬된 배열로 합친다

  merge_sort(arr):
      if len(arr) <= 1: return arr          # 기저 조건
      mid = len(arr) // 2
      left  = merge_sort(arr[:mid])         # 왼쪽 절반 정렬
      right = merge_sort(arr[mid:])         # 오른쪽 절반 정렬
      return merge(left, right)             # 두 정렬된 배열 합병

  merge(L, R):
      결과 배열에 L과 R을 비교하며 작은 값부터 순서대로 담기

## 시간복잡도
  최선/평균/최악: O(n log n)  — 항상 같음 (가장 안정적인 정렬 중 하나)
  점화식: T(n) = 2T(n/2) + O(n)

## 공간복잡도
  O(n) — 합병할 임시 배열 필요 (in-place가 아님)

================================================================================
"""


# ===== 개념 코드: 합병 정렬 =====

def merge(left, right):
    """두 정렬된 배열 left, right를 하나의 정렬된 배열로 합병한다."""
    result = []
    i = j = 0

    # 두 배열을 앞에서부터 비교하며 작은 값을 result에 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    """합병 정렬로 arr을 오름차순 정렬하여 반환한다."""
    if len(arr) <= 1:   # 기저 조건: 원소 0~1개는 이미 정렬됨
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # 왼쪽 절반 정렬
    right = merge_sort(arr[mid:])   # 오른쪽 절반 정렬

    return merge(left, right)   # 두 정렬된 절반을 합병


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 두 개의 팀(A팀, B팀)이 각각 이미 정렬된 점수 리스트를 가지고 있어요.
#       두 팀의 점수를 합쳐서 순위표를 만드세요. (오름차순 정렬)
#
# 입력: 정렬된 정수 리스트 team_a, team_b
# 출력: 합쳐진 오름차순 정렬 리스트
#
# 예시:
#   team_a = [10, 30, 50, 70]
#   team_b = [20, 40, 60, 80]
#   결과:    [10, 20, 30, 40, 50, 60, 70, 80]
#
# 힌트: merge() 함수를 그대로 활용하면 O(n+m)으로 해결할 수 있어요!
# ================================================================================

def merge_rankings(team_a, team_b):
    """두 정렬된 팀 점수 리스트를 합쳐 순위표를 만든다."""
    return merge(team_a, team_b)


if __name__ == "__main__":
    print("=== 합병 정렬 단계별 시각화 ===")
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"  입력: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"  결과: {sorted_arr}")

    print()
    print("=== 예제 문제: 팀 합산 순위표 ===")
    team_a = [10, 30, 50, 70]
    team_b = [20, 40, 60, 80]
    combined = merge_rankings(team_a, team_b)
    print(f"  A팀 점수: {team_a}")
    print(f"  B팀 점수: {team_b}")
    print(f"  합산 순위표: {combined}")

    print()
    # 합병 정렬 안정성 확인
    print("=== O(n log n) 성능 확인 ===")
    import random, time
    for size in [100, 1000, 10000]:
        data = [random.randint(0, 10000) for _ in range(size)]
        start = time.time()
        merge_sort(data)
        elapsed = time.time() - start
        print(f"  n={size:6d}: {elapsed:.4f}초")

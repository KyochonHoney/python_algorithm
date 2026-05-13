"""
================================================================================
[03] 선택 알고리즘 (Selection Algorithm) — Quick Select
================================================================================

## 개념
n개의 숫자 중에서 k번째로 작은 값을 효율적으로 찾는 알고리즘이에요.
정렬 후 인덱스로 접근하면 O(n log n)이지만, Quick Select는 평균 O(n)에 해결해요.

## Quick Select 핵심 아이디어
  pivot(기준값) 하나를 고른 뒤, 배열을 세 그룹으로 나눠요:
    A : pivot보다 작은 값들
    M : pivot과 같은 값들
    B : pivot보다 큰 값들

  k번째 값이 어느 그룹에 있는지 판단:
    - len(A) >= k        → k번째 값은 A에 있음  →  A에서 다시 찾기
    - len(A)+len(M) >= k → k번째 값은 M에 있음  →  pivot이 정답!
    - 그 외               → k번째 값은 B에 있음  →  B에서 (k-len(A)-len(M))번째 찾기

## 시간복잡도
  평균: O(n)    최악: O(n²) (pivot이 매번 최솟값/최댓값일 때)

================================================================================
"""


# ===== 개념 코드: Quick Select =====

def quick_select(arr, k):
    """
    arr에서 k번째로 작은 값을 반환한다. (k는 1-indexed: 1이 가장 작은 값)
    """
    if len(arr) == 0:
        return None

    pivot = arr[0]
    A = [x for x in arr if x < pivot]   # pivot보다 작은 값
    M = [x for x in arr if x == pivot]  # pivot과 같은 값
    B = [x for x in arr if x > pivot]   # pivot보다 큰 값

    if k <= len(A):
        return quick_select(A, k)
    elif k <= len(A) + len(M):
        return pivot   # pivot이 정답
    else:
        return quick_select(B, k - len(A) - len(M))


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 성적 목록에서 중앙값(median)을 구하세요.
#       중앙값은 정렬했을 때 가운데 위치하는 값이에요.
#       (홀수 개: 정중앙 값 / 짝수 개: 두 중앙값 중 작은 값)
#
# 입력: 정수 리스트 scores
# 출력: 중앙값 (정수)
#
# 예시:
#   [3, 1, 4, 1, 5]  → 정렬하면 [1,1,3,4,5]  → 중앙값 = 3  (3번째로 작은 값)
#   [7, 2, 10, 9]    → 정렬하면 [2,7,9,10]   → 중앙값 = 7  (2번째로 작은 값)
#
# 힌트: n개짜리 배열에서 중앙값의 순위 k = (n + 1) // 2
# ================================================================================

def find_median(scores):
    n = len(scores)
    k = (n + 1) // 2   # 중앙값의 순위 (1-indexed)
    return quick_select(scores, k)


if __name__ == "__main__":
    print("=== Quick Select 동작 확인 ===")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    for k in range(1, len(arr) + 1):
        print(f"  {k}번째로 작은 값: {quick_select(arr, k)}")

    print()
    print("=== 예제 문제: 중앙값 찾기 ===")
    test_cases = [
        [3, 1, 4, 1, 5],
        [7, 2, 10, 9],
        [42],
        [5, 3, 8, 1, 9, 2, 7],
    ]
    for scores in test_cases:
        median = find_median(scores)
        sorted_scores = sorted(scores)
        print(f"  입력: {scores}")
        print(f"  정렬: {sorted_scores}  →  중앙값 = {median}")
        print()

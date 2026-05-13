"""
================================================================================
[04] 분할정복 (Divide & Conquer)
================================================================================

## 개념
큰 문제를 더 작은 문제로 나누고(분할), 각각을 재귀로 풀고(정복), 결과를 합치는(통합) 방법이에요.

## 3단계 구조
  1. 분할 (Divide)   : 문제를 더 작은 부분으로 쪼갠다
  2. 정복 (Conquer)  : 부분 문제를 재귀적으로 해결한다
  3. 통합 (Combine)  : 부분 해답을 합쳐 원래 문제의 답을 만든다

## 공식 (마스터 정리)
  T(n) = a·T(n/b) + f(n)
    a : 재귀 호출 횟수
    b : 분할 비율
    f(n) : 분할 & 통합에 걸리는 시간

## 대표적인 분할정복 시간복잡도 예시
  T(n) = T(n/2) + O(1)   → O(log n)   (이진탐색)
  T(n) = 2T(n/2) + O(n)  → O(n log n) (합병정렬)
  T(n) = T(n-1) + O(1)   → O(n)       (순차탐색)

================================================================================
"""


# ===== 개념 코드: 배열의 최댓값과 최솟값 동시에 찾기 =====
# 단순 방법: 최댓값 찾기 n-1번 + 최솟값 찾기 n-1번 = 비교 2(n-1)번
# 분할정복: 비교 횟수를 약 3n/2로 줄일 수 있어요!

def find_min_max(arr, left, right):
    """
    arr[left..right] 에서 (최솟값, 최댓값) 쌍을 반환한다.
    분할정복으로 비교 횟수를 최소화한다.
    """
    # 기저 조건 1: 원소가 1개
    if left == right:
        return arr[left], arr[left]

    # 기저 조건 2: 원소가 2개
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    # 분할: 중간을 기준으로 두 부분으로 나눔
    mid = (left + right) // 2

    # 정복: 각 부분의 최솟값/최댓값을 재귀로 구함
    left_min, left_max = find_min_max(arr, left, mid)
    right_min, right_max = find_min_max(arr, mid + 1, right)

    # 통합: 두 부분의 결과를 합침
    total_min = left_min if left_min < right_min else right_min
    total_max = left_max if left_max > right_max else right_max

    return total_min, total_max


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 주식 가격 리스트가 주어질 때, 분할정복으로 최저가와 최고가를 동시에 구하세요.
#       (내장 함수 min(), max() 사용 금지 — 직접 분할정복으로 구현)
#
# 입력: 정수 리스트 prices (주식 가격)
# 출력: (최저가, 최고가) 튜플
#
# 예시:
#   [3, 1, 4, 1, 5, 9, 2, 6]  →  (최저가=1, 최고가=9)
#   [100, 200, 50, 300, 150]   →  (최저가=50, 최고가=300)
# ================================================================================

def stock_min_max(prices):
    if not prices:
        return None, None
    return find_min_max(prices, 0, len(prices) - 1)


if __name__ == "__main__":
    print("=== 분할정복: 최솟값/최댓값 동시 찾기 ===")

    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [100, 200, 50, 300, 150],
        [7],
        [4, 2],
        [9, 3, 7, 1, 5],
    ]

    for prices in test_cases:
        low, high = stock_min_max(prices)
        print(f"  가격 목록: {prices}")
        print(f"  결과: 최저가={low}, 최고가={high}  (차익={high - low})")
        print()

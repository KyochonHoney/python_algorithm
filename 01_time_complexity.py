"""
================================================================================
[01] 시간복잡도 (Time Complexity) & 빅오 표기법 (Big-O Notation)
================================================================================

## 개념
알고리즘이 입력 크기 n에 따라 얼마나 많은 시간(연산 횟수)이 필요한지를 나타내는 척도예요.
빅오(Big-O) 표기법은 최악의 경우(Worst Case)를 기준으로 표현해요.

## 주요 시간복잡도 (빠른 순서대로)
  O(1)       — 상수 시간   : 입력 크기와 무관하게 항상 같은 시간
  O(log n)   — 로그 시간   : 입력이 2배 늘어도 연산 1번 증가 (이진탐색)
  O(n)       — 선형 시간   : 입력에 비례해 연산 증가 (선형탐색)
  O(n log n) — 선형로그    : 합병정렬, 퀵정렬 평균
  O(n²)      — 이차 시간   : 버블정렬, 삽입정렬
  O(2ⁿ)      — 지수 시간   : 단순 재귀 피보나치

## 핵심 규칙
  1. 상수는 무시한다          : O(3n) → O(n)
  2. 가장 큰 항만 남긴다      : O(n² + n) → O(n²)
  3. 최악의 경우를 기준으로   : 정렬된 배열도 O(n)으로 분석

================================================================================
"""


# ===== 개념 코드 예시 =====

def o_1_example(arr):
    """O(1) — 배열의 첫 번째 원소 반환 (입력 크기와 무관)"""
    return arr[0]


def o_n_example(arr, target):
    """O(n) — 선형 탐색 (배열을 처음부터 끝까지 순서대로 확인)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def o_log_n_example(arr, target):
    """O(log n) — 이진 탐색 (정렬된 배열에서 절반씩 범위를 줄임)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def o_n2_example(arr):
    """O(n²) — 버블 정렬 (이중 반복문)"""
    n = len(arr)
    result = arr[:]
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 아래 네 함수의 시간복잡도를 비교하여, 같은 입력(n=1000)에서
#       각 함수가 몇 번의 연산을 수행하는지 직접 카운트해보세요.
#
# 학습 목표: 시간복잡도가 알고리즘 성능에 얼마나 큰 영향을 주는지 체감하기
# ================================================================================

def count_operations(n):
    """각 Big-O별 연산 횟수를 출력한다."""
    import math

    print(f"입력 크기 n = {n} 일 때 연산 횟수 비교:")
    print(f"  O(1)       = {1:>15,} 번")
    print(f"  O(log n)   = {int(math.log2(n)):>15,} 번")
    print(f"  O(n)       = {n:>15,} 번")
    print(f"  O(n log n) = {int(n * math.log2(n)):>15,} 번")
    print(f"  O(n²)      = {n ** 2:>15,} 번")
    print(f"  O(2ⁿ)      = 너무 커서 생략 (2^1000은 우주 원자 수보다 많아요!)")


if __name__ == "__main__":
    count_operations(1000)

    print()
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    print(f"배열: {arr}, 찾는 값: {target}")
    print(f"선형탐색 O(n)   결과: 인덱스 {o_n_example(arr, target)}")
    print(f"이진탐색 O(logn) 결과: 인덱스 {o_log_n_example(arr, target)}")

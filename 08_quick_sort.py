"""
================================================================================
[08] 퀵 정렬 (Quick Sort)
================================================================================

## 개념
pivot(기준값)을 하나 골라 pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할하고,
각 부분을 재귀적으로 정렬하는 방법이에요.
실제로 가장 많이 쓰이는 정렬 알고리즘이에요!

## 공식 (알고리즘 단계)
  1. pivot 선택: 배열에서 기준값을 고른다 (주로 첫 번째 또는 중간 원소)
  2. 분할: pivot보다 작은 값 → 왼쪽, 같은 값 → 중간, 큰 값 → 오른쪽
  3. 재귀: 왼쪽과 오른쪽을 각각 다시 퀵 정렬한다
  4. 합치기: [왼쪽] + [중간] + [오른쪽]

  quick_sort(arr):
      if len(arr) <= 1: return arr
      pivot = arr[len(arr) // 2]
      left  = [x for x in arr if x < pivot]
      mid   = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + mid + quick_sort(right)

## 시간복잡도
  평균: O(n log n)   — pivot이 항상 중앙에 가까운 값일 때
  최악: O(n²)        — pivot이 항상 최솟값/최댓값일 때 (이미 정렬된 배열 + 첫 원소 pivot)
  점화식: T(n) = 2T(n/2) + O(n)  (평균)

## 합병 정렬과 비교
  합병 정렬 : 항상 O(n log n), 추가 메모리 O(n) 필요
  퀵 정렬   : 평균 O(n log n), 추가 메모리 거의 없음 (but 최악 O(n²))

================================================================================
"""


# ===== 개념 코드: 퀵 정렬 (간단 버전) =====

def quick_sort(arr):
    """퀵 정렬로 arr을 오름차순 정렬하여 반환한다."""
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]   # 중간 원소를 pivot으로 선택
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 학생들의 나이 목록이 주어졌을 때, 퀵 정렬로 오름차순 정렬하고
#       각 나이별로 몇 명인지 카운트하세요.
#
# 입력: 정수 리스트 ages
# 출력: 정렬된 나이 리스트, {나이: 인원수} 딕셔너리
#
# 예시:
#   입력: [22, 19, 22, 20, 19, 21, 22, 20]
#   정렬: [19, 19, 20, 20, 21, 22, 22, 22]
#   카운트: {19: 2, 20: 2, 21: 1, 22: 3}
# ================================================================================

def analyze_ages(ages):
    sorted_ages = quick_sort(ages)

    count = {}
    for age in sorted_ages:
        count[age] = count.get(age, 0) + 1

    return sorted_ages, count


if __name__ == "__main__":
    print("=== 퀵 정렬 단계 이해 ===")
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"  입력: {arr}")

    # 한 단계 분할 시각화
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"  pivot = {pivot}")
    print(f"  left(pivot 미만)  = {left}")
    print(f"  mid (pivot 동일)  = {mid}")
    print(f"  right(pivot 초과) = {right}")
    print(f"  최종 결과: {quick_sort(arr)}")

    print()
    print("=== 예제 문제: 나이 분석 ===")
    ages = [22, 19, 22, 20, 19, 21, 22, 20]
    sorted_ages, count = analyze_ages(ages)
    print(f"  입력:   {ages}")
    print(f"  정렬:   {sorted_ages}")
    print(f"  카운트: {count}")
    print()
    most_common_age = max(count, key=count.get)
    print(f"  가장 많은 나이: {most_common_age}세 ({count[most_common_age]}명)")

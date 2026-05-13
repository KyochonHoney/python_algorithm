"""
================================================================================
[05] 버블 정렬 (Bubble Sort)
================================================================================

## 개념
인접한 두 원소를 비교하여 순서가 잘못되어 있으면 교환하는 정렬이에요.
한 번의 전체 순회가 끝나면 가장 큰 값이 맨 끝으로 "거품처럼 떠오른다"는 데서 이름이 왔어요.

## 공식 (알고리즘 단계)
  1. 배열의 처음부터 끝까지 인접한 두 원소를 비교한다.
  2. 앞 원소 > 뒤 원소 이면 두 원소를 교환(swap)한다.
  3. 한 번의 순회 후 가장 큰 값이 맨 끝에 고정된다.
  4. 고정된 부분을 제외하고 1~3을 n-1번 반복한다.

  for i in range(n):
      for j in range(n - i - 1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

## 시간복잡도
  최선(이미 정렬됨): O(n)   — 교환이 없으면 조기 종료 가능
  평균/최악:         O(n²)

## 공간복잡도
  O(1) — 제자리(in-place) 정렬

================================================================================
"""


# ===== 개념 코드: 버블 정렬 (최적화 포함) =====

def bubble_sort(arr):
    """
    버블 정렬로 arr을 오름차순 정렬하여 반환한다.
    swapped 최적화: 한 순회에서 교환이 없으면 이미 정렬된 것 → 조기 종료
    """
    result = arr[:]   # 원본 배열 보존
    n = len(result)

    for i in range(n):
        swapped = False   # 이번 순회에서 교환이 발생했는지 추적

        for j in range(n - i - 1):   # 마지막 i개는 이미 정렬됨
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:   # 교환이 없으면 이미 정렬 완료
            break

    return result


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 시험 점수 목록을 버블 정렬로 오름차순 정렬하고,
#       몇 번의 교환(swap)이 발생했는지도 함께 출력하세요.
#
# 입력: 정수 리스트 scores
# 출력: 정렬된 리스트, 교환 횟수
#
# 예시:
#   [64, 34, 25, 12, 22, 11, 90]
#   정렬 결과: [11, 12, 22, 25, 34, 64, 90]
#   교환 횟수: ?번
# ================================================================================

def bubble_sort_with_count(scores):
    result = scores[:]
    n = len(result)
    swap_count = 0

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break

    return result, swap_count


if __name__ == "__main__":
    print("=== 버블 정렬 단계별 시각화 ===")
    arr = [5, 3, 8, 1, 2]
    temp = arr[:]
    n = len(temp)
    print(f"  초기 상태: {temp}")

    for i in range(n):
        for j in range(n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
        print(f"  {i+1}번째 순회 후: {temp}")

    print()
    print("=== 예제 문제: 시험 점수 정렬 ===")
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],       # 이미 정렬됨 (교환 0회)
        [5, 4, 3, 2, 1],       # 역순 정렬 (교환 최다)
    ]

    for scores in test_cases:
        sorted_scores, count = bubble_sort_with_count(scores)
        print(f"  입력:   {scores}")
        print(f"  결과:   {sorted_scores}")
        print(f"  교환 횟수: {count}번")
        print()

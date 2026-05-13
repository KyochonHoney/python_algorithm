"""
================================================================================
[09] 이진 탐색 (Binary Search)
================================================================================

## 개념
정렬된 배열에서 찾는 값의 범위를 절반씩 줄여가며 탐색하는 방법이에요.
전화번호부에서 이름을 찾을 때 중간 페이지를 펼쳐 앞/뒤로 이동하는 것과 같아요.

## 전제 조건
  반드시 정렬된 배열이어야 해요!

## 공식 (알고리즘 단계)
  1. 탐색 범위의 중간(mid)을 구한다    mid = (left + right) // 2
  2. arr[mid] == target → 찾음! 반환
  3. arr[mid] < target  → target은 오른쪽에 있음  →  left = mid + 1
  4. arr[mid] > target  → target은 왼쪽에 있음   →  right = mid - 1
  5. left > right 이면 탐색 실패 (-1 반환)

  T(n) = T(n/2) + O(1)  →  O(log n)

## 선형 탐색 vs 이진 탐색 비교
  n = 1,000,000 일 때:
    선형 탐색: 최대 1,000,000번 비교
    이진 탐색: 최대 20번 비교 (log₂(1,000,000) ≈ 20)

================================================================================
"""


# ===== 개념 코드: 이진 탐색 (반복문 버전) =====

def binary_search(arr, target):
    """
    정렬된 arr에서 target의 인덱스를 반환한다.
    없으면 -1을 반환한다.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid         # 찾음
        elif arr[mid] < target:
            left = mid + 1     # 오른쪽 절반 탐색
        else:
            right = mid - 1    # 왼쪽 절반 탐색

    return -1   # 없음


# ===== 응용: Lower Bound (같은 값 중 가장 왼쪽 인덱스) =====

def lower_bound(arr, target):
    """target 이상인 값이 처음 등장하는 인덱스를 반환한다."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 도서관에 책이 ISBN 번호 순서로 정렬되어 있어요.
#       사서가 특정 ISBN의 책이 있는지 찾고, 있다면 몇 번 선반에 있는지 알려주세요.
#       (선반 번호 = 인덱스 + 1)
#
# 입력: 정렬된 ISBN 리스트, 찾을 ISBN
# 출력: "N번 선반에 있습니다." 또는 "해당 책이 없습니다."
#
# 예시:
#   isbns = [1001, 1023, 1045, 1067, 1089, 1100, 1234]
#   찾는 ISBN: 1067  →  "4번 선반에 있습니다."
#   찾는 ISBN: 1050  →  "해당 책이 없습니다."
# ================================================================================

def find_book(isbns, target_isbn):
    idx = binary_search(isbns, target_isbn)
    if idx == -1:
        return f"ISBN {target_isbn}: 해당 책이 없습니다."
    return f"ISBN {target_isbn}: {idx + 1}번 선반에 있습니다."


if __name__ == "__main__":
    print("=== 이진 탐색 단계별 시각화 ===")
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    left, right = 0, len(arr) - 1
    step = 1

    print(f"  배열: {arr}")
    print(f"  찾는 값: {target}")
    while left <= right:
        mid = (left + right) // 2
        print(f"  [{step}단계] left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}", end="")
        if arr[mid] == target:
            print(f"  → 찾음! 인덱스 {mid}")
            break
        elif arr[mid] < target:
            print(f"  → 오른쪽으로")
            left = mid + 1
        else:
            print(f"  → 왼쪽으로")
            right = mid - 1
        step += 1

    print()
    print("=== 예제 문제: 도서관 ISBN 검색 ===")
    isbns = [1001, 1023, 1045, 1067, 1089, 1100, 1234]
    print(f"  선반 목록: {isbns}")
    print()
    for isbn in [1067, 1050, 1001, 1234, 9999]:
        print(f"  {find_book(isbns, isbn)}")

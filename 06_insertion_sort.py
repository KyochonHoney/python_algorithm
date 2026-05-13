"""
================================================================================
[06] 삽입 정렬 (Insertion Sort)
================================================================================

## 개념
카드를 손에 쥐고 정렬하는 방식과 같아요.
이미 정렬된 부분에 새 원소를 알맞은 위치에 '끼워 넣는' 방식으로 정렬해요.

## 공식 (알고리즘 단계)
  1. 두 번째 원소부터 시작한다 (첫 번째는 이미 정렬됨).
  2. 현재 원소(key)를 왼쪽 정렬 부분과 비교한다.
  3. key보다 큰 원소들을 오른쪽으로 한 칸씩 민다.
  4. 알맞은 위치에 key를 삽입한다.
  5. 다음 원소로 이동하여 반복한다.

  for i in range(1, n):
      key = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > key:
          arr[j + 1] = arr[j]    # 오른쪽으로 밀기
          j -= 1
      arr[j + 1] = key           # 알맞은 위치에 삽입

## 시간복잡도
  최선(이미 정렬됨): O(n)   — 비교만 하고 이동 없음
  평균/최악:         O(n²)

## 장점
  - 거의 정렬된 데이터에서 매우 빠름
  - 안정 정렬(Stable Sort): 같은 값의 순서가 유지됨
  - 제자리 정렬: 추가 메모리 O(1)

================================================================================
"""


# ===== 개념 코드: 삽입 정렬 =====

def insertion_sort(arr):
    """삽입 정렬로 arr을 오름차순 정렬하여 반환한다."""
    result = arr[:]
    n = len(result)

    for i in range(1, n):
        key = result[i]   # 삽입할 값
        j = i - 1

        # key보다 큰 원소를 오른쪽으로 한 칸씩 밀기
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key   # 알맞은 자리에 key 삽입

    return result


# ================================================================================
# 예제 문제
# ================================================================================
# 문제: 학생 이름과 점수 쌍의 리스트를 점수 기준 오름차순으로 정렬하세요.
#       단, 삽입 정렬을 사용하고 점수가 같은 경우 원래 순서를 유지하세요 (안정 정렬).
#
# 입력: [(이름, 점수), ...] 형태의 리스트
# 출력: 점수 기준 오름차순 정렬된 리스트 (점수 같으면 원래 순서 유지)
#
# 예시:
#   입력: [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Diana", 78)]
#   출력: [("Diana", 78), ("Alice", 85), ("Charlie", 85), ("Bob", 92)]
#   → Alice와 Charlie 점수 동일, 원래 순서(Alice → Charlie) 유지
# ================================================================================

def insertion_sort_students(students):
    result = students[:]
    n = len(result)

    for i in range(1, n):
        key = result[i]
        j = i - 1

        # 점수(인덱스 1)를 기준으로 비교
        while j >= 0 and result[j][1] > key[1]:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


if __name__ == "__main__":
    print("=== 삽입 정렬 단계별 시각화 ===")
    arr = [5, 2, 4, 6, 1, 3]
    temp = arr[:]
    n = len(temp)
    print(f"  초기 상태: {temp}")

    for i in range(1, n):
        key = temp[i]
        j = i - 1
        while j >= 0 and temp[j] > key:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = key
        print(f"  {i}번째 삽입 후 (key={key}): {temp}")

    print()
    print("=== 예제 문제: 학생 점수 안정 정렬 ===")
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Diana", 78)]
    print(f"  입력: {students}")
    sorted_students = insertion_sort_students(students)
    print(f"  결과: {sorted_students}")
    print()
    # Alice와 Charlie의 순서가 유지됐는지 확인
    names_85 = [name for name, score in sorted_students if score == 85]
    ok = "YES (OK)" if names_85[0] == 'Alice' else "NO (FAIL)"
    print(f"  점수 85인 학생 순서: {names_85}  ->  Alice가 Charlie보다 앞에 있나요? {ok}")

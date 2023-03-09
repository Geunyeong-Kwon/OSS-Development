# 선택 정렬
def sel_sort(a):
    n = len(a)
    b = [] # 빈 리스트 만들기
    while n > 1:
        x = max(a)
        a.remove(x)
        b = [x] + b
        n = n-1

    return b

# 재귀적 선택 정렬
def sel_sort_rec(a):
    # a에 원소가 있으면 재귀함수를 호출
    if a!= []:
        x = max(a) # 최대값과 최대값의 위치 찾기
        a.remove(x) # 최대값의 위치에 있는 원소 제거하기
        return sel_sort_rec(a) + [x]

    else:
        return []

a = [4, 3, 5, 1, 2, 6, 8, 9, 3, 5, 2, 6, 7]
print('입력 행렬', a)
b = sel_sort(a)
print('선택정렬 결과', b)

a = [4, 3, 5, 1, 2, 6, 8, 9, 3, 5, 2, 6, 7]
c = sel_sort_rec(a)
print('재귀버전 결과', c)

# reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
# 10~(10+60)70분 1번상담유형 
def solution(k, n, reqs): # 멘토 n(5)명, 1~k(3)의 상담유형, 
    dfs(k, n, 0, 0)
    answer = 0
    return answer

def cal(reqs):
    # 대기시간 리턴
    time = 0

array = [i for i in range(1, n+1)] # 멘토n명 
result = []    
visited = [False] *  
def dfs(k, n, depth, start): # k의 상담유형 멘토 n명  => 1~N까지 자연수 k의 조합   ex) 상담원a,b,c,d => 3개의조합 (a, b, cd)(a, bc, d)
    

    if depth == k:
        print(*result, seq=" ")
        return
    
    for i in range(start, n):


# 모든 경우의 수
# 먼저 상담 요청한 참가자가 우선됩니다.
# 단, 각 유형별로 멘토 인원이 적어도 한 명 이상이어야 합니다.
# reqs는 a를 기준으로 오름차순으로 정렬되어 있습니다.
# 1 ≤ k ≤ 5  상담유형
# k ≤ n ≤ 20 멘토

#---------------------------------
# 풀이방법
# 1)조합을 이용해 모든 배정가능한 경우의 수를 구한다 
# 2)최소시간을 계산한 후 가장 작은 최소시간을 리턴한다
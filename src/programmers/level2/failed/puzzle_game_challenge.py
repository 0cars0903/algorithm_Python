def solution(diffs, times, limit):
    def calculate_time(level):
        """주어진 숙련도로 모든 퍼즐을 푸는데 걸리는 총 시간 계산"""
        total_time = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1] if i > 0 else 0  # 첫 번째 퍼즐은 time_prev = 0
            
            if diff <= level:
                # 틀리지 않는 경우
                total_time += time_cur
            else:
                # 틀리는 경우
                mistakes = diff - level
                total_time += (time_cur + time_prev) * mistakes + time_cur
        
        return total_time
    
    # 이진 탐색으로 최소 숙련도 찾기
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if calculate_time(mid) <= limit:
            # 제한 시간 내에 해결 가능 -> 더 낮은 숙련도 시도
            answer = mid
            right = mid - 1
        else:
            # 제한 시간 초과 -> 더 높은 숙련도 필요
            left = mid + 1
    
    return answer
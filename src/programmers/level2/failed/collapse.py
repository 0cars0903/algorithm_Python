def solution(points, routes):
    # 2개의 포인트 사이의 최단경로 
    def get_path(start, end):
        r1, c1 = start
        r2, c2 = end
        path = [(r1, c1)]
        
        while r1 != r2:
            if r1 < r2:
                r1 += 1
            else:
                r1 -= 1
            path.append((r1, c1))
        
        while c1 != c2:
            if c1 < c2:
                c1 += 1
            else:
                c1 -= 1
            path.append((r1, c1))
            
        return path
    
    # 각 로봇의 전체 이동 경로 
    robot_path = []
    for route in routes:
        full_path = []
        
        for i in range(len(route)):
            point = points[route[i]-1]
            
            if i == 0:
                # ✅ Tuple의 의미: 딕셔너리 키로 사용하기 위해 불변(immutable) 타입 필요
                # 리스트 [1,2]는 해시 불가 → 딕셔너리 키 불가
                # 튜플 (1,2)는 해시 가능 → 딕셔너리 키 가능
                full_path.append(tuple(point))
                
            else:
                prev_point = points[route[i-1]-1]
                curr_point = point
                seg_path = get_path(prev_point, curr_point)
                
                # ❌ 오류: append 대신 extend 사용해야 함!
                # append: 리스트 자체를 원소로 추가 → [[좌표들]]
                # extend: 리스트의 각 원소를 추가 → [좌표1, 좌표2, ...]
                full_path.extend(seg_path[1:])  # 수정!
                
        robot_path.append(full_path)
    
    # 충돌 횟수 확인
    max_time = max(len(path) for path in robot_path)
    collapse = 0
    
    for i in range(max_time):
        pos_cnt = {}
        for path in robot_path:
            if i < len(path):
                pos = path[i]
                
                # ✅ pos_cnt.get(pos, 0) + 1의 의미:
                # get(key, default): key가 없으면 default 반환
                # 있으면 해당 값 반환 → +1 해서 다시 저장
                pos_cnt[pos] = pos_cnt.get(pos, 0) + 1
                
        for cnt in pos_cnt.values():
            if cnt >= 2:
                collapse += 1
                
    return collapse    

# collections 모듈에서 Counter 사용 예시

from collections import Counter

def solution(points, routes):
    maps = {}  # {좌표: [방문 시간들]}
    
    for route in routes:  # 각 로봇마다
        time = 0
        y, x = points[route[0] - 1]  # 시작 위치
        
        # ✅ setdefault: 키가 없으면 빈 리스트 생성 후 append
        # maps.get(key, []).append()는 안 됨! (새 리스트에 추가되고 사라짐)
        maps.setdefault((y, x), []).append(time)
        
        for i in range(1, len(route)):
            end_y, end_x = points[route[i] - 1]
            
            # 1단계: r 좌표 이동
            step = 1 if y < end_y else -1
            for y in range(y + step, end_y + step, step):
                time += 1
                maps.setdefault((y, x), []).append(time)
            
            # 2단계: c 좌표 이동
            step = 1 if x < end_x else -1
            for x in range(x + step, end_x + step, step):
                time += 1
                maps.setdefault((end_y, x), []).append(time)
    
    # 🔥 핵심: 각 좌표별로 같은 시간에 2대 이상 있었는지 확인
    return sum(
        sum(1 for counter in Counter(values).values() if counter > 1)
        for values in maps.values()
    )
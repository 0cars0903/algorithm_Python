def solution(bandage, health, attacks):
    health_state = health
    for i in range(len(attacks)-1):
        health_state -= attacks[i][1]
        if health_state <= 0:
            return -1 
        else:
            cond = (attacks[i+1][0] - attacks[i][0]) - 1
            bandage_buff = cond // bandage[0]
            HP = cond * bandage[1] + bandage_buff * bandage[2]
            health_state += HP
            health_state = min(health_state, health)

    health_state -= attacks[-1][1]
    if health_state <= 0:
        return -1 
    else:
        return health_state
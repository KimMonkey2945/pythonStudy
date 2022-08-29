def solution(bridge_length, weight, truck_weights):
    answer = 0 # second
    bridge = [0]*bridge_length # 지나가는 다리위를 0으로 채운다.

    while bridge: # 다리가 비어있을 때 까지
        answer += 1 # 시간은 흘러가도록
        bridge.pop(0) # 다리에 올라가야 되므로 하나 빼준다
        if truck_weights: # 대기 트럭에서 하나씩 가져오기
            if sum(bridge) + truck_weights[0] <= weight: # 현재 다리위의 무게와 대기트럭의 처번째 트럭 무게가 제한 무게가 넘지 않으면
                bridge.append(truck_weights.pop(0)) # 다리 위로 올라감.
            else:
                bridge.append(0) # 아니면 0을 채우고 다리를 건넌다
    return answer

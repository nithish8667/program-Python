def min_walking_distance(n, gates, distances):
    spot_positions = [0] * (n + 1)
    for i in range(1, n):
        spot_positions[i] = spot_positions[i - 1] + distances[i - 1]
    total_min_distance = 0
    for gate_position, num_fishermen in gates:
        spot_distances = [abs(spot_position - gate_position) for spot_position in spot_positions]
        sorted_spots = sorted(range(n), key=lambda i: spot_distances[i])
        assigned_spots = [False] * n
        min_distance = float('inf')       
        for i in range(num_fishermen):
            if i < n:
                spot_idx = sorted_spots[i]
                assigned_spots[spot_idx] = True
                distance_to_spot = spot_distances[spot_idx]
                if i == num_fishermen - 1:  
                    min_distance = min(min_distance, distance_to_spot)
                else:
                    total_min_distance += distance_to_spot
        if num_fishermen > n:
            total_min_distance += min_distance
    return total_min_distance
n = 5
gates = [(1, 3), (4, 2), (7, 2)]
distances = [2, 3, 4, 2]
print(min_walking_distance(n, gates, distances))  

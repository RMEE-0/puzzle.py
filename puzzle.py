import heapq

goal_state = [[0,1,4],
              [3,7,6],
              [5,2,8]]  


def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j]-1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance


def state_to_tuple(state):
    return tuple(num for row in state for num in row)


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def neighbors(state):
    x, y = find_zero(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state


def astar(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))  
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path + [state]

        state_tuple = state_to_tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor in neighbors(state):
            heapq.heappush(pq, (g+1+manhattan(neighbor), g+1, neighbor, path+[state]))
    return None


def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()


def play_game():
    
    start_state = [[2,8,3],
                   [1,6,4],
                   [7,0,5]]

    print("Start State:")
    print_state(start_state)

    print("Solving puzzle with A* search...")
    solution = astar(start_state)

    if not solution:
        print("No solution found.")
        return

    print(f"Solved in {len(solution)-1} moves!")
    for step in solution:
        print_state(step)

if __name__ == "__main__":
    play_game()
from collections import deque


def help_xy(red):
    return red/8, red % 8


def bfs(x, y, k):
    q = deque([(x, y)])
    while q:
        x_s, y_s = q.popleft()
        for dx in [-2, -1, 1, 2]:
            for dy in [-2, -1, 1, 2]:
                if abs(dx) == abs(dy):
                    continue
                x_t, y_t = x_s + dx, y_s + dy
                if 0 <= x_t <= 7 and 0 <= y_t <= 7:
                    if k[x_t][y_t] is None:
                        k[x_t][y_t] = k[x_s][y_s] + 1
                        q.append((x_t, y_t))


def answer(src, dest):
    # using BFS
    k = [[None for _ in range(8)] for _ in range(8)]
    x, y = help_xy(src)
    dx, dy = help_xy(dest)

    k[x][y] = 0
    bfs(x, y, k)
    return k[dx][dy]


# test case 1
print answer(19, 36)

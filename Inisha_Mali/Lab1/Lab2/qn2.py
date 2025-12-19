import matplotlib.pyplot as plt

def dda_line(x0, y0, x1, y1):
    points = []

    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        return [(x0, y0)]

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

def bresenham_line(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    x, y = x0, y0
    while True:
        points.append((x, y))

        if x == x1 and y == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points

if __name__ == "__main__":
    x0, y0 = 2, 2
    x1, y1 = 18, 10

    dda_pts = dda_line(x0, y0, x1, y1)
    bre_pts = bresenham_line(x0, y0, x1, y1)

    # Separate X and Y
    dda_x = [p[0] for p in dda_pts]
    dda_y = [p[1] for p in dda_pts]

    bre_x = [p[0] for p in bre_pts]
    bre_y = [p[1] for p in bre_pts]

    plt.figure(figsize=(7,7))

    # DDA curve
    plt.plot(dda_x, dda_y, marker='o', label="DDA (curve joining points)")

    # Bresenham curve
    plt.plot(bre_x, bre_y, marker='s', label="Bresenham (curve joining points)")

    plt.title("DDA and Bresenham Line Algorithms (Curves Only)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.gca().set_aspect("equal", adjustable="box")

    plt.show()

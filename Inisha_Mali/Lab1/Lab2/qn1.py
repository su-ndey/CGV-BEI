import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    """Return (x, y) points for Bresenham's Line Algorithm."""
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    x, y = x1, y1

    while True:
        points.append((x, y))

        if x == x2 and y == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x += sx

        if e2 < dx:
            err += dx
            y += sy

    return points


# ---------------------- MAIN PROGRAM ---------------------- #

x1, y1 = 2, 4
x2, y2 = 15, 10

# Generate Bresenham points
points = bresenham(x1, y1, x2, y2)

# Convert to x and y lists
xs = [p[0] for p in points]
ys = [p[1] for p in points]

print("Bresenham Points:")
for p in points:
    print(p)

# Plot Bresenham points AND connect them with a line
plt.figure(figsize=(7, 7))

plt.plot(xs, ys, color="purple", linewidth=2, marker="o", label="Bresenham Line")

plt.title("Bresenham Line (Connected Points Only)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Pixel-style axes
# plt.xticks(range(min(xs)-1, max(xs)+2))
# plt.yticks(range(min(ys)-1, max(ys)+2))
# plt.gca().invert_yaxis()

plt.legend()
plt.show()
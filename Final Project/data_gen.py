import random

# Parametres
d = 50
m = 10000
coordinate_range = (-10, 10)

# Generate m random points with dimensions d and save to database.txt
with open("database.txt", "w") as f:
    for i in range(m):
        point = [random.randint(*coordinate_range) for j in range(d)]
        f.write(",".join(map(str, point)) + "\n")

print(f"{m} random points generated and saved to database.txt.")

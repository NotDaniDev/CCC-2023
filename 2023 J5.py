# Read input
word = input()
n_rows = int(input())
n_cols = int(input())
grid = [input().split() for _ in range(n_rows)]

# Define helper function to check for matches in a given direction
def check_direction(r, c, dr, dc):
    for char in word:
        if not (0 <= r < n_rows and 0 <= c < n_cols and grid[r][c] == char):
            return False
        r += dr
        c += dc
    return True

# Iterate over all possible starting positions and directions
matches = 0
for r in range(n_rows):
    for c in range(n_cols):
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            if check_direction(r, c, dr, dc):
                matches += 1
            if len(word) > 1 and check_direction(r, c, dc, dr):
                matches += 1

# Output number of matches found
print(matches)






"""NATURE
6
9
N A T S F E G Q N
S A I B M R H F A
C F T J C U C L T
K B H U P T A N U
D P R R R J D I R
I E E K M E G B E"""

"""MENU
5
7
F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S"""
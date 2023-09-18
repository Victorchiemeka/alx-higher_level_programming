def display(self):
    """Display the value of #"""
    grid = [["#" for _ in range(self.x)] for _ in range(self.y)]
    for row in grid:
        print("".join(row))


display(4, 6)

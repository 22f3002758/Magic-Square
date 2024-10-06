import random
import streamlit as st

# Function to check if the current grid forms a magic square
def is_magic_square(grid, size):
    magic_sum = size * (size**2 + 1) // 2  # Magic constant for the grid
    # Check rows and columns
    for i in range(size):
        if sum(grid[i]) != magic_sum or sum([row[i] for row in grid]) != magic_sum:
            return False
    # Check diagonals
    if sum([grid[i][i] for i in range(size)]) != magic_sum or sum([grid[i][size-i-1] for i in range(size)]) != magic_sum:
        return False
    return True

def main():
    st.title("Magic Square Game")
    
    grid_size = st.selectbox("Choose grid size:", [3, 4, 5])
    
    # Create the grid
    grid = []
    for i in range(grid_size):
        row = []
        cols = st.columns(grid_size)
        for j in range(grid_size):
            user_input = cols[j].text_input(f'Row {i+1}, Col {j+1}', '')
            # Check if input is valid integer
            if user_input.isdigit():
                row.append(int(user_input))
            else:
                row.append(0)  # Default to 0 if input is invalid
        grid.append(row)
    
    if st.button("Check"):
        if all(all(isinstance(x, int) and x > 0 for x in row) for row in grid) and is_magic_square(grid, grid_size):
            st.success("Congratulations! You formed a Magic Square!")
        else:
            st.error("This is not a Magic Square. Try again!")
    
if __name__ == "__main__":
    main()

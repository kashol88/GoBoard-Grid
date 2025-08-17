"""
Go Board Generator - Creates a 19x19 Go board PDF with standard dimensions
Created by [Your Name] - Free to use and modify
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Conversion constant
MM_TO_PT = 72 / 25.4

# 19x19 Go board - EXACT specifications
h_spacing_mm = 22.00                    # Horizontal spacing between adjacent lines
v_spacing_mm = 23.70                    # Vertical spacing between adjacent lines
grid_width_mm = 396.00                  # Grid width (18 spaces)
grid_height_mm = 426.60                 # Grid height (18 spaces)
board_width_mm = 424.20                 # Board outer width
board_height_mm = 454.50                # Board outer length
side_margin_mm = 14.10                  # Side margins (edge to outermost line center)
top_bottom_margin_mm = 13.95            # Top/bottom margins (edge to outermost line center)
line_thickness_mm = 1.00                # Line thickness
hoshi_diameter_mm = 4.00                # Hoshi (star point) diameter

# Convert to points
h_spacing = h_spacing_mm * MM_TO_PT
v_spacing = v_spacing_mm * MM_TO_PT
grid_width = grid_width_mm * MM_TO_PT
grid_height = grid_height_mm * MM_TO_PT
board_width = board_width_mm * MM_TO_PT
board_height = board_height_mm * MM_TO_PT
side_margin = side_margin_mm * MM_TO_PT
top_bottom_margin = top_bottom_margin_mm * MM_TO_PT
line_thickness = line_thickness_mm * MM_TO_PT
hoshi_radius = (hoshi_diameter_mm * MM_TO_PT) / 2

# Custom page size to fit the board exactly
PAGE_WIDTH = board_width + 20 * MM_TO_PT    # Add 20mm margin around board
PAGE_HEIGHT = board_height + 20 * MM_TO_PT  # Add 20mm margin around board

print(f"Board size: {board_width_mm}mm × {board_height_mm}mm")
print(f"Page size: {PAGE_WIDTH/MM_TO_PT:.1f}mm × {PAGE_HEIGHT/MM_TO_PT:.1f}mm")

# Hoshi positions (columns 4, 10, 16 / rows 4, 10, 16) - 0-indexed as 3, 9, 15
hoshi_positions = [
    (3, 3), (3, 9), (3, 15),    # Left column
    (9, 3), (9, 9), (9, 15),    # Center column
    (15, 3), (15, 9), (15, 15)  # Right column
]

# Create PDF with custom page size
c = canvas.Canvas("go_board_19x19_single.pdf", pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
c.setLineWidth(line_thickness)

# Center the board on the page
board_x = (PAGE_WIDTH - board_width) / 2
board_y = (PAGE_HEIGHT - board_height) / 2

# Grid starting position (top-left of grid, accounting for margins)
grid_x = board_x + side_margin
grid_y = board_y + board_height - top_bottom_margin  # Start from top

print("Drawing 19×19 Go board...")

# Draw 19 vertical lines (columns 1-19)
for i in range(19):
    x = grid_x + i * h_spacing
    y_start = grid_y - grid_height  # Bottom of grid
    y_end = grid_y                  # Top of grid
    c.line(x, y_start, x, y_end)
    print(f"Vertical line {i+1}: x={x/MM_TO_PT:.2f}mm")

# Draw 19 horizontal lines (rows 1-19)
for j in range(19):
    y = grid_y - j * v_spacing      # Start from top, go down
    x_start = grid_x                # Left of grid
    x_end = grid_x + grid_width     # Right of grid
    c.line(x_start, y, x_end, y)
    print(f"Horizontal line {j+1}: y={(board_y + board_height - y)/MM_TO_PT:.2f}mm from top")

# Draw outer border rectangle
border_x = board_x
border_y = board_y
c.rect(border_x, border_y, board_width, board_height, fill=0, stroke=1)

# Draw hoshi (star) points
print("Drawing hoshi points...")
for col, row in hoshi_positions:
    x = grid_x + col * h_spacing
    y = grid_y - row * v_spacing
    c.circle(x, y, hoshi_radius, fill=1, stroke=0)
    
    # Calculate actual coordinates from left and top edges
    x_from_left = side_margin_mm + col * h_spacing_mm
    y_from_top = top_bottom_margin_mm + row * v_spacing_mm
    print(f"Hoshi at column {col+1}, row {row+1}: ({x_from_left:.2f}mm, {y_from_top:.2f}mm)")

c.save()
print(f"\nPDF created: go_board_19x19_single.pdf")
print(f"Board dimensions: {board_width_mm}mm × {board_height_mm}mm")
print("Ready for large format printing!")

# Verify measurements
print(f"\nVerification:")
print(f"Grid: {grid_width_mm}mm × {grid_height_mm}mm")
print(f"Side margins: {side_margin_mm}mm each")
print(f"Top/bottom margins: {top_bottom_margin_mm}mm each")
print(f"Total board: {side_margin_mm*2 + grid_width_mm}mm × {top_bottom_margin_mm*2 + grid_height_mm}mm")
print(f"Expected: {board_width_mm}mm × {board_height_mm}mm")
"""
Go Board Generator - Creates a 9x9 Go board PDF with minimum line thickness
Created by [Your Name] - Free to use and modify
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Page size
PAGE_WIDTH, PAGE_HEIGHT = A4  # A4 in points (1 point = 1/72 inch)

# Conversion constant
MM_TO_PT = 72 / 25.4  # 1 mm = 2.83465 points

# Measurements in mm
h_spacing_mm = 22.00
v_spacing_mm = 23.70
left_right_margin_mm = 14.55  # 14.10 + 0.45 to compensate for thinner lines
top_bottom_margin_mm = 14.40  # 13.95 + 0.45 to compensate for thinner lines
line_thickness_mm = 0.1  # Minimum thickness a printer can print (0.1mm)
hoshi_diameter_mm = 4.00

# Convert to points
h_spacing = h_spacing_mm * MM_TO_PT
v_spacing = v_spacing_mm * MM_TO_PT
left_margin = left_right_margin_mm * MM_TO_PT
top_margin = top_bottom_margin_mm * MM_TO_PT
line_thickness = line_thickness_mm * MM_TO_PT
hoshi_radius = (hoshi_diameter_mm * MM_TO_PT) / 2

# 9x9 grid
num_lines = 9
grid_width = (num_lines - 1) * h_spacing
grid_height = (num_lines - 1) * v_spacing

# Calculate total board size with SINGLE margins (edge to outermost line center)
# 14.10mm left/right, 13.95mm top/bottom from edge to line center
total_width = grid_width + 2 * left_margin  # Grid + 14.10mm on each side
total_height = grid_height + 2 * top_margin  # Grid + 13.95mm on each side

# Center the entire board on A4 paper
board_center_x = (PAGE_WIDTH - total_width) / 2
board_center_y = (PAGE_HEIGHT - total_height) / 2

# Position grid (inner part) - single margins from edge
x_start = board_center_x + left_margin
y_start = board_center_y + top_margin

# Create canvas
c = canvas.Canvas("go_board_9x9_min_thickness.pdf", pagesize=A4)
c.setLineWidth(line_thickness)

# Vertical lines
for i in range(num_lines):
    x = x_start + i * h_spacing
    c.line(x, y_start, x, y_start + grid_height)

# Horizontal lines
for j in range(num_lines):
    y = y_start + j * v_spacing
    c.line(x_start, y, x_start + grid_width, y)

# Single border around the board (at the edge, 14.10/13.95mm from grid)
border_x = board_center_x
border_y = board_center_y
c.rect(border_x, border_y, total_width, total_height, fill=0, stroke=1)

# Additional line above the top border (14.55mm above)
additional_margin_pt = 14.55 * MM_TO_PT
top_line_y = border_y + total_height + additional_margin_pt
c.line(border_x, top_line_y, border_x + total_width, top_line_y)

# Star points (hoshi) for 9x9 board - standard 5 points
# 9x9 has 5 star points: 4 corners + center
# Positions: (2,2), (2,6), (6,2), (6,6), (4,4) in 0-indexed coordinates
hoshi_positions = [
    (2, 2),  # Top-left
    (2, 6),  # Top-right  
    (6, 2),  # Bottom-left
    (6, 6),  # Bottom-right
    (4, 4)   # Center
]

for hoshi_x, hoshi_y in hoshi_positions:
    x = x_start + hoshi_x * h_spacing
    y = y_start + hoshi_y * v_spacing
    c.circle(x, y, hoshi_radius, fill=1, stroke=0)

# Add text at bottom of page showing grid spacing and outline sizes
c.setFont("Helvetica", 8)
text_y_position = 30  # Start position from bottom of page

# Grid spacing information
grid_text = f"Grid Size: {num_lines}x{num_lines} | Grid Spacing: {h_spacing_mm}mm x {v_spacing_mm}mm"
c.drawString(50, text_y_position, grid_text)

# Top/bottom outline size
text_y_position -= 12
outline_tb_text = f"Top/Bottom Outline: {top_bottom_margin_mm}mm"
c.drawString(50, text_y_position, outline_tb_text)

# Left/right outline size
text_y_position -= 12
outline_lr_text = f"Left/Right Outline: {left_right_margin_mm}mm"
c.drawString(50, text_y_position, outline_lr_text)

# Save PDF
c.save()
print("PDF created: go_board_9x9_min_thickness.pdf")
# GoBoard-Grid

A collection of Python scripts to generate printable Go (Weiqi/Baduk) board PDFs with accurate dimensions and customizable standards.

## Programs

### go_board_generator.py
Creates a **9x9 Go board** with Japanese standard dimensions (22.0mm x 23.7mm spacing). Includes detailed customization instructions for adapting to different international standards (Chinese, Korean, etc.).

### go_board_19x19_single.py  
Generates a **19x19 Go board** with standard dimensions on letter-size paper. Perfect for full-size tournament play.

**Printing note for 19x19 board only:** To print the 19x19 board at correct dimensions, open the PDF in a PDF viewer and set printer settings to "Poster" mode. This will automatically split the large board across multiple A4 pages with proper scaling. The 9x9 boards print normally on single pages.

### go_board_generator_min_thickness.py
Creates a **9x9 Go board** with minimum line thickness for lighter printing or specific printer requirements.

## Features
- Accurate measurements in millimeters
- Star points (hoshi) correctly positioned
- Customizable grid spacing for different standards
- Professional PDF output ready for printing
- Clear grid dimension annotations

## Requirements

- **Python 3.6+**
- **ReportLab** module for PDF generation

## Installation

1. Install Python from [python.org](https://python.org) (version 3.6 or higher)

2. Install ReportLab using pip:
```bash
pip install reportlab
```

## Usage

Run any script from the terminal:

```bash
python go_board_generator.py
python go_board_19x19_single.py  
python go_board_generator_min_thickness.py
```

Each script will generate a PDF file in the same directory.

## Customization

To modify board dimensions, edit the measurement variables at the top of each script:

```python
h_spacing_mm = 22.00    # Horizontal line spacing
v_spacing_mm = 23.70    # Vertical line spacing
```

**Common international standards:**
- Japanese: 22.0mm x 23.7mm
- Chinese: 23.0mm x 23.0mm  
- Korean: 22.5mm x 23.0mm

## Author

Created by Kasper Holm - Free to use and modify

## License

Open source - feel free to use, modify, and distribute
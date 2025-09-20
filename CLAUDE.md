# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python application for generating interactive Sankey diagrams from CSV data using Plotly. The project uses `uv` as the package manager and creates beautiful, interactive visualizations that can be exported to multiple formats.

## Commands

### Development Commands
- `uv sync` - Install/sync dependencies
- `uv run python main.py --sample --open` - Generate sample diagram and open in browser
- `uv run python main.py --csv <file>` - Generate diagram from CSV file
- `uv run python main.py --csv <file> --format png --output diagram.png` - Export as image

### Testing
- No test framework is currently configured in this project

## Architecture

### Core Components

**SankeyDiagramGenerator Class** (`main.py:9-122`)
- Main class handling the entire diagram generation pipeline
- `load_csv()` - Validates and loads CSV data with required columns: source, target, value
- `prepare_sankey_data()` - Converts CSV to Plotly format with node mapping
- `create_sankey_diagram()` - Generates the interactive Plotly figure with styling
- `save_html()` - Exports interactive HTML files
- `save_image()` - Exports static images (PNG, SVG, PDF) using kaleido

### Data Format Requirements
CSV files must contain exactly three columns:
- `source` - Source node name (string)
- `target` - Target node name (string)
- `value` - Flow value (numeric)

### Dependencies
- `plotly>=5.0.0` - Core visualization library
- `pandas>=2.0.0` - Data manipulation and CSV handling
- `kaleido>=0.2.1` - Required for static image export (PNG, SVG, PDF)

### Output Formats
- HTML (default) - Interactive diagrams with hover, drag, zoom capabilities
- PNG/SVG/PDF - Static images for presentations, requires kaleido package

### Color System
The application uses a predefined color palette (`main.py:12-15`) with automatic node coloring and semi-transparent link colors derived from source nodes.

### Error Handling
- CSV validation for required columns and data types
- Graceful handling of missing/invalid data with dropna()
- Clear error messages for common issues like missing files or invalid formats
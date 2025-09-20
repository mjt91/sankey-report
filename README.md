# Sankey Report Generator

A beautiful Python application for creating interactive Sankey diagrams from CSV data using Plotly.

## Features

- 🎨 Beautiful, interactive Sankey diagrams
- 📊 Load data from CSV files
- 🌐 Interactive browser visualization
- 💾 Export to multiple formats (HTML, PNG, SVG, PDF)
- ⚙️ Fully customizable titles, dimensions, and styling
- 📱 Responsive design for different screen sizes

## Installation

This project uses `uv` as the package manager:

```bash
uv sync
```

## Usage

### Quick Start

Generate a sample Sankey diagram:

```bash
uv run python main.py --sample --open
```

This creates `sample_sankey_data.csv` and opens an interactive diagram in your browser.

### Basic Usage

```bash
uv run python main.py --csv your_data.csv
```

### Advanced Usage

```bash
uv run python main.py \
  --csv your_data.csv \
  --title "My Custom Sankey Diagram" \
  --output my_diagram.html \
  --width 1400 \
  --height 900 \
  --open
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--csv` | Path to CSV file (required) | - |
| `--title` | Chart title | "Sankey Diagram" |
| `--output` | Output file path | "sankey_diagram.html" |
| `--width` | Chart width in pixels | 1200 |
| `--height` | Chart height in pixels | 800 |
| `--format` | Output format (html, png, svg, pdf) | html |
| `--sample` | Create sample CSV data | - |
| `--open` | Open diagram in browser | - |

### CSV Data Format

Your CSV file must contain three columns:

| Column | Description | Example |
|--------|-------------|---------|
| `source` | Source node name | "Marketing" |
| `target` | Target node name | "Sales" |
| `value` | Flow value (numeric) | 150 |

#### Example CSV:

```csv
source,target,value
Marketing,Sales,150
Marketing,Support,50
Sales,Revenue,120
Support,Revenue,30
R&D,Product,200
Product,Sales,180
```

### Export Formats

#### Interactive HTML (Default)
```bash
uv run python main.py --csv data.csv --format html --open
```

#### Static Images
```bash
# PNG
uv run python main.py --csv data.csv --format png --output diagram.png

# SVG
uv run python main.py --csv data.csv --format svg --output diagram.svg

# PDF
uv run python main.py --csv data.csv --format pdf --output diagram.pdf
```

### Examples

#### 1. Business Process Flow
```csv
source,target,value
Leads,Qualified,1000
Leads,Unqualified,500
Qualified,Opportunity,800
Qualified,Lost,200
Opportunity,Closed Won,300
Opportunity,Closed Lost,500
```

```bash
uv run python main.py --csv business_flow.csv --title "Sales Funnel Analysis" --open
```

#### 2. Budget Allocation
```csv
source,target,value
Budget,Marketing,50000
Budget,Engineering,80000
Budget,Operations,30000
Marketing,Digital Ads,30000
Marketing,Events,20000
Engineering,Development,60000
Engineering,QA,20000
```

```bash
uv run python main.py --csv budget.csv --title "Budget Allocation 2024" --width 1600 --height 1000
```

#### 3. Energy Flow
```csv
source,target,value
Solar,Battery,40
Wind,Battery,30
Battery,Home,50
Battery,Grid,20
Grid,Home,30
```

```bash
uv run python main.py --csv energy.csv --title "Home Energy Flow" --format png --output energy_flow.png
```

## Features Explained

### Interactive Elements
- **Hover tooltips**: Show exact values and node names
- **Drag nodes**: Rearrange diagram layout
- **Zoom and pan**: Navigate large diagrams
- **Responsive**: Adapts to different screen sizes

### Customization
- **Colors**: Automatically assigned beautiful color palette
- **Transparency**: Links have semi-transparent colors for better visibility
- **Layout**: Plotly's automatic layout optimization
- **Typography**: Clean, readable fonts

### Data Processing
- **Automatic validation**: Checks for required columns
- **Data cleaning**: Removes invalid/missing values
- **Type conversion**: Converts values to numeric format
- **Error handling**: Clear error messages for invalid data

## Troubleshooting

### Common Issues

1. **"No module named 'pandas'"**
   ```bash
   uv sync
   ```

2. **"CSV must contain columns: ['source', 'target', 'value']"**
   - Check your CSV has the exact column names
   - Ensure no extra spaces in column headers

3. **"Error saving image"**
   - Kaleido package is required for image export
   - It should be automatically installed with dependencies

4. **Empty diagram**
   - Check your data has valid numeric values
   - Ensure source and target nodes are properly connected

### Performance Tips

- For large datasets (>1000 flows), consider aggregating similar flows
- Use HTML format for best interactivity
- PNG/SVG formats work better for presentations
- Increase width/height for complex diagrams

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with sample data
5. Submit a pull request

## License

MIT License - feel free to use and modify as needed!
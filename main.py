import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
import argparse
import sys
from pathlib import Path


class SankeyDiagramGenerator:
    def __init__(self):
        self.data = None
        self.colors = [
            '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
        ]

    def load_csv(self, file_path):
        """Load CSV data. Expected format: source,target,value"""
        try:
            self.data = pd.read_csv(file_path)

            # Validate required columns
            required_cols = ['source', 'target', 'value']
            if not all(col in self.data.columns for col in required_cols):
                raise ValueError(f"CSV must contain columns: {required_cols}")

            # Convert value column to numeric
            self.data['value'] = pd.to_numeric(self.data['value'], errors='coerce')

            # Remove rows with NaN values
            self.data = self.data.dropna()

            print(f"✓ Loaded {len(self.data)} records from {file_path}")
            return True

        except Exception as e:
            print(f"✗ Error loading CSV: {e}")
            return False

    def prepare_sankey_data(self):
        """Convert CSV data to Plotly Sankey format"""
        if self.data is None:
            raise ValueError("No data loaded. Call load_csv() first.")

        # Get unique nodes
        all_nodes = list(set(self.data['source'].tolist() + self.data['target'].tolist()))
        node_dict = {node: i for i, node in enumerate(all_nodes)}

        # Map source and target to node indices
        sources = [node_dict[source] for source in self.data['source']]
        targets = [node_dict[target] for target in self.data['target']]
        values = self.data['value'].tolist()

        return {
            'nodes': all_nodes,
            'sources': sources,
            'targets': targets,
            'values': values
        }

    def create_sankey_diagram(self, title="Sankey Diagram", width=1200, height=800):
        """Create beautiful interactive Sankey diagram"""
        sankey_data = self.prepare_sankey_data()

        # Create node colors
        node_colors = [self.colors[i % len(self.colors)] for i in range(len(sankey_data['nodes']))]

        # Create link colors (semi-transparent versions of source node colors)
        link_colors = []
        for source_idx in sankey_data['sources']:
            base_color = self.colors[source_idx % len(self.colors)]
            # Convert to RGBA with transparency
            if base_color.startswith('#'):
                r = int(base_color[1:3], 16)
                g = int(base_color[3:5], 16)
                b = int(base_color[5:7], 16)
                link_colors.append(f'rgba({r},{g},{b},0.4)')
            else:
                link_colors.append(base_color)

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=sankey_data['nodes'],
                color=node_colors
            ),
            link=dict(
                source=sankey_data['sources'],
                target=sankey_data['targets'],
                value=sankey_data['values'],
                color=link_colors
            )
        )])

        fig.update_layout(
            title_text=title,
            title_x=0.5,
            font_size=12,
            width=width,
            height=height,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )

        return fig

    def save_html(self, fig, output_path="sankey_diagram.html"):
        """Save diagram as interactive HTML file"""
        pyo.plot(fig, filename=output_path, auto_open=False)
        print(f"✓ Saved interactive diagram to {output_path}")

    def save_image(self, fig, output_path="sankey_diagram.png", format="png"):
        """Save diagram as static image"""
        try:
            fig.write_image(output_path, format=format, width=1200, height=800, scale=2)
            print(f"✓ Saved static image to {output_path}")
        except Exception as e:
            print(f"✗ Error saving image: {e}")
            print("Note: Image export requires kaleido package")


def create_sample_data():
    """Create sample CSV data for demonstration"""
    sample_data = pd.DataFrame({
        'source': ['A', 'A', 'B', 'B', 'C', 'C', 'D'],
        'target': ['B', 'C', 'D', 'E', 'D', 'E', 'F'],
        'value': [10, 15, 8, 12, 5, 7, 20]
    })
    sample_data.to_csv('sample_sankey_data.csv', index=False)
    print("✓ Created sample_sankey_data.csv")


def main():
    parser = argparse.ArgumentParser(description='Generate beautiful Sankey diagrams from CSV data')
    parser.add_argument('--csv', type=str, help='Path to CSV file (columns: source,target,value)')
    parser.add_argument('--output', type=str, default='sankey_diagram.html', help='Output file path')
    parser.add_argument('--title', type=str, default='Sankey Diagram', help='Chart title')
    parser.add_argument('--width', type=int, default=1200, help='Chart width')
    parser.add_argument('--height', type=int, default=800, help='Chart height')
    parser.add_argument('--format', type=str, choices=['html', 'png', 'svg', 'pdf'], default='html',
                        help='Output format')
    parser.add_argument('--sample', action='store_true', help='Create sample CSV data')
    parser.add_argument('--open', action='store_true', help='Open diagram in browser')

    args = parser.parse_args()

    # Create sample data if requested
    if args.sample:
        create_sample_data()
        if not args.csv:
            args.csv = 'sample_sankey_data.csv'

    # Check if CSV file is provided
    if not args.csv:
        print("Error: Please provide a CSV file with --csv or use --sample to create sample data")
        parser.print_help()
        sys.exit(1)

    # Check if file exists
    if not Path(args.csv).exists():
        print(f"Error: File {args.csv} not found")
        sys.exit(1)

    # Generate Sankey diagram
    generator = SankeyDiagramGenerator()

    if not generator.load_csv(args.csv):
        sys.exit(1)

    print(f"Creating {args.format} diagram...")
    fig = generator.create_sankey_diagram(title=args.title, width=args.width, height=args.height)

    # Save in requested format
    if args.format == 'html':
        generator.save_html(fig, args.output)
        if args.open:
            import webbrowser
            webbrowser.open(f'file://{Path(args.output).absolute()}')
    else:
        generator.save_image(fig, args.output, format=args.format)

    print("✓ Done!")


if __name__ == "__main__":
    main()

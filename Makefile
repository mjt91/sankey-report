# Sankey Report Generator - Example Targets

# Default target
.PHONY: all
all: business-flow budget energy

# Individual example targets
.PHONY: business-flow
business-flow:
	uv run python main.py --csv business_flow.csv --title "Sales Funnel Analysis" --open

.PHONY: budget
budget:
	uv run python main.py --csv budget.csv --title "Budget Allocation 2024" --width 1600 --height 1000

.PHONY: energy
energy:
	uv run python main.py --csv energy.csv --title "Home Energy Flow" --format png --output energy_flow.png

# Export variants
.PHONY: business-flow-png
business-flow-png:
	uv run python main.py --csv business_flow.csv --title "Sales Funnel Analysis" --format png --output business_flow.png

.PHONY: budget-html
budget-html:
	uv run python main.py --csv budget.csv --title "Budget Allocation 2024" --width 1600 --height 1000 --open

.PHONY: energy-html
energy-html:
	uv run python main.py --csv energy.csv --title "Home Energy Flow" --open

# Generate sample data
.PHONY: sample
sample:
	uv run python main.py --sample --open

# Clean generated files
.PHONY: clean
clean:
	rm -f *.html *.png *.svg *.pdf sample_sankey_data.csv

# Setup project
.PHONY: setup
setup:
	uv sync

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all              - Run all examples (business-flow, budget, energy)"
	@echo "  business-flow    - Generate sales funnel analysis (opens in browser)"
	@echo "  budget          - Generate budget allocation diagram"
	@echo "  energy          - Generate energy flow diagram (PNG output)"
	@echo "  business-flow-png - Export business flow as PNG"
	@echo "  budget-html     - Generate budget diagram and open in browser"
	@echo "  energy-html     - Generate energy diagram and open in browser"
	@echo "  sample          - Generate sample data and diagram"
	@echo "  clean           - Remove generated files"
	@echo "  setup           - Install dependencies"
	@echo "  help            - Show this help message"
"""
Layout Visualizer & Analyzer
A simple tool to analyze and visualize 2D grid-based layouts.
"""

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class LayoutAnalyzer:
    """Analyzes and visualizes 2D grid layouts."""
    
    def __init__(self, grid):
        """
        Initialize with a 2D grid layout.
        
        Args:
            grid: 2D list where 0 = empty, positive integers = objects
        """
        self.grid = np.array(grid)
        self.height, self.width = self.grid.shape
    
    def visualize(self, show_grid=True):
        """Display the layout using matplotlib."""
        plt.figure(figsize=(8, 6))
        plt.imshow(self.grid, cmap='tab20', interpolation='nearest')
        plt.colorbar(label='Object ID (0 = empty)')
        plt.title('Layout Visualization')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        
        if show_grid:
            # Add grid lines
            plt.grid(True, which='both', color='gray', linewidth=0.5, alpha=0.3)
            plt.xticks(range(self.width))
            plt.yticks(range(self.height))
        
        plt.tight_layout()
        plt.show()
    
    def print_ascii(self):
        """Print ASCII representation to console."""
        print("\nLayout (ASCII):")
        print("-" * (self.width * 3 + 1))
        for row in self.grid:
            print("|" + "|".join(f"{cell:2d}" for cell in row) + "|")
        print("-" * (self.width * 3 + 1))
    
    def calculate_utilization(self):
        """Calculate space utilization percentage."""
        total_cells = self.grid.size
        occupied_cells = np.count_nonzero(self.grid)
        utilization = (occupied_cells / total_cells) * 100
        return utilization
    
    def detect_issues(self):
        """Detect overlapping or invalid placements."""
        issues = []
        
        # Check for negative values (invalid)
        if np.any(self.grid < 0):
            issues.append("Invalid: Negative values detected")
        
        # Note: In this simple grid model, each cell can only hold one value,
        # so overlapping is prevented by design. We check for clustering instead.
        
        return issues if issues else ["No issues detected"]
    
    def analyze_clustering(self):
        """Analyze object clustering and suggest improvements."""
        if np.all(self.grid == 0):
            return "Grid is empty"
        
        # Count objects
        object_counts = Counter(self.grid.flatten())
        object_counts.pop(0, None)  # Remove empty cells
        
        if not object_counts:
            return "No objects to analyze"
        
        # Calculate density in quadrants
        mid_h, mid_w = self.height // 2, self.width // 2
        quadrants = [
            self.grid[:mid_h, :mid_w],      # Top-left
            self.grid[:mid_h, mid_w:],      # Top-right
            self.grid[mid_h:, :mid_w],      # Bottom-left
            self.grid[mid_h:, mid_w:]       # Bottom-right
        ]
        
        densities = [np.count_nonzero(q) / q.size for q in quadrants]
        max_density = max(densities)
        min_density = min(densities)
        
        # Suggest optimization
        if max_density - min_density > 0.3:
            return f"High clustering detected (density variance: {max_density - min_density:.2f}). Consider redistributing objects."
        else:
            return "Objects are reasonably distributed"
    
    def generate_report(self):
        """Generate a complete analysis report."""
        print("\n" + "=" * 50)
        print("LAYOUT ANALYSIS REPORT")
        print("=" * 50)
        
        print(f"\nDimensions: {self.height} × {self.width}")
        print(f"Total cells: {self.grid.size}")
        
        utilization = self.calculate_utilization()
        print(f"\nSpace Utilization: {utilization:.1f}%")
        print(f"Occupied cells: {np.count_nonzero(self.grid)}")
        print(f"Empty cells: {self.grid.size - np.count_nonzero(self.grid)}")
        
        print("\nIssue Detection:")
        for issue in self.detect_issues():
            print(f"  • {issue}")
        
        print("\nClustering Analysis:")
        print(f"  • {self.analyze_clustering()}")
        
        # Object distribution
        object_counts = Counter(self.grid.flatten())
        object_counts.pop(0, None)
        if object_counts:
            print("\nObject Distribution:")
            for obj_id, count in sorted(object_counts.items()):
                print(f"  • Object {obj_id}: {count} cells")
        
        print("\n" + "=" * 50)

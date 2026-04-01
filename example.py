"""
Example usage of the Layout Analyzer.
"""

from layout_analyzer import LayoutAnalyzer


# Example 1: Well-distributed layout
print("Example 1: Well-distributed layout")
layout1 = [
    [1, 0, 2, 0],
    [0, 3, 0, 4],
    [5, 0, 6, 0],
    [0, 7, 0, 8]
]

analyzer1 = LayoutAnalyzer(layout1)
analyzer1.print_ascii()
analyzer1.generate_report()
analyzer1.visualize()


# Example 2: Clustered layout
print("\n\nExample 2: Clustered layout (poor distribution)")
layout2 = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 2, 2]
]

analyzer2 = LayoutAnalyzer(layout2)
analyzer2.print_ascii()
analyzer2.generate_report()
analyzer2.visualize()


# Example 3: Low utilization
print("\n\nExample 3: Low utilization")
layout3 = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

analyzer3 = LayoutAnalyzer(layout3)
analyzer3.print_ascii()
analyzer3.generate_report()
analyzer3.visualize()

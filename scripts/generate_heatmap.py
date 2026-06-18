import os
from query_github import days

OUTPUT_FILE = "assets/heatmap.svg"

def color(n):
    if n == 0:
        return "#ebedf0"
    elif n <= 2:
        return "#9be9a8"
    elif n <= 5:
        return "#40c463"
    elif n <= 8:
        return "#30a14e"
    else:
        return "#216e39"

cell_size = 15
gap = 4

width = 7 * (cell_size + gap)
height = cell_size + 20

svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="white"/>
<text x="0" y="12" font-size="12" fill="#333">Last 7 Days</text>
'''

x = 0
y = 20

for i, d in enumerate(days):
    svg += f'''
    <rect x="{x}" y="{y}"
          width="{cell_size}" height="{cell_size}"
          fill="{color(d['count'])}"
          rx="3"/>
    <text x="{x}" y="{y + 12}" font-size="8" fill="#111">{d['count']}</text>
    '''
    x += cell_size + gap

svg += "</svg>"

os.makedirs("assets", exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    f.write(svg)

print("SVG generated:", OUTPUT_FILE)

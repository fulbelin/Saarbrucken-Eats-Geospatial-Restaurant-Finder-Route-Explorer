from flask import Flask, render_template, send_from_directory
import os
import markdown

app = Flask(__name__)

def get_readme_content():
    """Reads and converts README.md from Markdown to HTML, with error handling."""
    readme_path = os.path.join(os.getcwd(), 'README.md')
    if not os.path.exists(readme_path):  # Handle missing file
        return "<p>README.md not found.</p>"

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_text = f.read()
    return markdown.markdown(readme_text, extensions=['fenced_code'])  # Convert Markdown to HTML

@app.route('/')
def index():
    readme_content = get_readme_content()
    return render_template('index.html', readme_content=readme_content)

# Serve static HTML files from the 'static/maps' directory
@app.route('/maps/<map_name>')
def serve_map(map_name):
    """Serves HTML map files dynamically from the 'static/maps' directory."""
    valid_maps = {
        "cluster_map": "cluster_map.html",
        "distance_clusters": "distance_clusters_map.html",
        "heatmap": "heatmap.html",
        "restaurants": "restaurants_distances_map.html",
        "routes": "routes_map.html"
    }
    
    if map_name in valid_maps:
        return send_from_directory('static/maps', valid_maps[map_name])
    return "<h3>Map Not Found</h3>", 404

if __name__ == "__main__":
    app.run(debug=True)

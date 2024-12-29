from .flask_app import HarmonixPy as _HarmonixPy

# Default class instance for easy access to HarmonixPy functions
_app = _HarmonixPy()

# User-facing functions
def html(file_path):
    """Set the HTML file path."""
    _app.html(file_path)

def css(file_path):
    """Set the CSS file path."""
    _app.css(file_path)

def js(file_path):
    """Set the JavaScript file path."""
    _app.js(file_path)

def dependency(file_path):
    """Set the requirements.txt file path for dependencies."""
    _app.requirements_file_path = file_path

def create_default_files():
    """Create default HTML, CSS, and JS files in the specified directories."""
    _app.create_default_files()

def install_dependencies():
    """Install dependencies from requirements.txt."""
    _app.install_dependencies()

def load_html_content():
    """Load the content of the main HTML file as a string."""
    return _app.load_html_content()

def run(host="127.0.0.1", port=5000):
    """Run the Flask application."""
    _app.app.run(debug=True, host=host, port=port)

# Allow a single function to initialize and run the app
def HarmonixPy(html_file="index.html", css_file="static/styles.css", js_file="static/scripts.js", requirements_file="requirements.txt", static_folder="static"):
    """
    Initialize the app with specified files and folders and run it.

    Args:
        html_file (str): Path to the HTML file.
        css_file (str): Path to the CSS file.
        js_file (str): Path to the JavaScript file.
        requirements_file (str): Path to the requirements.txt file.
        static_folder (str): Path to the static folder.
    """
    if html_file:
        html(html_file)
    if css_file:
        css(css_file)
    if js_file:
        js(js_file)
    if requirements_file:
        dependency(requirements_file)
    
    _app.static_folder = static_folder
    create_default_files()
    run()

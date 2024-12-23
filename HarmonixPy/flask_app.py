'''HMNX'''
import os
import subprocess
from flask import Flask, render_template_string

class HarmonixPy:
    '''initial setup'''
    def __init__(self, project_dir="my_project"):
        self.project_dir = project_dir
        self.static_folder = os.path.join(self.project_dir, "static")  # Define static folder
        self.templates_folder = os.path.join(self.project_dir, "templates")  # Define templates folder
        self.html_files = [os.path.join(self.templates_folder, "index.html")]  # List of HTML files
        self.css_files = [os.path.join(self.static_folder, "styles.css")]  # List of CSS files
        self.js_files = [os.path.join(self.static_folder, "script.js")]  # List of JS files
        self.requirements_file_path = os.path.join(self.project_dir, "requirements.txt")  # Default dependencies file
        self.app = Flask(__name__, static_folder=self.static_folder, template_folder=self.templates_folder)

        # Define the home route
        @self.app.route("/")
        def home():
            html_content = self.load_html_content()
            return render_template_string(html_content)

    def html(self, path):
        """Add a custom path for the HTML file."""
        self.html_files.append(path)
        return self.html_files

    def css(self, path):
        """Add a custom path for the CSS file."""
        self.css_files.append(path)
        return self.css_files

    def js(self, path):
        """Add a custom path for the JavaScript file."""
        self.js_files.append(path)
        return self.js_files

    def load_html_content(self):
        """Load content from the first HTML file in the list."""
        try:
            with open(self.html_files[0], "r", encoding="utf-8") as html_file:
                html_content = html_file.read()
            # Add dynamic links for multiple CSS and JS files
            html_content = self.add_static_links(html_content)
            return html_content
        except FileNotFoundError:
            return "<h1>Error: HTML file not found.</h1>"

    def add_static_links(self, html_content):
        """Dynamically link external JS and CSS files using Flask's url_for."""
        # Add all CSS links
        css_links = "\n".join([f'<link rel="stylesheet" href="{{{{ url_for(\'static\', filename=\'{os.path.basename(css_file)}\') }}}}">' for css_file in self.css_files])

        # Add all JS links
        js_links = "\n".join([f'<script src="{{{{ url_for(\'static\', filename=\'{os.path.basename(js_file)}\') }}}}"></script>' for js_file in self.js_files])

        if "</head>" in html_content:
            html_content = html_content.replace("</head>", f"{css_links}\n{js_links}\n</head>")
        else:
            raise ValueError("No closing </head> tag found in the HTML file.")

        return html_content

    def install_dependencies(self):
        """Install dependencies listed in the specified requirements file."""
        try:
            if os.path.exists(self.requirements_file_path):
                with open(self.requirements_file_path, "r", encoding="utf-8") as file:
                    dependencies = file.read().splitlines()

                for dependency in dependencies:
                    subprocess.check_call(["pip", "install", dependency])
                print("All dependencies installed successfully!")
            else:
                print(f"Error: {self.requirements_file_path} not found.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing a package: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run(self):
        """Install dependencies and start the Flask app."""
        self.install_dependencies()
        self.app.run(debug=True, host="0.0.0.0", port=5000)

    def create_default_files(self):
        """Create default static and template files if not exist."""
        # Create directories if not exist
        os.makedirs(self.static_folder, exist_ok=True)
        os.makedirs(self.templates_folder, exist_ok=True)

        # Default HTML content
        if not os.path.exists(self.html_files[0]):
            with open(self.html_files[0], 'w', encoding='utf-8') as html_file:
                html_file.write("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Dynamic Test Page</title>
                </head>
                <body>
                    <h1>Welcome to HarmonixPy</h1>
                    <p>This is a test page with dynamic linking of CSS and JavaScript files.</p>
                </body>
                </html>
                """)

        # Default CSS content
        if not os.path.exists(self.css_files[0]):
            with open(self.css_files[0], 'w', encoding='utf-8') as css_file:
                css_file.write("""
                body {
                    background-color: #f0f0f0;
                    color: #333;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #007bff;
                }
                """)

        # Default JS content
        if not os.path.exists(self.js_files[0]):
            with open(self.js_files[0], 'w', encoding='utf-8') as js_file:
                js_file.write("""
                console.log('Hello, world!');
                document.addEventListener('DOMContentLoaded', () => {
                    console.log('DOM fully loaded and parsed.');
                });
                """)

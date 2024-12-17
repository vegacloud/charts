import os

# Path to your chart directory
chart_dir = './'

# Path to the index.html file
html_file = 'index.html'

# Open the HTML file for writing
with open(html_file, 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vega Cloud Kubernetes Metrics Agent Helm Chart Repository</title>
    <!-- Bootstrap CSS for modern styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEJf6IQfYAOoZ2NuQz5/p9v0ImtFhgzqF3nDLhM9zwzbsAljLQlmTX8vJ2aA6" crossorigin="anonymous">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
        }
        .container {
            max-width: 900px;
            margin-top: 30px;
        }
        .header {
            background-color: #007bff;
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .logo {
            max-width: 120px;  /* Set max width of logo */
            margin-bottom: 20px;
        }
        .list-group-item {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            font-size: 1.1rem;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .list-group-item a {
            color: #007bff;
            text-decoration: none;
        }
        .list-group-item a:hover {
            text-decoration: underline;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9rem;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Logo at the top -->
        <div class="text-center">
            <img src="https://vegacloud.github.io/assets/logo.png" alt="Vega Cloud Logo" class="logo">
        </div>

        <div class="header">
            <h1>Vega Cloud Kubernetes Metrics Agent Helm Chart Repository</h1>
            <p class="lead">A collection of Helm charts for deploying the Vega Cloud Kubernetes Metrics Agent.</p>
        </div>
        <div class="mt-4">
            <h3>Available Helm Charts</h3>
            <ul class="list-group">
""")

    # List the files in the chart directory and sort them in descending order
    chart_files = [file_name for file_name in os.listdir(chart_dir) if file_name.endswith(".tgz")]
    chart_files.sort(reverse=True)  # Sort files in descending order

    # Create list items for each chart file in the sorted list
    for file_name in chart_files:
        chart_url = f"https://vegacloud.github.io/charts/{file_name}"
        f.write(f"""<li class="list-group-item">
                        <a href="{chart_url}">{file_name}</a>
                    </li>
""")

    f.write("""        </ul>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 Vega Cloud. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS for interactivity (if needed) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-wvA4WQft88R6P88aYgJ4bfz6pyZfi7n/KxOyzQ6eZOaJNEpB6T5oVx8cC5FuW8Vg" crossorigin="anonymous"></script>
</body>
</html>""")

print("index.html has been generated.")

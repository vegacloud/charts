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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-R6M0xDQrYqD8En5p+prGBpENbBU5Fw9c86wlORjaAs4pVSS0fuBSdWi0O9V9LS1y" crossorigin="anonymous">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
        }
        .navbar-brand img {
            height: 30px;
            margin-right: 10px;
        }
        .hero {
            padding: 60px 0;
            background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
            color: #fff;
        }
        .hero h1 {
            font-weight: 700;
            margin-bottom: 20px;
        }
        .hero p.lead {
            font-size: 1.25rem;
            font-weight: 300;
        }
        .card {
            border: none;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
        }
        .card-body a {
            text-decoration: none;
            color: #007bff;
        }
        .card-body a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 40px;
            padding: 20px 0;
            border-top: 1px solid #e9ecef;
            text-align: center;
            font-size: 0.9rem;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="#">
                <img src="https://vegacloud.github.io/charts/assets/logo.png" alt="Vega Cloud Logo">
                Vega Cloud Metrics Agent Charts
            </a>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <section class="hero text-center">
        <div class="container">
            <h1>Vega Cloud Kubernetes Metrics Agent Helm Chart Repository</h1>
            <p class="lead">A collection of Helm charts for deploying the Vega Cloud Kubernetes Metrics Agent.</p>
        </div>
    </section>

    <!-- Chart List Section -->
    <div class="container my-5">
        <h3 class="mb-4">Available Helm Charts</h3>
        <div class="row g-4">
""")

    # List the files in the chart directory and sort them in descending order
    chart_files = [file_name for file_name in os.listdir(chart_dir) if file_name.endswith(".tgz")]
    chart_files.sort(reverse=True)  # Sort files in descending order

    # Create card for each chart file
    for file_name in chart_files:
        chart_url = f"https://vegacloud.github.io/charts/{file_name}"
        f.write(f"""
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <div class="card h-100">
                    <div class="card-body d-flex flex-column justify-content-between">
                        <h5 class="card-title">{file_name}</h5>
                        <a href="{chart_url}" class="mt-auto">Download Chart</a>
                    </div>
                </div>
            </div>
        """)

    f.write("""    </div>
    </div>

    <footer>
        <p>&copy; 2024-2025 Vega Cloud. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS for interactivity -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-qRpHygAuK4xeNH4wyEY8+dOn8dn5rSd9iXS/lD4t/q+JYBGeSBbu7P5Fr3fZ6/uY" crossorigin="anonymous"></script>
</body>
</html>""")

print("index.html has been generated with a modern, professional design.")

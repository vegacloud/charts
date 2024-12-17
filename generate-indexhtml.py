import os

# Path to your chart directory
chart_dir = './'

# Path to the index.html file
html_file = 'index.html'

with open(html_file, 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vega Cloud Kubernetes Metrics Agent Helm Chart Repository</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-R6M0xDQrYqD8En5p+prGBpENbBU5Fw9c86wlORjaAs4pVSS0fuBSdWi0O9V9LS1y" crossorigin="anonymous">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f9fa;
        }

        /* Navbar */
        .navbar {
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .navbar-brand img {
            height: 30px;
            margin-right: 10px;
        }

        /* Hero Section */
        .hero {
            padding: 80px 0;
            background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
            color: #fff;
            text-align: center;
        }
        .hero h1 {
            font-weight: 700;
            margin-bottom: 20px;
        }
        .hero p.lead {
            font-size: 1.25rem;
            font-weight: 300;
            margin-bottom: 30px;
        }

        /* Chart Cards */
        .card {
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
        }
        .card-title {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .card a {
            color: #007bff;
            text-decoration: none;
            font-weight: 500;
        }
        .card a:hover {
            text-decoration: underline;
        }

        /* Footer */
        footer {
            margin-top: 60px;
            padding: 20px 0;
            color: #6c757d;
            text-align: center;
            font-size: 0.9rem;
            border-top: 1px solid #e9ecef;
        }

        /* Spacing Tweaks */
        .charts-section {
            padding-bottom: 60px;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-white bg-white sticky-top">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="#">
                <img src="https://vegacloud.github.io/charts/assets/logo.png" alt="Vega Cloud Logo">
                <span class="fw-bold">Vega Cloud Metrics Agent Charts</span>
            </a>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Vega Cloud Kubernetes Metrics Agent Helm Chart Repository</h1>
            <p class="lead">A collection of Helm charts for deploying the Vega Cloud Kubernetes Metrics Agent.</p>
            <a href="https://docs.vegacloud.io/docs/providers/kubernetes" target="_blank" class="btn btn-light btn-lg fw-semibold">View Documentation</a>
        </div>
    </section>

    <!-- Chart List Section -->
    <div class="container charts-section mt-5">
        <h3 class="mb-4 fw-semibold">Available Helm Charts</h3>
        <div class="row g-4">
""")

    # List the files in the chart directory and sort them in descending order
    chart_files = [file_name for file_name in os.listdir(chart_dir) if file_name.endswith(".tgz")]
    chart_files.sort(reverse=True)  # Sort files in descending order

    # Create cards for each chart file
    for file_name in chart_files:
        chart_url = f"https://vegacloud.github.io/charts/{file_name}"
        f.write(f"""
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <div class="card h-100 p-3 d-flex flex-column">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{file_name}</h5>
                        <div class="mt-auto">
                            <a href="{chart_url}" class="stretched-link">Download Chart</a>
                        </div>
                    </div>
                </div>
            </div>
        """)

    f.write("""    </div>
    </div>

    <footer>
        <p>&copy; 2024-2025 Vega Cloud. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-qRpHygAuK4xeNH4wyEY8+dOn8dn5rSd9iXS/lD4t/q+JYBGeSBbu7P5Fr3fZ6/uY" crossorigin="anonymous"></script>
</body>
</html>""")

print("index.html has been generated with an improved design.")

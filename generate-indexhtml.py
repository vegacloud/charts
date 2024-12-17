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

        /* Enhanced card styles */
        .card {
            border: 1px solid rgba(0,0,0,0.08);
            background-color: #ffffff;
        }
        .chart-meta {
            font-size: 0.85rem;
            color: #6c757d;
            margin-bottom: 0.5rem;
        }
        .installation-section {
            background-color: #f8f9fa;
            padding: 60px 0;
            margin-top: -30px;
        }
        .installation-section pre {
            background-color: #2d2d2d;
            color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }
        .footer-links a {
            color: #6c757d;
            margin: 0 10px;
            text-decoration: none;
        }
        .footer-links a:hover {
            color: #007bff;
        }

        .hero a.btn-light:visited {
            color: #212529;  /* Default dark color for light buttons */
        }
        .hero a:visited {
            color: #ffffff;
        }
    </style>
</head>
<body>   
    
    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Vega Cloud Kubernetes Metrics Agent</h1>
            <p class="lead">Official Helm repository for deploying and managing the Vega Cloud Kubernetes Metrics Agent</p>
            <div class="d-flex justify-content-center gap-3">
                <a href="https://docs.vegacloud.io/docs/providers/kubernetes" target="_blank" class="btn btn-light btn-lg fw-semibold">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-book me-2" viewBox="0 0 16 16">
                        <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/>
                    </svg>
                    Documentation
                </a>
                <a href="https://github.com/vegacloud/vega-metrics-agent" target="_blank" class="btn btn-light btn-lg fw-semibold">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github me-2" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                    GitHub Repository
                </a>
            </div>
        </div>
    </section>

    <!-- Installation Section -->
    <section class="installation-section">
        <div class="container">
            <h3 class="mb-4 fw-semibold">Quick Installation</h3>
            <pre><code># Add the Vega Cloud Helm repository
helm repo add vegacloud https://vegacloud.github.io/charts
helm repo update

# Install the metrics agent
helm install vega-metrics vegacloud/vega-metrics-agent \
  --set vega.clientId="your-client-id" \
  --set vega.clientSecret="your-client-secret" \
  --set vega.orgSlug="your-org-slug" \
  --set vega.clusterName="your-cluster-name"</code></pre>
        </div>
    </section>

    <!-- Chart List Section -->
    <div class="container charts-section mt-5">
        <h3 class="mb-4 fw-semibold">Available Versions</h3>
        <div class="row g-4">
""")

    # List the files in the chart directory and sort them in descending order
    chart_files = [file_name for file_name in os.listdir(chart_dir) if file_name.endswith(".tgz")]
    chart_files.sort(reverse=True)  # Sort files in descending order

    # Enhanced card template
    for file_name in chart_files:
        # Extract version from vega-metrics-agent-1.0.0.tgz or vega-metrics-agent-1.0.0-<tag>.tgz
        version = '-'.join(file_name.split('-')[3:]).replace('.tgz', '')
        chart_url = f"https://vegacloud.github.io/charts/{file_name}"
        f.write(f"""
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <div class="card h-100 p-3">
                    <div class="card-body">
                        <h5 class="card-title">Version {version}</h5>
                        <div class="chart-meta">
                            <div>Chart: {file_name}</div>
                        </div>
                        <div class="mt-3">
                            <a href="{chart_url}" class="btn btn-outline-primary btn-sm">Download Chart</a>
                        </div>
                    </div>
                </div>
            </div>
        """)

    f.write("""
        </div>
    </div>

    <footer class="bg-light">
        <div class="container py-4">
            <div class="footer-links mb-3">
                <a href="https://vegacloud.io">Website</a>
                <a href="https://docs.vegacloud.io/docs/providers/kubernetes">Documentation</a>
                <a href="https://github.com/vegacloud/vega-metrics-agent">GitHub</a>
                <a href="https://vegacloud.io/contact">Contact</a>
            </div>
            <p>&copy; 2024-2025 Vega Cloud. All rights reserved.</p>
        </div>
    </footer>
    """)

    # Bootstrap JS -->
    f.write("""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-qRpHygAuK4xeNH4wyEY8+dOn8dn5rSd9iXS/lD4t/q+JYBGeSBu7P5Fr3fZ6/uY" crossorigin="anonymous"></script>
</body>
</html>""")

print("index.html has been generated with an improved design.")

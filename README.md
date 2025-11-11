# GitHub Data Pipeline with dlt and BigQuery

This repository demonstrates how to extract data from the GitHub REST API using [dlt](https://github.com/dlt-hub/dlt), and load it into Google BigQuery for analysis.

## Features
- **dlt REST API Source**: Connects to the GitHub API and extracts repository metadata for a specified user.
- **BigQuery Integration**: Stores all extracted data in a BigQuery dataset for fast analytics.
- **Secrets Management**: Uses `.dlt/secrets.toml` to securely store your GitHub access token, owner name, and Google Cloud service account credentials.
- **Automated Extraction**: Can be scheduled to run periodically (e.g., via GitHub Actions or cron).

## How It Works
1. **Configure Secrets**: Add your GitHub personal access token, the target owner, and your Google Cloud service account credentials to `.dlt/secrets.toml`.
2. **Run the Pipeline**: Execute `python github_pipeline.py` to extract all repository data for the owner and load it into BigQuery.
3. **Analyze Data**: Query the `github_data.repositories` table in BigQuery to explore repository metadata.

## Setup
1. Install dependencies:
   ```bash
   pip install 'dlt[bigquery]'
   ```
2. Fill in `.dlt/secrets.toml`:
   ```toml
   access_token = "<your_github_pat>"
   owner = "<github_username>"

   [credentials]
   project_id = "<your_gcp_project_id>"
   private_key = """
   -----BEGIN PRIVATE KEY-----
   ...your private key...
   -----END PRIVATE KEY-----
   """
   client_email = "<your_service_account_email>"
   ```
3. Run the pipeline:
   ```bash
   python github_pipeline.py
   ```

## Output
- Data is loaded into your BigQuery project under the dataset `github_data`, table `repositories`.
- All available fields from the GitHub API response are included.

## Security
- Keep your personal access token and GCP credentials secret. Do not commit `.dlt/secrets.toml` with real credentials to public repositories.

## License
MIT

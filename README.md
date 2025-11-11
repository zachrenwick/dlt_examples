# GitHub Data Pipeline with dlt and DuckDB

This repository demonstrates how to extract data from the GitHub REST API using [dlt](https://github.com/dlt-hub/dlt), and load it into a local DuckDB database for analysis.

## Features
- **dlt REST API Source**: Connects to the GitHub API and extracts repository metadata for a specified user.
- **DuckDB Integration**: Stores all extracted data in a local DuckDB file for fast analytics.
- **Secrets Management**: Uses `.dlt/secrets.toml` to securely store your GitHub access token and owner name.
- **Automated Extraction**: Can be scheduled to run periodically (e.g., via GitHub Actions or cron).

## How It Works
1. **Configure Secrets**: Add your GitHub personal access token and the target owner to `.dlt/secrets.toml`.
2. **Run the Pipeline**: Execute `python github_pipeline.py` to extract all repository data for the owner and load it into DuckDB.
3. **Analyze Data**: Query the `github_data.repositories` table in `github_pipeline.duckdb` to explore repository metadata.

## Setup
1. Install dependencies:
   ```bash
   pip install 'dlt[workspace]' duckdb
   ```
2. Fill in `.dlt/secrets.toml`:
   ```toml
   access_token = "<your_github_pat>"
   owner = "<github_username>"
   ```
3. Run the pipeline:
   ```bash
   python github_pipeline.py
   ```

## Output
- Data is loaded into `github_pipeline.duckdb` under the schema `github_data`, table `repositories`.
- All available fields from the GitHub API response are included.

## Security
- Keep your personal access token secret. Do not commit `.dlt/secrets.toml` with real credentials to public repositories.

## License
MIT

## Machine Learning Engineering & MLOps

**Project: INNUTRIRE — AI-Powered Resting Energy Expenditure Prediction System**

- **MLOps Pipeline Development:** Implemented an automated machine-learning training pipeline integrating GitHub Actions, Data Version Control (DVC), MLflow, and Python-based model training.

- **Self-Hosted CI/CD Infrastructure:** Configured a Windows self-hosted GitHub Actions runner to execute machine-learning workloads locally, enabling remote training execution through GitHub.

- **Data Versioning and Reproducibility:** Integrated DVC to manage versioned clinical research datasets, configure private local data storage, and automatically retrieve training data during CI/CD execution.

- **Python Environment and Dependency Management:** Migrated the machine-learning project to `pyproject.toml` and `uv.lock`, enabling reproducible dependency installation using uv and Python 3.12.

- **Automated Software Testing:** Integrated pytest into GitHub Actions, successfully executing 33 automated tests covering machine-learning functionality, data processing, MLflow integration, and repository integrity.

- **Repository Integrity and Data Protection:** Developed pytest-based repository validation checks to verify essential DVC and uv configuration files and detect potentially sensitive or generated files staged for Git commits.

- **Automated Model Training:** Successfully executed a training pipeline covering seven regression algorithms: Linear Regression, Ridge Regression, Random Forest, Gradient Boosting, XGBoost, LightGBM, and Support Vector Regression.

- **Machine Learning Model Evaluation:** Evaluated regression models using RMSE, MAE, and R², comparing retrained models against the deployed SVR model and conventional predictive equations on a common evaluation cohort.

- **Experiment Tracking and Management:** Integrated MLflow with a persistent SQLite tracking database to record machine-learning experiments, training parameters, and evaluation metrics.

- **CI/CD Workflow Troubleshooting:** Diagnosed and resolved GitHub Actions workflow registration, branch-specific execution, Python dependency, DVC repository detection, and MLflow tracking backend issues.

- **Research and Production Isolation:** Established branch-isolated training workflows and manually triggered experimentation to prevent unvalidated machine-learning models from being automatically deployed to clinical environments.

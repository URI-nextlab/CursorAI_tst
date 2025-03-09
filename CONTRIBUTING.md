# Contributing to DeepSeek R1 Streamlit Interface

Thank you for considering contributing to the DeepSeek R1 Streamlit Interface! This document outlines the process for contributing to the project.

## Code of Conduct

Please be respectful and considerate to all participants in our community. This project adheres to a code of conduct that outlines our expectations for all those who participate in our community, as well as the consequences for unacceptable behavior.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** if possible.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps** or point out the part of the project the suggestion applies to.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** to most users.
* **List some other applications where this enhancement exists.**

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible
* Follow the Python style guide
* Include unit tests when applicable
* End all files with a newline
* Avoid platform-dependent code

## Style Guides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Style Guide

All Python code must adhere to PEP 8 style guide:

* Use 4 spaces for indentation
* Maximum line length of 79 characters
* Use appropriate naming conventions
* Add docstrings to all functions
* Include type hints when appropriate

## Setting Up Development Environment

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/deepseek-streamlit.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   * Windows: `venv\Scripts\activate`
   * Unix/MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file with your API keys
7. Run the application: `streamlit run streamlit_app.py`

## Thank You!

Thank you for taking the time to contribute to the project! 
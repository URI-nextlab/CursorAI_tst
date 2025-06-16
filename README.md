# DeepSeek R1 Streamlit Chat Interface

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

</div>

<p align="center">
  A sleek, modern dark-themed GUI for interacting with the DeepSeek Reasoner model, featuring real-time equation rendering, code highlighting, and advanced reasoning visualization.
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#mathematical-expressions">Mathematical Expressions</a> •
  <a href="#examples">Examples</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## Key Features

- **Clean Dark Mode Interface**: Modern dark theme optimized for reduced eye strain during long usage
- **Real-time Reasoning Process**: Watch the model's step-by-step thinking process as it solves problems
- **LaTeX Equation Rendering**: Beautiful mathematical expressions with proper notation
- **Syntax Highlighting**: Clean, highlighted code snippets that are easy to read and understand
- **Conversation Export**: Download your conversation history as a text file for later reference
- **Responsive Design**: Works smoothly on both desktop and mobile devices
- **Enter Key Submission**: Fast, intuitive message submission with Enter key support

## Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/URI-nextlab/CursorAI_tst.git
   cd proj2
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**:
   Create a `.env` file in the project root with your DeepSeek API key:
   ```
   DEEPSEEK_API_KEY=your-api-key-here
   ```
   
   > **Note**: You can obtain a DeepSeek API key by registering at [DeepSeek Platform](https://platform.deepseek.com/).

## Usage

1. **Start the application**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the interface**:
   Open your browser at http://localhost:8501

3. **Using the application**:
   - Type your message in the text area and press Enter to send
   - Toggle the reasoning process display using the sidebar control
   - Download your conversation using the Export button
   - Clear history to start a fresh conversation

## Mathematical Expressions

The DeepSeek R1 model excels at handling mathematical problems with clear, step-by-step reasoning. Try questions like:

| Example Query | Description |
|---------------|-------------|
| `Solve x² + 6x + 9 = 0` | Quadratic equation solving |
| `Find the derivative of x³ + 2x² - 5x + 3` | Calculus problems |
| `If all A are B, and all B are C, then all A are C. Is this valid?` | Logical reasoning |
| `What is the probability of getting at least one 6 when rolling two dice?` | Probability problems |

## Examples

### Code Generation
Below is an example of how you can ask the model to generate a Python function (for example, a Fibonacci calculator) and then copy the highlighted (syntax‑highlighted) code snippet from the chat.

```python
# Example prompt: "Generate a Python function to compute Fibonacci numbers (iterative version)."
# The model's response (with syntax highlighting) might look like:
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
```

### Mathematical Reasoning
The DeepSeek R1 model excels at solving math problems (for example, quadratic equations, derivatives, or probability questions) and renders the reasoning (using LaTeX) in real‑time. For instance, if you ask "Solve x² + 6x + 9 = 0", the model's step‑by‑step reasoning (with rendered equations) will be displayed in the chat.

### Logical Analysis
You can also ask the model to analyze logical arguments (for example, "If all A are B, and all B are C, then all A are C. Is this valid?"). The model's detailed breakdown (with logical steps) is rendered (using markdown and LaTeX) in the chat.

## Troubleshooting & FAQ

- **Q: My API key isn't recognized.**  
  A: Ensure that your `.env` file (in the project root) contains a valid `DEEPSEEK_API_KEY` (and that you've activated your virtual environment).  
- **Q: The reasoning process (or LaTeX equations) isn't rendering.**  
  A: Check that your browser supports MathJax (or that you're using a modern browser) and that your prompt (or model's output) is formatted correctly (using LaTeX delimiters).  
- **Q: How do I export my conversation?**  
  A: Use the "Export" button (or a similar UI control) provided in the interface to download your chat history as a text file.

## Acknowledgments & Credits

- This project was built by URI NextLab (see the [LICENSE](LICENSE) file for copyright details).
- We thank the DeepSeek team (and the [DeepSeek Platform](https://platform.deepseek.com/)) for providing the reasoning model.
- Thanks also to the Streamlit, Pygments, and MathJax communities for their excellent tools.

---

<div align="center">
  <sub>Built with ❤️ by URI NextLab</sub>
</div> 
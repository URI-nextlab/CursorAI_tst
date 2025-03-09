# DeepSeek R1 Streamlit Chat Interface

<div align="center">

![DeepSeek R1](https://img.shields.io/badge/DeepSeek-R1_Reasoner-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTggNmEyIDIgMCAwIDAtMi0ybC0xMiAuMDFhMiAyIDAgMCAwLTEuOTUgMS44NWwtLjAxIDEyYTIgMiAwIDAgMCAyIDJoMTJhMiAyIDAgMCAwIDItMiIvPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjQiLz48L3N2Zz4=)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

</div>

<div align="center">
  <img src="https://placehold.co/800x400?text=DeepSeek+R1+Streamlit+Interface&font=playfair" alt="DeepSeek R1 Interface Demo" width="800px">
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
   git clone https://github.com/URI-nextlab/proj2.git
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

<div align="center">
  <img src="https://placehold.co/600x400?text=Usage+Demo+GIF&font=playfair" alt="Usage Demo" width="600px">
</div>

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
```python
# Example: Ask the model to generate a Python function to calculate Fibonacci numbers
```

### Mathematical Reasoning
```
# Example: The model's step-by-step approach to solving complex math problems
```

### Logical Analysis
```
# Example: How the model breaks down and analyzes logical arguments
```

## Technical Details

- **Frontend**: Streamlit web application framework
- **Backend**: DeepSeek API (OpenAI-compatible client)
- **Model**: DeepSeek Reasoner with chain-of-thought capabilities
- **Equation Rendering**: LaTeX via Streamlit's native MathJax support
- **Code Highlighting**: Pygments syntax highlighter
- **Conversation Management**: Session-based state management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ by URI NextLab</sub>
</div> 
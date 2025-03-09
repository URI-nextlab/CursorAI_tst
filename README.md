# DeepSeek R1 Streamlit Chat Interface

A streamlined dark-themed GUI for interacting with the DeepSeek Reasoner model.

## Features

- **Clean Dark Mode Interface**: Modern dark theme for reduced eye strain
- **Reasoning Process Display**: View the model's step-by-step thinking process
- **Mathematical Expression Rendering**: Properly formatted equations using LaTeX notation
- **Code Syntax Highlighting**: Beautiful syntax highlighting for code snippets
- **Text Export**: Download your conversation history as a text file
- **Enter Key Submission**: Easily submit messages using Enter key

## Screenshot

![DeepSeek R1 Streamlit Interface](https://placehold.co/600x400?text=DeepSeek+R1+Streamlit+Interface&font=playfair)

## Setup

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up your API key**:
   - Ensure your DeepSeek API key is set in the `.env` file:
   ```
   DEEPSEEK_API_KEY=your-api-key-here
   ```

## Running the Application

1. Start the Streamlit server:
   ```
   streamlit run streamlit_app.py
   ```

2. Open your browser at http://localhost:8501

## Usage

- **Chat Interface**: Type your message in the text area and press Enter to send
- **Reasoning Toggle**: Use the toggle in the sidebar to show/hide the model's reasoning process
- **Export Conversation**: Click the "Export as Text" button to download your conversation
- **Clear History**: Use the "Clear chat history" button to start fresh

## Working with Mathematical Expressions

The DeepSeek R1 model excels at handling mathematical problems. Try asking questions like:

- "Solve the quadratic equation x² + 6x + 9 = 0"
- "What is the derivative of x³ + 2x² - 5x + 3?"
- "Is the statement 'If all A are B, and all B are C, then all A are C' valid?"

## Example Prompt Types

- **Mathematical Problems**: Algebra, calculus, probability, etc.
- **Code Generation**: Ask for code samples or explanations
- **Logical Reasoning**: Syllogisms, paradoxes, or logical puzzles
- **Step-by-step Explanations**: Ask for detailed explanations of complex topics

## Technical Details

- Built with Streamlit, a Python framework for data apps
- Connected to DeepSeek API using the OpenAI-compatible client
- DeepSeek Reasoner model provides both reasoning steps and final answers
- Math rendering uses LaTeX notation supported by Streamlit
- Code highlighting powered by Pygments

## License

[MIT License](LICENSE) 
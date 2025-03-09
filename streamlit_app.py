#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DeepSeek R1 Streamlit GUI - Simplified Version

A streamlined dark-themed GUI for the DeepSeek Reasoner model focusing on:
- Clean dark mode interface
- Code syntax highlighting
- Mathematical expression rendering
- Enter key submission
"""

import os
import re
import io
import base64
import tempfile
import streamlit as st
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv
from openai import OpenAI
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from gtts import gTTS

# Set page configuration
st.set_page_config(
    page_title="DeepSeek R1 Chat",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark mode
custom_css = """
<style>
    /* Dark theme */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Improved spacing and visual elements */
    .main {
        max-width: 1000px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Message styling */
    .message {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 85%;
        word-wrap: break-word;
        position: relative;
    }
    
    .user-message {
        background-color: #1E293B;
        color: white;
        align-self: flex-end;
    }
    
    .bot-message {
        background-color: #3B4252;
        color: white;
        align-self: flex-start;
    }
    
    /* Sound button inside message */
    .sound-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: #4C566A;
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.2s ease;
        border: none;
        outline: none;
    }
    
    .sound-btn:hover {
        background-color: #5E81AC;
        transform: scale(1.1);
    }
    
    /* Reasoning box */
    .reasoning-box {
        background-color: #2E3440;
        border-left: 3px solid #88C0D0;
        color: #E5E9F0;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    
    /* Math styling */
    .katex {
        font-size: 1.1em !important;
    }
    
    .katex-display {
        margin: 1.2em 0 !important;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 8px;
    }
    
    /* Hide fullscreen button for cleaner UI */
    button[title="View fullscreen"] {
        display: none;
    }
    
    /* Code block styling */
    .code-block {
        background-color: #2E3440;
        border-radius: 5px;
        margin: 10px 0;
        overflow-x: auto;
    }
    
    .code-block pre {
        margin: 0;
        padding: 10px;
    }
    
    /* Export buttons */
    .export-btn {
        display: inline-block;
        padding: 5px 15px;
        margin: 5px;
        border-radius: 20px;
        text-decoration: none;
        text-align: center;
        transition: all 0.3s ease;
        background-color: #4C566A;
        color: white;
    }
    
    .export-btn:hover {
        background-color: #5E81AC;
    }
    
    /* Listen button styling */
    button[data-testid="baseButton-secondary"]:has(div:contains("🔊")) {
        background-color: #5E81AC;
        color: white;
        border: none;
        border-radius: 20px;
        transition: all 0.3s ease;
        margin: 0;
        padding: 0;
        min-width: 32px;
        width: 32px;
        height: 32px;
    }
    
    button[data-testid="baseButton-secondary"]:has(div:contains("🔊")):hover {
        background-color: #81A1C1;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    /* Audio player styling */
    audio {
        width: 100%;
        border-radius: 8px;
        margin-top: 10px;
        background-color: #3B4252;
    }
    
    /* Audio container */
    .audio-container {
        margin-top: 10px;
        background-color: #2E3440;
        border-radius: 8px;
        padding: 8px;
    }
    
    /* Input area styling */
    .stTextInput > div > div > input {
        background-color: #1E293B;
        color: white;
        border-color: #3B4252;
    }
    
    /* Placeholder style */
    .stTextInput > div > div > input::placeholder {
        color: #8899A6;
    }
</style>
"""

# Apply CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Code block detection and highlighting
def format_code_blocks(text: str) -> str:
    """
    Detect and format code blocks with syntax highlighting.
    
    Args:
        text: Text that may contain code blocks.
        
    Returns:
        Formatted text with highlighted code blocks.
    """
    # Pattern to match code blocks with language specification
    # Example: ```python\nprint("Hello")\n```
    pattern = r'```(\w+)?\n(.*?)\n```'
    
    def replace_code_block(match):
        lang = match.group(1) or 'text'
        code = match.group(2)
        
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter(style='monokai')
            highlighted_code = pygments.highlight(code, lexer, formatter)
            
            # Wrap the highlighted code in our custom div
            return f'<div class="code-block">{highlighted_code}</div>'
        except:
            # Fallback if language is not supported
            return f'<div class="code-block"><pre><code>{code}</code></pre></div>'
    
    # Use re.DOTALL to match across multiple lines
    return re.sub(pattern, replace_code_block, text, flags=re.DOTALL)

def format_equation(text: str) -> str:
    """
    Format equations for better display.
    
    Args:
        text: Text containing equations.
        
    Returns:
        Formatted text with properly displayed equations.
    """
    # Format standalone equations (equations on their own line)
    text = re.sub(r'(?<!\$)((?:^|\n)[\s]*[a-zA-Z0-9]+[^.\n]*?=.+?)(?:\n|$)', r'\n$$\1$$\n', text)
    
    # Format inline equations with variables (like x^2, sqrt(x))
    text = re.sub(r'(\b[a-zA-Z])\^(\d+)', r'$\1^{\2}$', text)
    text = re.sub(r'\bsqrt\(([^)]+)\)', r'$\\sqrt{\1}$', text)
    
    # Format fractions
    text = re.sub(r'(\d+)/(\d+)', r'$\\frac{\1}{\2}$', text)
    
    # Format common mathematical symbols
    text = re.sub(r'\bpi\b', r'$\\pi$', text)
    text = re.sub(r'\balpha\b', r'$\\alpha$', text)
    text = re.sub(r'\bbeta\b', r'$\\beta$', text)
    text = re.sub(r'\btheta\b', r'$\\theta$', text)
    
    # Format certain operations
    text = re.sub(r'(\d+)\s*\*\s*(\d+)', r'$\1 \\times \2$', text)
    
    return text

def preprocess_text(text: str) -> str:
    """
    Apply all text preprocessors in sequence.
    
    Args:
        text: Original text.
        
    Returns:
        Fully processed text with equations and code formatting.
    """
    text = format_equation(text)
    text = format_code_blocks(text)
    return text

def initialize_session():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'reasoning_contents' not in st.session_state:
        st.session_state.reasoning_contents = []
    if 'show_reasoning' not in st.session_state:
        st.session_state.show_reasoning = True
    if 'client' not in st.session_state:
        load_dotenv()
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            st.error("DeepSeek API key not found. Please set the DEEPSEEK_API_KEY environment variable.")
            st.stop()
        st.session_state.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

def get_response(prompt: str) -> Tuple[str, str]:
    """
    Get a response from the DeepSeek Reasoner model.
    
    Args:
        prompt: The user prompt.
        
    Returns:
        Tuple of (reasoning, answer).
    """
    # Create a fresh conversation with proper alternating user/assistant messages
    formatted_messages = []
    
    # First add any existing conversation history, ensuring alternating pattern
    if len(st.session_state.messages) > 0:
        for i in range(0, len(st.session_state.messages) - 1, 2):
            # Add user message
            if i < len(st.session_state.messages):
                formatted_messages.append(st.session_state.messages[i])
            
            # Add assistant message
            if i + 1 < len(st.session_state.messages):
                formatted_messages.append(st.session_state.messages[i + 1])
    
    # Add the current prompt as the last user message
    formatted_messages.append({"role": "user", "content": prompt})
    
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.client.chat.completions.create(
                model="deepseek-reasoner",
                messages=formatted_messages,
                stream=True
            )
            
            reasoning_content = ""
            content = ""
            
            # Create placeholder for streaming content
            if st.session_state.show_reasoning:
                reasoning_placeholder = st.empty()
            
            # Process stream chunks
            for chunk in response:
                if hasattr(chunk.choices[0].delta, 'reasoning_content') and chunk.choices[0].delta.reasoning_content:
                    chunk_text = chunk.choices[0].delta.reasoning_content
                    reasoning_content += chunk_text
                    
                    if st.session_state.show_reasoning:
                        # Format math in reasoning
                        formatted_reasoning = format_equation(reasoning_content)
                        reasoning_placeholder.markdown(
                            f'<div class="reasoning-box">{formatted_reasoning}</div>', 
                            unsafe_allow_html=True
                        )
                
                elif hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
                    content += chunk.choices[0].delta.content
            
            return reasoning_content, content
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "", f"Error: {str(e)}"

def create_text_file(messages: List[Dict[str, str]]) -> str:
    """
    Create a text file from the conversation.
    
    Args:
        messages: List of message dictionaries.
        
    Returns:
        Conversation as text.
    """
    text = "DeepSeek R1 Chat Conversation\n\n"
    
    for msg in messages:
        role = "You" if msg["role"] == "user" else "DeepSeek R1"
        content = msg["content"]
        
        text += f"{role}:\n{content}\n\n"
    
    return text

def get_download_link(file_content, file_name, link_text, mime_type):
    """
    Generate a download link for a file.
    
    Args:
        file_content: Content of the file.
        file_name: Name of the file.
        link_text: Text to display for the link.
        mime_type: MIME type of the file.
        
    Returns:
        HTML for a download link.
    """
    if isinstance(file_content, str):
        file_content = file_content.encode()
        
    b64 = base64.b64encode(file_content).decode()
    href = f'<a href="data:{mime_type};base64,{b64}" download="{file_name}" class="export-btn">{link_text}</a>'
    return href

def handle_input():
    """Handle user input when Enter is pressed."""
    if st.session_state.user_input:
        # Store user message
        user_message = st.session_state.user_input
        
        # Set a flag in session state instead of calling rerun directly
        st.session_state.pending_message = user_message
        
        # Clear input field
        st.session_state.user_input = ""

# Function to check if pending message is present and process it
def process_pending_message():
    if 'pending_message' in st.session_state:
        user_message = st.session_state.pending_message
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_message})
        
        # Clear pending message
        del st.session_state.pending_message
        
        # Get response with reasoning
        reasoning, answer = get_response(user_message)
        
        # Store reasoning content
        st.session_state.reasoning_contents.append(reasoning)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # Force rerun outside of callback
        st.rerun()

def main():
    """Main function to run the Streamlit app."""
    # Initialize session
    initialize_session()
    
    # App title
    st.markdown("# 🧠 DeepSeek R1 Chat")
    st.markdown("Chat with DeepSeek R1 - an AI that shows its reasoning process")
    
    # Process any pending message
    process_pending_message()
    
    # Sidebar
    with st.sidebar:
        st.header("Settings")
        
        # Reasoning toggle
        st.session_state.show_reasoning = st.toggle(
            "Show reasoning process", 
            value=st.session_state.show_reasoning
        )
        
        # Export options
        st.subheader("Export Conversation")
        
        if st.button("Export as Text"):
            if st.session_state.messages:
                text_content = create_text_file(st.session_state.messages)
                st.markdown(
                    get_download_link(text_content, "deepseek_chat.txt", "📥 Download Text", "text/plain"),
                    unsafe_allow_html=True
                )
            else:
                st.info("Nothing to export yet.")
        
        # Clear history button
        if st.button("Clear chat history", key="clear_history"):
            st.session_state.messages = []
            st.session_state.reasoning_contents = []
            st.rerun()
    
    # Display message history with reasoning
    for i, message in enumerate(st.session_state.messages):
        css_class = "user-message" if message["role"] == "user" else "bot-message"
        content = message["content"]
        
        # Apply formatting to the content
        formatted_content = preprocess_text(content)
        
        # For assistant messages, show message and reasoning
        if message["role"] == "assistant":
            # Container for the assistant's response
            msg_container = st.container()
            
            with msg_container:
                # Display message with formatting
                st.markdown(f'<div class="message {css_class}">{formatted_content}</div>', unsafe_allow_html=True)
                
                # Display reasoning if available and enabled
                reasoning_idx = i // 2
                if st.session_state.show_reasoning and reasoning_idx < len(st.session_state.reasoning_contents):
                    reasoning = st.session_state.reasoning_contents[reasoning_idx]
                    if reasoning:
                        # Format the reasoning with equation handling
                        formatted_reasoning = format_equation(reasoning)
                        st.markdown(f'<div class="reasoning-box">{formatted_reasoning}</div>', unsafe_allow_html=True)
        else:
            # Display regular user message
            st.markdown(f'<div class="message {css_class}">{formatted_content}</div>', unsafe_allow_html=True)
    
    # Chat input with Enter key handling
    st.text_area(
        "Your message:",
        key="user_input",
        height=100,
        on_change=handle_input,
        help="Press Enter to send"
    )
    
    # Add a small instructions line
    st.caption("Press Enter to send your message")

if __name__ == "__main__":
    main() 
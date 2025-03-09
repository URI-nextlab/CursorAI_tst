#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple CLI for DeepSeek Reasoning Model

A minimal command-line interface for interacting with the DeepSeek Reasoner model.
"""

import os
import sys
import re
from typing import List, Dict, Any
from dotenv import load_dotenv
from openai import OpenAI

# Dictionary for common mathematical symbols
MATH_SYMBOLS = {
    '^2': '²',
    '^3': '³',
    '^4': '⁴',
    '^5': '⁵',
    '^6': '⁶',
    '^7': '⁷',
    '^8': '⁸',
    '^9': '⁹',
    '^n': 'ⁿ',
    'sqrt': '√',
    'pi': 'π',
    'theta': 'θ',
    'alpha': 'α',
    'beta': 'β',
    'gamma': 'γ',
    'delta': 'δ',
    'epsilon': 'ε',
    'zeta': 'ζ',
    'eta': 'η',
    'lambda': 'λ',
    'mu': 'μ',
    'sigma': 'σ',
    'tau': 'τ',
    'phi': 'φ',
    'omega': 'ω',
    'Omega': 'Ω',
    'infinity': '∞',
    '<=': '≤',
    '>=': '≥',
    '!=': '≠',
    '==': '≡',
    '->': '→',
    '<-': '←',
    '*': '×',  # Use multiplication symbol
    'integral': '∫',
    'sum': '∑',
    'product': '∏',
    'approx': '≈',
    'prop': '∝',
    'in': '∈',
    'notin': '∉',
    'subset': '⊂',
    'union': '∪',
    'intersection': '∩',
    'therefore': '∴',
    'because': '∵',
    '+-': '±',
}

def format_equation(text: str) -> str:
    """
    Format mathematical equations for better display in terminal.
    
    Args:
        text: Text that may contain equations.
        
    Returns:
        Text with equations formatted for better readability.
    """
    # Replace common math symbols with their Unicode equivalents
    for symbol, unicode_char in MATH_SYMBOLS.items():
        # Use word boundaries for replacing whole words only
        if len(symbol) > 1 and symbol.isalpha():
            text = re.sub(r'\b' + symbol + r'\b', unicode_char, text)
        else:
            text = text.replace(symbol, unicode_char)
    
    # Handle fractions - convert a/b to ⁿ⁄ᵐ where possible
    text = re.sub(r'(\d+)/(\d+)', r'\1⁄\2', text)
    
    # Handle superscripts for single digit numbers
    text = re.sub(r'x\^(\d)', lambda m: f'x{superscript(m.group(1))}', text)
    text = re.sub(r'y\^(\d)', lambda m: f'y{superscript(m.group(1))}', text)
    text = re.sub(r'z\^(\d)', lambda m: f'z{superscript(m.group(1))}', text)
    text = re.sub(r'a\^(\d)', lambda m: f'a{superscript(m.group(1))}', text)
    text = re.sub(r'b\^(\d)', lambda m: f'b{superscript(m.group(1))}', text)
    text = re.sub(r'c\^(\d)', lambda m: f'c{superscript(m.group(1))}', text)
    text = re.sub(r'n\^(\d)', lambda m: f'n{superscript(m.group(1))}', text)
    
    # Format inline equation blocks that match common patterns
    text = re.sub(r'((?:\d+)?x\^2\s*(?:[-+]\s*\d+x)?\s*(?:[-+]\s*\d+)?)', lambda m: highlight_equation(m.group(1)), text)

    # Format equation blocks
    def format_eq_block(match):
        eq = match.group(1).strip()
        # Format the equation
        eq = highlight_equation(eq)
        # Add some spacing and highlight with box drawing characters
        width = max(len(eq) + 6, 20)
        padding = width - len(eq) - 4
        left_padding = padding // 2
        right_padding = padding - left_padding
        
        top_line = '┌' + '─' * (width - 2) + '┐'
        content_line = '│' + ' ' * left_padding + eq + ' ' * right_padding + '│'
        bottom_line = '└' + '─' * (width - 2) + '┘'
        
        return f"\n{top_line}\n{content_line}\n{bottom_line}\n"
    
    # Look for equation patterns like "x = y + z" at the beginning of lines or after punctuation
    text = re.sub(r'(?:^|\. |\n)([a-zA-Z0-9_]+\s*=\s*[^\.;!\?\n]+)', format_eq_block, text)
    
    return text

def superscript(text):
    """Convert text to superscript Unicode characters."""
    superscript_map = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
        '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
        'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ',
        'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
        'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ',
        'p': 'ᵖ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ',
        'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ'
    }
    return ''.join(superscript_map.get(char, char) for char in text)

def highlight_equation(eq):
    """Apply special formatting to highlight an equation."""
    # Make sure it's properly spaced
    eq = re.sub(r'([+\-*/=<>])', r' \1 ', eq)
    eq = re.sub(r'\s+', ' ', eq).strip()
    
    # Replace common patterns
    eq = eq.replace(' * ', ' × ')
    eq = eq.replace(' / ', ' ÷ ')
    eq = eq.replace(' - ', ' − ')  # Use minus sign instead of hyphen
    
    return eq

def init_client():
    """
    Initialize the OpenAI client with DeepSeek API configuration.
    
    Returns:
        The configured OpenAI client.
    """
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DeepSeek API key not found in environment variables")
    
    # Initialize client with compatible parameters
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    return client

def colored_text(text: str, color_code: str) -> str:
    """
    Apply color to text for terminal output.
    
    Args:
        text: The text to color.
        color_code: The ANSI color code.
        
    Returns:
        The colored text.
    """
    return f"\033[{color_code}m{text}\033[0m"

def format_box(text: str, width: int = 80, title: str = None) -> str:
    """
    Create a formatted box around text.
    
    Args:
        text: The text to put in the box.
        width: The width of the box.
        title: Optional title for the box.
        
    Returns:
        The formatted box as a string.
    """
    lines = text.split('\n')
    result = []
    
    # Top border with optional title
    if title:
        title_str = f" {title} "
        padding = (width - len(title_str) - 2) // 2
        result.append("╔" + "═" * padding + title_str + "═" * (width - padding - len(title_str) - 2) + "╗")
    else:
        result.append("╔" + "═" * (width - 2) + "╗")
    
    # Content
    for line in lines:
        # Handle lines longer than width by splitting them
        while len(line) > width - 4:
            result.append("║ " + line[:width - 4] + " ║")
            line = line[width - 4:]
        result.append("║ " + line + " " * (width - len(line) - 4) + " ║")
    
    # Bottom border
    result.append("╚" + "═" * (width - 2) + "╝")
    
    return "\n".join(result)

def get_response(client: Any, messages: List[Dict[str, str]], show_reasoning: bool = True) -> str:
    """
    Get a response from the DeepSeek Reasoner model.
    
    Args:
        client: The OpenAI client.
        messages: The conversation history.
        show_reasoning: Whether to show the reasoning process.
        
    Returns:
        The model's response.
    """
    try:
        # Create chat completion
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages,
            stream=True
        )
        
        # Process streaming response
        reasoning_content = ""
        content = ""
        reasoning_buffer = ""
        
        # Show reasoning process animation
        if show_reasoning:
            print(colored_text("\n" + format_box("Thinking Process", title="REASONING"), "36"))
            
        # Process stream chunks
        for chunk in response:
            if hasattr(chunk.choices[0].delta, 'reasoning_content') and chunk.choices[0].delta.reasoning_content:
                chunk_text = chunk.choices[0].delta.reasoning_content
                reasoning_content += chunk_text
                reasoning_buffer += chunk_text
                
                # Format and display reasoning in chunks for better responsiveness
                if show_reasoning:
                    # Check if we have a complete sentence or paragraph to format
                    if chunk_text.endswith('.') or chunk_text.endswith('\n'):
                        formatted_chunk = format_equation(reasoning_buffer)
                        print(colored_text(formatted_chunk, "36"), end="", flush=True)
                        reasoning_buffer = ""
                    else:
                        # For partial text, just show without formatting
                        print(colored_text(chunk_text, "36"), end="", flush=True)
            
            elif hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
                content += chunk.choices[0].delta.content
        
        # Display any remaining reasoning buffer
        if show_reasoning and reasoning_buffer:
            formatted_chunk = format_equation(reasoning_buffer)
            print(colored_text(formatted_chunk, "36"), end="", flush=True)
        
        # Add a newline after reasoning
        if show_reasoning and reasoning_content:
            print("\n")
        
        return content
    except Exception as e:
        print(f"\nError details: {type(e).__name__}: {str(e)}")
        return f"Error: {str(e)}"

def print_header():
    """Print the chat application header."""
    header = """
    DeepSeek Reasoner Chat

    Type your message or use these commands:
    /exit - Exit the chat
    /clear - Clear the conversation history
    /reasoning - Toggle reasoning process display
    """
    
    print(colored_text(format_box(header, title="DEEPSEEK REASONER"), "34"))  # Blue color

def main():
    """Run the main chat loop."""
    print_header()
    client = init_client()
    messages = []
    show_reasoning = True
    
    while True:
        try:
            # Get user input
            print("\n" + "─" * 80)
            user_input = input(colored_text("\n💬 You: ", "32"))  # Green
            
            # Handle commands
            if user_input.lower() == "/exit":
                print(colored_text("\nExiting chat. Goodbye!", "35"))
                sys.exit(0)
            elif user_input.lower() == "/clear":
                messages = []
                print(colored_text("\nConversation history cleared.", "35"))
                continue
            elif user_input.lower() == "/reasoning":
                show_reasoning = not show_reasoning
                status = "ON" if show_reasoning else "OFF"
                print(colored_text(f"\nReasoning process display: {status}", "35"))
                continue
            
            # Add user message to history
            messages.append({"role": "user", "content": user_input})
            
            # Get and display assistant response
            print(colored_text("\n🤖 DeepSeek Reasoner:", "33"))  # Yellow
            response = get_response(client, messages, show_reasoning)
            
            # Format equations in the response
            formatted_response = format_equation(response)
            
            # Display the final answer in a formatted box
            print(colored_text(format_box(formatted_response, title="ANSWER"), "33"))
            
            # Add assistant response to history (use original unformatted response)
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print(colored_text("\n\nInterrupted by user. Exiting...", "35"))
            sys.exit(0)
        except Exception as e:
            print(colored_text(f"\nError: {str(e)}", "31"))

if __name__ == "__main__":
    main() 
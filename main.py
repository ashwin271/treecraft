#!/usr/bin/env python3
"""
File Structure Creator - Main Entry Point
Creates directory structures from text-based tree representations.
"""

import argparse
from src.parser.tree_parser import TreeParser
from src.generator.file_generator import FileGenerator

def parse_arguments():
    """Set up command-line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Create directory structures from text-based tree representations"
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input file containing the tree structure"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=".",
        help="Output directory where the structure will be created (default: current directory)"
    )
    return parser.parse_args()

def main():
    """Main execution function."""
    args = parse_arguments()
    
    try:
        # Parse the input file
        with open(args.input_file, 'r') as f:
            tree_content = f.read()
        
        # Create parser and generator instances
        parser = TreeParser()
        generator = FileGenerator()
        
        # Parse the tree structure
        file_structure = parser.parse(tree_content)
        
        # Generate the directory structure
        generator.generate(file_structure, args.output)
        
        print(f"Successfully created directory structure in {args.output}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
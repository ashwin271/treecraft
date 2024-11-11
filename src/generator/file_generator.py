"""
File Generator Module
Creates actual files and directories from the parsed structure.
"""

import os
from typing import Dict

class FileGenerator:
    """Generates file system structure from parsed tree representation."""
    
    def generate(self, structure: Dict[str, any], base_path: str):
        """
        Generate the directory structure from the parsed representation.
        
        Args:
            structure (Dict[str, any]): Nested dictionary representing the file structure
            base_path (str): Base directory where the structure will be created
            
        Raises:
            OSError: If there's an error creating directories or files
        """
        self._create_structure(structure, base_path)
    
    def _create_structure(self, structure: Dict[str, any], current_path: str):
        """
        Recursively create the directory structure.
        
        Args:
            structure (Dict[str, any]): Current level of the structure
            current_path (str): Current path being processed
        """
        for name, contents in structure.items():
            path = os.path.join(current_path, name)
            
            if name.endswith('.py'):
                # Create empty Python file
                self._create_file(path)
            else:
                # Create directory
                self._create_directory(path)
                # Recurse into subdirectories
                self._create_structure(contents, path)
    
    def _create_directory(self, path: str):
        """Create a directory if it doesn't exist."""
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
    
    def _create_file(self, path: str):
        """Create an empty file if it doesn't exist."""
        if not os.path.exists(path):
            with open(path, 'w') as f:
                if path.endswith('.py'):
                    f.write('"""' + os.path.basename(path) + '\n"""\n\n')
            print(f"Created file: {path}")
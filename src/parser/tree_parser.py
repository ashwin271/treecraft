"""
Tree Parser Module
Parses text-based tree representations into a structured format.
"""

from typing import Dict, List
import re

class TreeParser:
    """Parses text-based tree structures into a dictionary representation."""
    
    def __init__(self):
        self.indent_pattern = re.compile(r'^[│├└─\s]+')
    
    def parse(self, content: str) -> Dict[str, any]:
        """
        Parse the tree structure text into a nested dictionary.
        
        Args:
            content (str): The input tree structure text
            
        Returns:
            Dict[str, any]: Nested dictionary representing the file structure
            
        Example input:
            src/
            ├── agents/
            │   ├── __init__.py
            │   └── agent.py
        """
        lines = content.strip().split('\n')
        structure = {}
        current_path = []
        prev_indent = -1
        
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
                
            # Calculate indent level
            indent = len(self.indent_pattern.match(line).group(0))
            name = line.strip().rstrip('/')
            
            # Adjust current path based on indent
            if indent > prev_indent:
                current_path.append(name)
            elif indent == prev_indent:
                current_path.pop()
                current_path.append(name)
            else:
                for _ in range(prev_indent - indent + 1):
                    current_path.pop()
                current_path.append(name)
            
            # Update structure
            self._update_structure(structure, current_path.copy())
            prev_indent = indent
            
        return structure
    
    def _update_structure(self, structure: Dict, path: List[str]):
        """
        Update the structure dictionary with the given path.
        
        Args:
            structure (Dict): The structure dictionary to update
            path (List[str]): The path to add to the structure
        """
        current = structure
        for i, item in enumerate(path[:-1]):
            if item not in current:
                current[item] = {}
            current = current[item]
        current[path[-1]] = {}
"""
Helper functions for the file structure creator.
"""

import os
from typing import List

def validate_path(path: str) -> bool:
    """
    Validate if a path is safe to create.
    
    Args:
        path (str): Path to validate
        
    Returns:
        bool: True if path is safe, False otherwise
    """
    # Check for absolute path
    if os.path.isabs(path):
        return False
    
    # Check for parent directory traversal
    if '..' in path.split(os.sep):
        return False
    
    return True

def clean_path(path: str) -> str:
    """
    Clean and normalize a path string.
    
    Args:
        path (str): Path to clean
        
    Returns:
        str: Cleaned path
    """
    return os.path.normpath(path)

def get_file_extension(path: str) -> str:
    """
    Get the file extension from a path.
    
    Args:
        path (str): Path to analyze
        
    Returns:
        str: File extension without the dot
    """
    return os.path.splitext(path)[1][1:]
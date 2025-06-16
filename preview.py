"""
Module for simulating and previewing GitHub contribution graphs locally.
Provides visualization of the commit pattern before actual commits are made.
"""

from typing import List, List
from PIL import Image, ImageDraw

class GraphPreview:
    """
    Handles the local preview of GitHub contribution graphs.
    """
    
    def __init__(self, width: int = 53, height: int = 7):
        """
        Initialize the GraphPreview with dimensions.
        
        Args:
            width (int): Width of the graph in weeks
            height (int): Height of the graph in days
        """
        self.width = width
        self.height = height
    
    def generate_preview(self, commit_dates: List[datetime]) -> Image.Image:
        """
        Generate a preview image of the contribution graph.
        
        Args:
            commit_dates (List[datetime]): List of dates with commits
            
        Returns:
            Image.Image: Preview image of the contribution graph
        """
        pass
    
    def save_preview(self, image: Image.Image, output_path: str) -> None:
        """
        Save the preview image to a file.
        
        Args:
            image (Image.Image): The preview image to save
            output_path (str): Path where to save the image
        """
        pass 
import os

def abs_ff_path(rel_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    abs_path = os.path.join(base_dir, rel_path)  
    return abs_path

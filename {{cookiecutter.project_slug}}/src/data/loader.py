import pandas as pd

def load_data(file_path):
    """
    Load data from various file formats.
    
    Parameters:
    -----------
    file_path : str
        Path to the data file
        
    Returns:
    --------
    pd.DataFrame
        Loaded data
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

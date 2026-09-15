import pandas as pd
import os

def process_data(file_path):
    """
    Reads a CSV file, processes the data, and returns a cleaned DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A cleaned DataFrame.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Drop rows with any missing values
    df.dropna(inplace=True)

    # Convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    return df

def multiply_column(df, column_name, factor):
    """
    Multiplies a specified column in the DataFrame by a given factor.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    column_name (str): The name of the column to multiply.
    factor (float): The factor by which to multiply the column.

    Returns:
    pd.DataFrame: The DataFrame with the specified column multiplied.
    """
    if column_name in df.columns:
        df[column_name] = df[column_name] * factor
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    return df

if __name__ == "__main__":
    # Example usage
    cleaned_df = process_data('data/synthetic_data.csv')
    cleaned_df = multiply_column(cleaned_df, 'feature1', 2.0)
    if os.path.exists('data'):
        pass
    else:
        os.makedirs('data')
    cleaned_df.to_csv('data/cleaned_data.csv', index=False)
    print("Data processed and saved to 'data/cleaned_data.csv'.")
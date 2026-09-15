import pandas as pd

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

if __name__ == "__main__":
    # Example usage
    cleaned_df = process_data('data/synthetic_data.csv')
    cleaned_df.to_csv('data/cleaned_data.csv', index=False)
    print("Data processed and saved to 'data/cleaned_data.csv'.")
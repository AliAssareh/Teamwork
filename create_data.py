import numpy as np
import pandas as pd
import os

np.random.seed(42)

def create_data(num_samples=1000):
    # Generate random data
    data = {
        'feature1': np.round(np.random.rand(num_samples), 2),
        'feature2': np.round(np.random.rand(num_samples), 2),
        'feature3': np.round(np.random.rand(num_samples), 2),
        'target': np.random.randint(0, 2, num_samples)
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    return df

if __name__ == "__main__":
    df = create_data()
    if os.path.exists('data'):
        pass
    else:
        os.makedirs('data')
    df.to_csv('data/synthetic_data.csv', index=False)
    print("Synthetic data created and saved to 'data/synthetic_data.csv'.")
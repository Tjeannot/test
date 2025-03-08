import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading Functions
def load_all_signals():
    """Load all signal data files and return them as a dictionary."""
    signals = {
        'altitude': pd.read_pickle("signals_altitude.pkl"),
        'fuel_flow': pd.read_pickle("signals_fuel_flow.pkl"),
        'speed': pd.read_pickle("signals_vitesse.pkl"),
        'wind': pd.read_pickle("signals_wind.pkl")
    }
    return signals

def print_dataframe_shapes(signals_dict):
    """Print the shapes of all dataframes in the signals dictionary."""
    for name, df in signals_dict.items():
        print(f"{name.title()} DataFrame shape: {df.shape}")

# Plotting Functions
def plot_signal_distribution(data, feature_name, bins=50):
    """Plot histogram and basic statistics for a given feature."""
    plt.figure(figsize=(10, 6))
    plt.hist(data.flatten(), bins=bins)
    plt.title(f'Distribution of {feature_name}')
    plt.xlabel(feature_name)
    plt.ylabel('Count')
    
    # Add statistics annotation
    stats = {
        'Mean': np.mean(data),
        'Std': np.std(data),
        'Min': np.min(data),
        'Max': np.max(data)
    }
    stats_text = '\n'.join([f'{k}: {v:.2f}' for k, v in stats.items()])
    plt.annotate(stats_text, xy=(0.95, 0.95), xycoords='axes fraction',
                bbox=dict(facecolor='white', alpha=0.8),
                ha='right', va='top')
    plt.show()

def plot_time_series(df, feature, flight_nums=None, figsize=(12, 6)):
    """Plot time series data for specified flights."""
    if flight_nums is None:
        flight_nums = np.random.choice(df.columns, 5, replace=False)
    
    plt.figure(figsize=figsize)
    for flight in flight_nums:
        plt.plot(df.index, df[flight], label=f'Flight {flight}')
    
    plt.title(f'{feature} Over Time')
    plt.xlabel('Time')
    plt.ylabel(feature)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_correlation_matrix(df, title='Feature Correlation Matrix'):
    """Plot correlation matrix for the given dataframe."""
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title(title)
    plt.show()

# Data Processing Functions
def detect_anomalies(df, feature, n_std=5):
    """Detect anomalies in a feature using the n-std method."""
    mean = df[feature].mean()
    std = df[feature].std()
    threshold_low = mean - n_std * std
    threshold_high = mean + n_std * std
    
    anomalies = df[
        (df[feature] < threshold_low) |
        (df[feature] > threshold_high) |
        (df[feature] < 0)  # For features that can't be negative
    ]
    
    return {
        'anomalies': anomalies,
        'stats': {
            'mean': mean,
            'std': std,
            'threshold_low': threshold_low,
            'threshold_high': threshold_high
        }
    }

def clean_dataset(df, features, n_std=5):
    """Clean dataset by removing anomalies from multiple features."""
    original_shape = df.shape
    clean_df = df.copy()
    
    for feature in features:
        anomaly_results = detect_anomalies(clean_df, feature, n_std)
        anomaly_indices = anomaly_results['anomalies'].index
        clean_df = clean_df.drop(anomaly_indices)
    
    print(f"Original dataset shape: {original_shape}")
    print(f"Cleaned dataset shape: {clean_df.shape}")
    print(f"Removed {original_shape[0] - clean_df.shape[0]} rows "
          f"({((original_shape[0] - clean_df.shape[0])/original_shape[0]*100):.2f}% of data)")
    
    return clean_df

def create_features(df):
    """Create derived features from the raw data."""
    features_df = df.copy()
    
    # Add rolling statistics
    window_sizes = [3, 5, 10]
    for window in window_sizes:
        features_df[f'altitude_rolling_mean_{window}'] = df['altitude'].rolling(window).mean()
        features_df[f'speed_rolling_mean_{window}'] = df['speed'].rolling(window).mean()
        features_df[f'fuel_flow_rolling_mean_{window}'] = df['fuel_flow'].rolling(window).mean()
    
    # Add rate of change features
    features_df['altitude_change'] = df['altitude'].diff()
    features_df['speed_change'] = df['speed'].diff()
    features_df['fuel_flow_change'] = df['fuel_flow'].diff()
    
    return features_df

def aggregate_flight_data(flight_num, signals_dict):
    """
    Aggregates data for a specific flight number from all dataframes.
    Returns a dataframe with columns: altitude, fuel_flow, speed, wind
    """
    # Extract data for the specified flight
    altitude = signals_dict['altitude'][flight_num].dropna().to_frame().rename(columns={flight_num: 'altitude'})
    fuel_flow = signals_dict['fuel_flow'][flight_num].dropna().to_frame().rename(columns={flight_num: 'fuel_flow'})
    speed = signals_dict['speed'][flight_num].dropna().to_frame().rename(columns={flight_num: 'speed'})
    wind = signals_dict['wind'][flight_num].dropna().to_frame().rename(columns={flight_num: 'wind'})
    
    # Merge all dataframes on their indices (timestamps)
    merged_df = altitude.merge(fuel_flow, left_index=True, right_index=True, how='inner')
    merged_df = merged_df.merge(speed, left_index=True, right_index=True, how='inner')
    merged_df = merged_df.merge(wind, left_index=True, right_index=True, how='inner')
    
    # Add flight number as a column
    merged_df['flight_num'] = flight_num
    
    # Reset index to make timestamp a column
    merged_df = merged_df.reset_index().rename(columns={'index': 'timestamp'})
    
    return merged_df 
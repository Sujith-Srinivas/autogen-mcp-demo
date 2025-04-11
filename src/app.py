#!/usr/bin/env python

import json
import sys
from pathlib import Path

def load_config():
    """Load configuration from config.json file."""
    config_path = Path(__file__).parents[1] / 'config.json'
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def load_sample_data():
    """Load sample data from the data directory."""
    data_path = Path(__file__).parents[1] / 'data' / 'sample.json'
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading sample data: {e}")
        return {}

def main():
    """Main application function."""
    config = load_config()
    print(f"Starting {config.get('app_name', 'Application')} v{config.get('version', '0.0.0')}")
    
    data = load_sample_data()
    print(f"Loaded {len(data)} sample items")
    
    print("Sample data summary:")
    for item in data:
        print(f"- {item['name']}: {item['description']}")

if __name__ == "__main__":
    main()
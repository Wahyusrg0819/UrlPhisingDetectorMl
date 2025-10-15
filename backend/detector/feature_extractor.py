import re

def extract_features(url):
    """Extract lexical features dari URL - HARUS IDENTIK dengan training code"""
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_www': 1 if 'www' in url else 0,  # Case-sensitive seperti training
        'has_https': 1 if 'https' in url else 0,  # Substring match seperti training
        'num_hyphens': url.count('-'),
        'num_slashes': url.count('/'),
        'has_numeric': 1 if bool(re.search(r'\d', url)) else 0,  # Regex seperti training
    }
    
    return [
        features['url_length'],
        features['num_dots'],
        features['has_www'],
        features['has_https'],
        features['num_hyphens'],
        features['num_slashes'],
        features['has_numeric']
    ]

import os
import joblib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .feature_extractor import extract_features

# Load Random Forest model saat startup
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'RandomForest_phishing_model.pkl')
try:
    model = joblib.load(MODEL_PATH)
    print(f"✓ Model loaded: {type(model).__name__}")
    print(f"  Classes: {model.classes_}")
    print(f"  Number of trees: {model.n_estimators}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None

@api_view(['POST'])
def predict_url(request):
    url = request.data.get('url', '')
    
    if not url:
        return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if model is None:
        return Response({'error': 'Model not loaded'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    try:
        # Extract features
        features = extract_features(url)
        
        # Predict using Random Forest
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        
        # Get class probabilities
        classes = model.classes_
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
        
        # Get confidence (probability of predicted class)
        pred_idx = list(classes).index(prediction)
        confidence = float(probabilities[pred_idx])
        
        return Response({
            'url': url,
            'prediction': prediction,
            'confidence': confidence,
            'probabilities': prob_dict,
            'features': {
                'url_length': features[0],
                'num_dots': features[1],
                'has_www': bool(features[2]),
                'has_https': bool(features[3]),
                'num_hyphens': features[4],
                'num_slashes': features[5],
                'has_numeric': bool(features[6])
            },
            'model_info': {
                'algorithm': 'Random Forest',
                'n_estimators': model.n_estimators,
                'classes': list(classes)
            }
        })
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

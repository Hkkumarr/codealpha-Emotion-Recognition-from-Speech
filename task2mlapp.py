import streamlit as st
import librosa
import numpy as np
import joblib
import tempfile

# Load Model
model = joblib.load(
    "emotion_model.pkl"
)

encoder = joblib.load(
    "label_encoder.pkl"
)

# Feature Extraction
def extract_features(file_path):

    audio, sample_rate = librosa.load(
        file_path,
        duration=3,
        offset=0.5
    )

    mfccs = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    return np.mean(
        mfccs.T,
        axis=0
    )

# Streamlit UI
st.set_page_config(
    page_title="Emotion Recognition",
    page_icon="🎤"
)

st.title(
    "🎤 Emotion Recognition from Speech"
)

st.write(
    "Upload a WAV audio file and predict emotion."
)

audio_file = st.file_uploader(
    "Choose Audio File",
    type=["wav"]
)

if audio_file is not None:

    st.audio(audio_file)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_file:

        temp_file.write(
            audio_file.read()
        )

        temp_path = temp_file.name

    features = extract_features(
        temp_path
    )

    features = features.reshape(
        1,
        -1
    )

    prediction = model.predict(
        features
    )

    emotion = encoder.inverse_transform(
        prediction
    )

    st.success(
        f"Predicted Emotion: {emotion[0]}"
    )

    probs = model.predict_proba(
        features
    )[0]

    st.subheader(
        "Prediction Confidence"
    )

    for label, prob in zip(
        encoder.classes_,
        probs
    ):

        st.write(
            f"{label}: {prob*100:.2f}%"
        )
### 📁 File: app.py

import streamlit as st
from segmenter import segment_rooftop
from analysis import estimate_roi

st.title("Solar Rooftop Analyzer with SAM")

uploaded = st.file_uploader("Upload satellite image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Original Image", use_column_width=True)
    with st.spinner("Segmenting rooftop..."):
        segmented_img, area_pixels = segment_rooftop(uploaded)
        st.image(segmented_img, caption="Detected Rooftop", use_column_width=True)

        # Optional: estimate area from pixels (assume 1 pixel ≈ 0.25 m²)
        area_m2 = area_pixels * 0.25
        cost, savings, roi = estimate_roi(area_m2)
        st.markdown(f"**Estimated Area (m²):** {round(area_m2, 2)}")
        st.markdown(f"**Installation Cost (₹):** {cost}")
        st.markdown(f"**Lifetime Savings (₹):** {savings}")
        st.markdown(f"**ROI (₹):** {roi}")


# 🌞 Solar Rooftop Analyzer using SAM (Segment Anything Model)

This project is a web-based AI tool that analyzes rooftop images to estimate their solar panel installation potential using Meta AI's **Segment Anything Model (SAM)**.

---

## 📌 Features

- Upload satellite or aerial images of rooftops.
- Perform rooftop segmentation using SAM (`vit_b`).
- Estimate potential area (in m²), installation cost, savings, and ROI.
- Streamlit interface for easy interaction.

---

## 🧾 Project Structure

```
├── app.py                 # Streamlit web app
├── segmenter.py          # SAM-based rooftop segmentation logic
├── analysis.py           # ROI and savings estimation logic
├── requirements.txt      # Required Python libraries
├── README.md             # Project instructions and links
```

---

## 📦 External Files Required

These files are large or external and **must be downloaded separately**:

1. ✅ **SAM Checkpoint (`sam_vit_b.pth`)**  
   Download from the official Segment Anything GitHub release:  
   [🔗 sam_vit_b.pth](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)

2. ✅ **segment_anything module**  
   Clone from GitHub:  
   ```bash
   git clone https://github.com/facebookresearch/segment-anything.git
   ```
   Place the folder inside your project directory or install it via pip:

   ```bash
   pip install git+https://github.com/facebookresearch/segment-anything.git
   ```

---

## 🛠️ Setup Instructions

1. **Create virtual environment (optional but recommended):**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # or `myenv\Scripts\activate` on Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and place `sam_vit_b.pth`** into your project root.

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. Open the browser at `http://localhost:8501`, upload a rooftop image, and see the analysis!

---

## 📷 Image Guidelines

- Upload satellite or aerial images of rooftops in JPG/PNG format.
- Recommended size: under 1024x1024 for faster processing.

---

## 🧠 Author Notes

- If SAM segmentation fails due to GPU/memory limits or API errors, fallback mechanisms or image resizing may be added.
- This project demonstrates real-world AI + energy application using vision models.

---

## ✅ License

This project is built for educational purposes under fair use of open research tools.

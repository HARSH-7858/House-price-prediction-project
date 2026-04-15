# Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Cloud

This project is configured for easy deployment on Streamlit Community Cloud.

### Prerequisites
- GitHub account
- This repository is public on GitHub
- Streamlit account (create one at https://streamlit.io/)

### Deployment Steps

1. **Go to Streamlit Community Cloud**
   - Visit: https://share.streamlit.io/

2. **Sign in with GitHub**
   - Click "New app"
   - You'll be prompted to authorize Streamlit to access your GitHub account

3. **Select Repository**
   - Repository: `HARSH-7858/House-price-prediction-project`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

4. **Advanced Settings (Optional)**
   - Python version: 3.11
   - Other settings can remain as default

5. **Deploy**
   - Click "Deploy"
   - Streamlit will build and deploy your app
   - Your app will be live at: `https://your-username-appname.streamlit.app`

### Troubleshooting

**Error: "The app's code is not connected to a remote GitHub repository"**

Solution:
- Ensure the repository is **public** on GitHub
- Verify you're on the `main` branch: `git branch -a`
- Make sure `streamlit_app.py` is in the root directory
- Ensure `requirements.txt` is in the root directory
- Commit all changes: `git add . && git commit -m "Deploy to Streamlit"`
- Push to GitHub: `git push origin main`

**App won't load dependencies**

Check:
- All dependencies are listed in `requirements.txt`
- Package names are spelled correctly (case-sensitive on Linux)
- Use `==` instead of `>=` for exact versions if you encounter issues

### File Structure for Deployment

```
House-price-prediction-project/
├── streamlit_app.py          (Main app file)
├── requirements.txt          (Dependencies)
├── README.md                 (Project documentation)
├── .streamlit/
│   └── config.toml          (Streamlit configuration)
├── .gitignore               (Git ignore rules)
├── House price prediction project.ipynb
└── [other project files]
```

### Updating the Deployed App

To update your deployed app:
1. Make changes locally
2. Commit: `git commit -am "Update app"`
3. Push: `git push origin main`
4. Streamlit Cloud automatically redeploys on every push to `main`

### App Features

Your deployed app will include:
- **Prediction Tab**: Real-time house price predictions with interactive sliders
- **Model Performance**: R² scores, MAE metrics, and visualization charts
- **Data Analysis**: Correlation heatmap and dataset statistics
- **About Tab**: Model information and feature descriptions

### Live Demo
Once deployed, you'll be able to share the URL with anyone. No installation required!

---

For more information, visit: https://docs.streamlit.io/streamlit-community-cloud

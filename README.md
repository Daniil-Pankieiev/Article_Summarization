## Getting Started

### Prerequisites
- Python 3.8 or higher
- Google Cloud CLI (https://cloud.google.com/sdk/docs/install#deb)
- Google Cloud Account with Vertex AI enabled (

### Installation


1. Clone the repository:

```bash
git clone https://github.com/Daniil-Pankieiev/Article_Summarization.git
```
2. Create and activate the virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
3. Install the necessary dependencies:

```bash
pip install -r backend/requirements.txt 
```


4. Run the backend server:

```bash
 uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
```
You can go to backend/main.py replace with your React frontend URL in the CORS settings.

And go to backend/settings.py and replace with your Google Cloud Project ID in the GOOGLE_CLOUD_PROJECT_ID setting.
5. Run the frontend:
```bash
 cd frontend
```
Copy .env.sample to .env and populate it with all required data.
```bash
 npm install
```
```bash
 npm start
```
## Contributing
Feel free to contribute to these enhancements, and let's make our product even better!
## Conclusion

Thank you for using the Arcticle Summarization 

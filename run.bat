@echo off
REM Navigate to the project directory
cd /d "%~dp0"

REM Install the required Python libraries
echo Installing required libraries...
pip install -r requirements.txt

REM Scrape the course data
echo Scraping course data...
python app/scraper.py

REM Generate the embeddings
echo Generating embeddings...
python app/embedding_model.py

REM Run the Gradio search interface
echo Starting the Gradio search interface...
python app.py

pause

@echo off
REM Navigate to the project directory (optional)
cd C:\Users\devad_pyiy\PycharmProjects\saucedemo
call .venv\Scripts\activate

REM Create a reports directory if it doesn't exist
if not exist reports (
    mkdir reports
)
REM Run Behave tests with the specified tag and output format
python -m behave --tags=swacedemo --format=json --outfile=reports/report.json

REM Optionally, pause the script to see any messages
pause




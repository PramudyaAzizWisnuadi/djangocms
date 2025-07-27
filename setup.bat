@echo off
:: Django Landing Page Setup Script for Windows

echo 🚀 Setting up Django Landing Page...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

:: Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo ⚡ Activating virtual environment...
call venv\Scripts\activate

:: Install requirements
echo 📥 Installing requirements...
pip install -r requirements.txt

:: Run migrations
echo 🗃️ Running database migrations...
python manage.py migrate

:: Setup initial data
echo 🌱 Setting up initial data...
python manage.py setup_initial_data
python manage.py setup_about_data
python manage.py setup_stats_data

:: Create superuser
echo 👤 Creating superuser account...
echo Please enter superuser details:
python manage.py createsuperuser

echo.
echo ✅ Setup completed successfully!
echo.
echo 🎉 Your Django Landing Page is ready!
echo.
echo To start the development server:
echo   python manage.py runserver
echo.
echo Then visit:
echo   🌐 Website: http://127.0.0.1:8000/
echo   ⚙️  Admin Panel: http://127.0.0.1:8000/admin/
echo.
echo Happy coding! 🚀
pause

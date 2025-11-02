@echo off
REM Git Pull Script for Robot

REM Check if robotName environment variable is set
if defined robotName (
    echo Your robot name is %robotName%
) else (
    echo Warning: Your robotName environment variable has not been set
)

echo.
echo git pull in five seconds
REM Uncomment the line below to add a 5 second delay
REM timeout /t 5 /nobreak >nul

git pull

REM Keep window open to see results (optional - comment out if not needed)
REM pause

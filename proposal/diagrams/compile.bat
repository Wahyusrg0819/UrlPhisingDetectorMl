@echo off
echo ========================================
echo  PlantUML Diagram Compiler
echo ========================================
echo.

REM Check if plantuml.jar exists
if not exist plantuml.jar (
    echo ERROR: plantuml.jar not found!
    echo.
    echo Please download plantuml.jar from:
    echo https://plantuml.com/download
    echo.
    echo Place it in this folder: %CD%
    echo.
    pause
    exit /b 1
)

echo Compiling diagrams...
echo.

echo [1/4] Compiling system-flowchart.puml...
java -jar plantuml.jar system-flowchart.puml

echo [2/4] Compiling usecase-diagram.puml...
java -jar plantuml.jar usecase-diagram.puml

echo [3/4] Compiling sequence-diagram.puml...
java -jar plantuml.jar sequence-diagram.puml

echo [4/4] Compiling architecture-diagram.puml...
java -jar plantuml.jar architecture-diagram.puml

echo.
echo ========================================
echo  Done! PNG files generated:
echo ========================================
echo  - system-flowch

#!/bin/bash

echo "Compiling PlantUML diagrams..."
echo ""

java -jar plantuml.jar system-flowchart.puml
java -jar plantuml.jar usecase-diagram.puml
java -jar plantuml.jar sequence-diagram.puml
java -jar plantuml.jar architecture-diagram.puml
java -jar plantuml.jar process-flowchart.puml
java -jar plantuml.jar logic-flowchart.puml
java -jar plantuml.jar feature-extraction-flowchart.puml
java -jar plantuml.jar model-prediction-flowchart.puml
java -jar plantuml.jar sdlc-waterfall.puml
java -jar plantuml.jar sdlc-circular.puml
java -jar plantuml.jar sdlc-timeline.puml
java -jar plantuml.jar sdlc-phases-detail.puml

echo ""
echo "Done! 12 PNG files generated."

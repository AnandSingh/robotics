#!/bin/bash 


# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color (reset)

echo ">> Executing      : $0"
echo ">> RobotName File : $1"
echo ">> Python File    : $2"

robotName=$(cat $1)
export ROBOT_NAME=$robotName

# Check if the environment variable is set
if [ -z "$ROBOT_NAME" ]; then
  echo -e  "${RED} Your Robot Name is NOT set.${NC}"

else
  echo -e "${GREEN}Your Robot Name is ${YELLOW}$robotName${NC}"

  filename=$(basename "$2")
  if [[ "${filename##*.}" != "py" ]]; then
    echo -e "${RED}Not a Python file, so exiting !!!${NC}"
  else
      echo -e "${GREEN}Loading $2 on  ${YELLOW}$ROBOT_NAME${NC}"
      pybricksdev run ble --name $ROBOT_NAME $2
      echo -e "${GREEN}------- DONE ---------${NC}"
  fi
fi
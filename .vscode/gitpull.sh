#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'

NC='\033[0m' # No Color (reset)

robotName=$(cat /config/workspace/.robotName)

export ROBOT_NAME=$robotName


# Check if the environment variable is set
if [ -z "$ROBOT_NAME" ]; then
  echo -e  "${RED} Your Robot Name is NOT set.${NC}"
else
  echo -e "${GREEN}Your Robot Name is '$ROBOT_NAME' !!${NC}"
fi


echo -e "${YELLOW}Doing git fetch and pull ...${NC}"
#sleep 3
git fetch && git pull
echo -e "${YELLOW}------- DONE -------${NC}"
#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Copy systemd scripts to /lib/systemd/system/ridder.service"

# because we need the script to run as root
sudo cp $DIR/ridder.service /lib/systemd/system/ridder.service
sudo systemctl daemon-reload

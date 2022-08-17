#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Copy systemd scripts to /etc/systemd/system/"

sudo cp $DIR/ridder.service /etc/systemd/system/ridder.service

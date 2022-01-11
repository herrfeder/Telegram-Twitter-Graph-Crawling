#!/bin/bash

set -a
source secrets.env
set +a

python3 $1

#!/bin/bash

set -a
source secrets.env
set +a

python3 02_crawl_telegram.py
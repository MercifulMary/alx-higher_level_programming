#!/bin/bash
# Sends a GET request to a given URL and displays response status code.
curl -s -o /dev/null -w "%{response_code}" "$1"

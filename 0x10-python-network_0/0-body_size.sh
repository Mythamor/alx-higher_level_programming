#!/usr/bin/env bash
# Sends request to URL, & display size of the body of the response
curl -sI "$1" | grep "content-length:" | cut -f2 -d' '

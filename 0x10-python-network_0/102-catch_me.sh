#!/bin/bash
#  request to 0.0.0.0:5000/catch_me; server respond - You got me!
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "User_Id=98" -H "Origin: X-School"

#!/bin/bash
echo "<!DOCTYPE html><html><body>"
for filename in $1/*; do
echo "<img src=\"$filename\"/>"
done
echo "</body></html>"

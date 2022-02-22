#!/bin/bash
set -e
make -f Makefile html
cp ./build/html ./docs
cp ./build/doctrees ./docs/.doctrees
cp ./CNAME ./docs
echo -n ""> ./docs/.nojekyll
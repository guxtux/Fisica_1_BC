#!/bin/sh

arg=${1:-.}
exts="aux bbl bcf blg brf dvi fdb_latexmk fdb_latexmk fls idx ilg ind lof log lol lot nav out ps run.xml toc snm synctex.gz vrb"

if [ -d $arg ]; then
    for ext in $exts; do
         rm -f $arg/*.$ext
    done
else
    for ext in $exts; do
         rm -f $arg.$ext
    done
fi	
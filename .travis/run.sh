#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

python build.py
if [[ "$(uname -s)" == 'Darwin' ]]; then
    conan user -r upload_repo -p ${CONAN_PASSWORD} ${CONAN_USERNAME}
    conan upload -r upload_repo zlib/1.2.8@lasote/stable --all --force
    conan upload -r upload_repo Boost/1.62.0@lasote/stable --all --force
fi

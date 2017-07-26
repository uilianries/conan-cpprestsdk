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
    echo "TODO (uilian.ries): Remove after upload all packages"
    conan upload -r upload_repo zlib/1.2.8@lasote/stable --all --force || true
    conan upload -r upload_repo Boost/1.62.0@lasote/stable --all --force || true
fi

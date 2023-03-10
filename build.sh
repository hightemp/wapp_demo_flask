#!/bin/bash

CFILE=wapp_demo_flask
PORT=5032

PYINSTALLER=pyinstaller
PYINSTALLER_DOCKER="docker run -v $PWD:/src fydeinc/pyinstaller "
PYINSTALLER_DOCKER="docker run -v $PWD:/src/ cdrx/pyinstaller-linux:python3"
PYINSTALLER_BUILD="docker build -t $CFILE/pyinstaller-linux:python3 . "
PYINSTALLER_DOCKER="docker run -v $PWD:/src/ $CFILE/pyinstaller-linux:python3 "
PYINSTALLER_DOCKER_PARAMS=" -F --path . --add-data=templates:templates --add-data=static:static --hidden-import 'main' --hidden-import 'baselib' --hidden-import 'database' --hidden-import 'request_vars' __main__.py"

echo '__DEBUG__='>.env
if [ "$1" == "flask" ]; then
    echo '__DEBUG__=1' > .env
    export FLASK_DEBUG=1
    export FLASK_APP=__init__.py 
    python3 -m flask run --extra-files . --with-threads -h0.0.0.0 -p$PORT
elif [ "$1" == "flask_db_init" ]; then
    echo '__DEBUG__=1' > .env
    export FLASK_DEBUG=1
    export FLASK_APP=__init__.py 
    python3 -m flask db init
elif [ "$1" == "flask_db_migrate" ]; then
    echo '__DEBUG__=1' > .env
    export FLASK_DEBUG=1
    export FLASK_APP=__init__.py 
    python3 -m flask db migrate
elif [ "$1" == "pyupdater" ]; then
    VER="$2"
    if [ "$VER" == "" ]; then
        VER=$(echo `cat VERSION`)
    fi
    pyupdater build --app-version $VER $PYINSTALLER_DOCKER_PARAMS
    cp dist/__main__ ../$CFILE.bin
    if [ "$2" == "run" ]; then
        ../$CFILE.bin  --bind 0.0.0.0:$PORT -w 10
    fi
elif [ "$1" == "pyinst" ]; then
    $PYINSTALLER $PYINSTALLER_DOCKER_PARAMS
    cp dist/__main__ ../$CFILE.bin
    if [ "$2" == "run" ]; then
        ../$CFILE.bin  --bind 0.0.0.0:$PORT -w 10
    fi
elif [ "$1" == "pyinst_docker" ]; then
    docker build -t $CFILE/pyinstaller-linux:python3 .
    $PYINSTALLER_DOCKER "$PYINSTALLER $PYINSTALLER_DOCKER_PARAMS"
    cp dist/__main__ ../$CFILE.bin
    if [ "$2" == "run" ]; then
        ../$CFILE.bin  --bind 0.0.0.0:$PORT -w 10
    fi
elif [ "$1" == "zipapp" ]; then
    # cp .env ..
    cd ..
    python3 -m zipapp $CFILE -p "/usr/bin/env python3"
    rm ./$CFILE.database.db
    echo $PWD/$CFILE.pyz
    if [ "$2" == "run" ]; then
        ./$CFILE.pyz --bind 0.0.0.0:$PORT -w 10
    fi
fi

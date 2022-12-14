#!/usr/bin/env bash

DB_USER=`cat .env | grep -o -P --color=no "(?<=DB_USER=)\w+"`
DATABASE=`cat .env | grep -o -P --color=no "(?<=DB_DATABASE=)\w+"`

show_help() {
    echo "usage: $0 [{run,start,help,install}]"
    echo ""
    echo "  run,start   start the web application (via flask)"
    echo "  help        show this help message and exit"
    echo "  install     setup the requirements for the app"
    echo "              (dependencies and software)"
    echo "  snapshot    record the most recent database snapshot"
    echo "              and pip requirements"
    echo ""
}

setup_app() {
    if ! [[ -v VIRTUAL_ENV ]]; then
        source venv/bin/activate;
    fi
    pip install -r requirements.txt;
    mysql -u "${DB_USER}" -e "DROP DATABASE IF EXISTS ${DATABASE}; CREATE DATABASE ${DATABASE}";
    if [[ -f "${DATABASE}.sql" ]]; then
        mysql -u "${DB_USER}" "${DATABASE}" < "${DATABASE}.sql";
    fi
}

run_app() {
    if ! [[ -v VIRTUAL_ENV ]]; then
        source venv/bin/activate;
    fi

    if [[ "${1:-production}" =~ debug ]]; then
        export FLASK_DEBUG=1
    fi
    export FLASK_APP=app

    flask run
}

snapshot_data() {
    if ! [[ -v VIRTUAL_ENV ]]; then
        source venv/bin/activate;
    fi

    mysqldump "${DATABASE}" > "${DATABASE}.sql"
    pip freeze > requirements.txt
}

ARG="${1:-start}"
case "${ARG//-/}" in
    h|help)
        show_help
        ;;
    run|start)
        run_app "${2:-production}"
        ;;
    i|install|restore)
        setup_app
        ;;
    backup|snapshot)
        snapshot_data
        ;;
esac
#!/usr/bin/env bash

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
    #mysql -u root -e "DROP DATABASE IF EXISTS attendance; CREATE DATABASE attendance";
    #mysql -u root attendance < "Attendance.sql";
}

run_app() {
    if ! [[ -v VIRTUAL_ENV ]]; then
        source venv/bin/activate;
    fi

    export FLASK_ENV="${2:-production}"
    export FLASK_APP=app

    flask run
}

snapshot_data() {
    if ! [[ -v VIRTUAL_ENV ]]; then
        source venv/bin/activate;
    fi

    # mysqldump attendance > Attendance.sql
    pip freeze > requirements.txt
}

ARG="${1:-start}"
case "${ARG//-/}" in
    h|help)
        show_help
        ;;
    run|start)
        run_app
        ;;
    i|install|restore)
        setup_app
        ;;
    backup|snapshot)
        snapshot_data
        ;;
esac
#!/bin/bash
PS_INFO_FILE="/home/${USER}/netstat-report"
NEW_PS_INFO_FILE="${PS_INFO_FILE}_temp"
RED='\033[0;31m'
NC='\033[0m'
FILE_NAME="$0"
function_create_report() {
    if [[ -f $PS_INFO_FILE ]]
    then
        netstat -pantx 2>/dev/null > $NEW_PS_INFO_FILE
    else
        netstat -pantx 2>/dev/null > $PS_INFO_FILE
        cp $PS_INFO_FILE $NEW_PS_INFO_FILE
    fi
    if [[ "`stat -c%s $PS_INFO_FILE`" != "`stat -c%s $NEW_PS_INFO_FILE`" ]]
    then
        cp $NEW_PS_INFO_FILE "${NEW_PS_INFO_FILE}_`date +%F-%H-%M-%S`"
        echo -e "$RED A new process has been created. See file ${NEW_PS_INFO_FILE}_`date +%D-%H-%M-%S`"
        echo -e "$NC"
    fi
}

usage() {
    echo "./$FILE_NAME "
    echo "Report the modification in services from first time when this script was run"
}

if [ "$#" -ge 1 ]
then
    usage
else
    function_create_report
fi

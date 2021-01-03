#!/bin/bash

# 実行するコマンド
COM1="python3 /home/sugimoto/pomodoro/app.py"

CMDNAME=`basename $0`
# 実行時に指定された引数の数が1でなければエラーを出力して終了
if [ $# -ne 1 ]; then
    # 標準出力を標準エラー出力にマージする
    echo "Usage: $CMDNAME [--start or --stop]" 1>&2
    exit 1
fi

#プロセスを実行
if [ "$1" = '--start' -o "$1" = '-s' ]; then
    # 一度終了処理を実行
    pkill -e -f -9 "$COM1"
    cd /home/kenya/work/my_study/realsense
    echo "`date '+%Y/%m/%d %H:%M:%S'` プログラムの実行開始"
    # 標準出力を出さずに実行
    ${COM1}
    echo "プログラムの実行終了"
    exit 0
fi

#プロセスを終了
if [ "$1" = '--stop' -o "$1" = '-t' ]; then
    pkill -e -f -9 "$COM1"
    exit 0
fi

exit 0



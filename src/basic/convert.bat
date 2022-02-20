@ECHO off
REM UTF-8へ変換
CHCP 65001

REM メタデータの準備
SET STR_BEFORE=CURRENT_DATE
SET STR_AFTER=%DATE%

SET FILE_INPUT=testrm.yaml.template
SET FILE_OUTPUT=testrm.yaml
DEL %FILE_OUTPUT%

SETLOCAL enableDelayedExpansion
FOR /f "delims=" %%a in (%FILE_INPUT%) do (
  SET line=%%a
  ECHO !line:%STR_BEFORE%=%STR_AFTER%! >> %FILE_OUTPUT%
)
ENDLOCAL

REM フォーマット変換
pandoc --toc -s --template=template.html -f markdown -t html -o testrm.html --metadata-file testrm.yaml testrm.md

REM SHIFT-JISへ変換
CHCP 932
ECHO on

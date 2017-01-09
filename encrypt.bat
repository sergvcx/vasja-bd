"%AES%"\aescrypt -e *.json
if %ERRORLEVEL% neq 0 exit /b
del *.json
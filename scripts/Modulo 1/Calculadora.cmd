@ echo off
cls
set "contador=-2"
echo Calculadora de Direcciones IP
echo ******************************
echo Posibles IPs
echo **********************
for /l %%a in (0,1,1) do (
for /l %%b in (0,1,1) do (
for /l %%c in (0,1,1) do (
for /l %%d in (0,1,1) do (
for /l %%e in (0,1,1) do (
for /l %%f in (0,1,1) do (
for /l %%g in (0,1,1) do (
for /l %%h in (0,1,1) do (
for /l %%i in (0,1,1) do (
for /l %%j in (0,1,1) do (
  echo 11000000.%%a%%b%%c%%d%%e%%f%%g%%h.00001%%i0%%j.00010111
  set /a "contador+=1"
)
)
)
)
)
)
)
)
)
)
echo Las IPs posibles para este script son: %contador%
pause
for /l %%j in (128, 1 ,131) do (
	for /l %%i in (1, 1 ,255) do (
	ping 192.168.%%j.%%i -n 1
	)
)
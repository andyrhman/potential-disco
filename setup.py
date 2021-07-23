import cx_Freeze

executables = [cx_Freeze.Executable("Tombol.py")]

cx_Freeze.setup(
	name = "Game Menghindar",
	options={'bulid_exe': {"packages":["pygame"],
							"include_files":["Ucycf5C2.png", "Lawan Arah.png", "701fed9bd55ea18.png", "Lawan Arah Icon.png", "Undertale OST - Snowy Extended.mp3", "bounce.wav"]}},
	executables = executables					
	)
import cx_Freeze

executables = [cx_Freeze.Executable('index.py')]

cx_Freeze.setup(
    name="Space Planet",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['img']}},

    executables = executables
    
)
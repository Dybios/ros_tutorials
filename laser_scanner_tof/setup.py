from setuptools import setup, Extension

extension = Extension(
    'vl53l0x_python',
    define_macros=[],
    include_dirs=['.', 'include/${PROJECT_NAME}/Api/core/inc', 'include/${PROJECT_NAME}/platform/inc'],
    libraries=[],
    library_dirs=[],
    sources=['include/${PROJECT_NAME}/Api/core/src/vl53l0x_api_calibration.c',
             'include/${PROJECT_NAME}/Api/core/src/vl53l0x_api_core.c',
             'include/${PROJECT_NAME}/Api/core/src/vl53l0x_api_ranging.c',
             'include/${PROJECT_NAME}/Api/core/src/vl53l0x_api_strings.c',
             'include/${PROJECT_NAME}/Api/core/src/vl53l0x_api.c',
             'include/${PROJECT_NAME}/Api/platform/src/vl53l0x_platform.c',
             'python_lib/vl53l0x_python.c'])

setup(name='VL53L0X',
      version='1.0.4',
      ext_modules=[extension],
      package_dir={'': 'src'},
      py_modules=['VL53L0X'],

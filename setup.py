from setuptools import setup, find_packages

# declare these here since we use them in multiple places
_tests_require = [
    'pytest',
    'pytest-cov',
    'flake8',
]


setup(
    # package info
    name='projectDani',
    description='Provee una interfaz al usuario para que autogenere reportes de transacciones',
    # version='0.0.0',
    url='http://your/url/here',
    author='Daniel Quintana',
    author_email='changeme@example.com',
    packages=find_packages(exclude=['tests', 'tests.*']),


    # scripts to install to usr/bin
    entry_points={
        'console_scripts': [
            'generadorDeReportes=generadorDeReportes.cli:generadorDeReportes_main'
        ]
    },


    # run time requirements
    # exact versions are in the requirements.txt file
    install_requires=[],

    # need this for setup.py test
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],

    # needs this if using setuptools_scm
    use_scm_version=True,

    # test dependencies
    tests_require=_tests_require,
    extras_require={
        # this allows us to pip install .[test] for all test dependencies
        'test': _tests_require,
    }
)

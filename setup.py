from setuptools import setup

setup(
    name='coopkit',
    version='1.0.0',
    description='Cockpit SYSTEMEOSIA – CoopKit IA Santé Éthique',
    author='Mohammed Ilyes Zoubirou',
    author_email='contact@systemeosia.org',
    py_modules=['generate_format'],
    entry_points={
        'console_scripts': [
            'coopkit = generate_format:main',
        ],
    },
    install_requires=[
        'qrcode',
        'fpdf',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)


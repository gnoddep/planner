from setuptools import setup, find_packages

setup(
    name='planner',
    version='0.0.dev0',
    license='MIT',

    description='Planner',
    url='https://nerdman.org/',

    author='Peter Gnodde',
    author_email='peter@gnodde.org',

    project_urls={
        'Bug Tracker': 'https://nerdman.org/code',
        'Documentation': 'https://nerdman.org/code',
        'Source Code': 'https://nerdman.org/code',
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'LICENSE :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],

    python_requires='>=3.8',

    install_requires=[
        'textx',
    ],

    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'tox',
        ],
    },

    packages=find_packages(exclude=['test']),
    package_data={
        '': ['*.md', '*.tx'],
    },
)

from setuptools import setup, find_packages

setup(
    name='DevSearch',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.3.2',
        'Flask-Babel>=3.1.0',
        'requests>=2.28.0'
    ],
    entry_points={
        'console_scripts': [
            'devsearch=app:app.run'
        ]
    },
    author='DevSearch Team',
    description='A bilingual Flask search engine using Google API with Tailwind CSS UI.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8'
)
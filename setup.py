from setuptools import setup, find_packages

setup(
    name='Array_Sqrt',
    version='1.0.0',
    description='Function that returns the square root',
    author='Bhargav Jethwa, Mithil Dave, Nirav Patel, Parth Kanakiya, Raj Shah',
    author_email='bjethwa@ncsu.edu',
    url='https://github.com/Nirav1929/A_Good_Repo',
    license='MIT',
    packages=find_packages(),
    # include = ['Code']),
    long_description='...',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Data Structure',
    ],
    
    install_requires=[
    'numpy==1.21.2',
    ]
)
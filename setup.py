from setuptools import setup, find_packages

setup(name='pdbtools', 
      version='0.1',
      packages=find_packages(),
      url='https://github.com/yizaochen/pdbtools.git',
      author='Yizao Chen',
      author_email='yizaochen@gmail.com',
      install_requires=[
          'numpy'
      ]
      )
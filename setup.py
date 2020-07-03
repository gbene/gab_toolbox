from distutils.core import setup
with open('README.md') as f:
    long_description = f.read()

setup(
      
      
      name = 'gab_toolbox',
      packages = ['gab_toolbox'],
      version = '0.2.32' ,
      license = 'MIT',
      description = 'Functions that I recurrenlty use in other scripts.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author = 'Gabriele Benedetti',
      author_email = 'gabri.benedetti@gmail.com',
      url = 'https://github.com/gbene',
      download_url = 'https://github.com//gbene/gab_toolbox/archive/v0.2.32.tar.gz' ,
      keywords = ['formatting','files','opening','writing','conversions','latex','bibtex'],
      install_requires = [''],
      classifiers=[
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          ],
)
   

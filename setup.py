from distutils.core import setup
setup(
  name = 'PetitPrinc3',         # How you named your package folder (MyLib)
  packages = ['PetitPrinc3'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "PetitPrinc3's libraries",   # Give a short description about your library
  author = 'PetitPrinc3',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/PetitPrinc3',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PetitPrinc3/PetitPrinc3',    # I explain this later on
  keywords = ['PetitPrinc3'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU License',   # Again, pick a license
    'Programming Language :: Python :: 3.12',      #Specify which pyhton versions that you want to support
  ],
)
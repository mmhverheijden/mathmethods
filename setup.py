from distutils.core import setup
setup(
  name = 'Math_methods',         # How you named your package folder (MyLib)
  packages = ['Math_methods'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Choose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple package to learn how to work with pip',   # Give a short description about your library
  author = 'Mike Verheijden',                   # Type in your name
  author_email = 'mmhverheijden@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mmhverheijden/maths_testpackage',   # Provide either the link to your github or to your website
  download_url = ' ',    # I explain this later on
  keywords = ['Maths', 'Test', 'Pip'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          '',
          '',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which pyhton versions that you want to support
  ],
)
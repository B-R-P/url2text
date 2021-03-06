from distutils.core import setup
setup(
  name = 'url2text',         # How you named your package folder (MyLib)
  packages = ['url2text'],   # Chose the same as "name"
  version = '0.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Extract text from website',   # Give a short description about your library
  author = 'Bijin Regi Panicker',                   # Type in your name
  author_email = 'bijinregipanicker@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/B-R-P/url2text',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/B-R-P/url2text/archive/0.01.zip',    # I explain this later on
  keywords = ['url2text', 'urltotext', 'website2text','websitetotext'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'urllib3',
          'bs4',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

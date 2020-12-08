import setuptools

setuptools.setup(
        name='SaveThatSong',
        version='2.1',
         classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
                     ],
        packages=setuptools.find_packages(),
        description=('This is a python script that downloads songs and even playlists from Spotify and YouTube very easily'),
        scripts=['savethatsong'],
        url='https://github.com/ArjunxyzSatish/SaveThatSong',
        author='Arjun Satish'
    )

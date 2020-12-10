import setuptools

setuptools.setup(
        name='SaveThatSong',
        version='3.7.3',
         classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
                     ],
        packages=setuptools.find_packages(),
        install_requires=[
                    'youtube_dl',
                    'youtube_search',
                    'spotipy',
                    #'ffmpeg'
                    ],
        description=('This is a python script that downloads songs and even playlists from Spotify and YouTube very easily'),
        scripts=['sts'],
        url='https://github.com/ArjunxyzSatish/SaveThatSong',
        author='Arjun Satish'
    )

"""Write a program that choose a random website name from list and open it in your browser"""

import webbrowser
from random import choice

random_page_generator = ['http://www.google.com',
                         'https://www.youtube.com/',
                         'https://www.linkedin.com/in/ayman-ibrahim-a9b8411'
                         ]
webbrowser.open(choice(random_page_generator))

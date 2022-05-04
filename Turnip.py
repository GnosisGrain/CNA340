1. """Turnip in a Case, inspired and directly by Carrot in a Box by Al Sweigart"""
  6.
  7. import random
  8.

 22. input('Press Enter to begin...')
 23.
 24. p1Name = input('Human player 1, enter your name: ')
 25. p2Name = input('Human player 2, enter your name: ')
 26. playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)
 27.
 28. print('''HERE ARE TWO BOXES:
 29.   __________     __________
 30.  /         /|   /         /|
 31. +---------+ |  +---------+ |
 32. |   RED   | |  |   GOLD  | |
 33. |   BOX   | /  |   BOX   | /
 34. +---------+/   +---------+/''')
 35.
 36. print()
 37. print(playerNames)
 38. print()
 39. print(p1Name + ', you have a RED box in front of you.')
 40. print(p2Name + ', you have a GOLD box in front of you.')
 41. print()
 42. print(p1Name + ', you will get to look into your box.')
 43. print(p2Name.upper() + ', close your eyes and don\'t look!!!')
 44. input('When ' + p2Name + ' has closed their eyes, press Enter...')
 45. print()
 46.
 47. print(p1Name + ' here is the inside of your box:')
 48.
 49. if random.randint(1, 2) == 1:
 50.     turnipInFirstBox = True
 51. else:
 52.     turnipInFirstBox = False
 53.
 54. if turnipInFirstBox:
 55.     print('''
 56.    ___VV____
 57.   |   VV    |
 58.   |   VV    |
 59.   |___||____|    __________
 60.  /    ||   /|   /         /|
 61. +---------+ |  +---------+ |
 62. |   RED   | |  |   GOLD  | |
 63. |   BOX   | /  |   BOX   | /
 64. +---------+/   +---------+/
 65.  (Turnip!)''')
 66.     print(playerNames)
 67. else:
 68.     print('''
 69.    _________
 70.   |         |
 71.   |         |
 72.   |_________|    __________
 73.  /         /|   /         /|
 74. +---------+ |  +---------+ |
 75. |   RED   | |  |   GOLD  | |
 76. |   BOX   | /  |   BOX   | /
 77. +---------+/   +---------+/
 78. (no Turnip!)''')
 79.     print(playerNames)
 80.
 81. input('Press Enter to continue...')
 82.
 83. print('\n' * 100)  # Clear the screen by printing several newlines.
 84. print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
 85. input('Press Enter to continue...')
 86.
 87. print()
 88. print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
 89. print('  1) There is a turnip in my box.')
 90. print('  2) There is not a turnip in my box.')
 91. print()
 92. input('Then press Enter to continue...')
 93.
 94. print()
 95. print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
 96. while True:
 97.     response = input('> ').upper()
 98.     if not (response.startswith('Y') or response.startswith('N')):
 99.         print(p2Name + ', please enter "YES" or "NO".')
100.     else:
101.         break
102.
103. firstBox = 'RED '  # Note the space after the "D".
104. secondBox = 'GOLD'
105.
106. if response.startswith('Y'):
107.     turnipInFirstBox = not turnipInFirstBox
108.     firstBox, secondBox = secondBox, firstBox
109.
110. print('''HERE ARE THE TWO BOXES:
111.   __________     __________
112.  /         /|   /         /|
113. +---------+ |  +---------+ |
114. |   {}  | |  |   {}  | |
115. |   BOX   | /  |   BOX   | /
116. +---------+/   +---------+/'''.format(firstBox, secondBox))
117. print(playerNames)
118.
119. input('Press Enter to reveal the winner...')
120. print()
121.
122. if turnipInFirstBox:
123.     print('''
124.    ___VV____      _________
125.   |   VV    |    |         |
126.   |   VV    |    |         |
127.   |___||____|    |_________|
128.  /    ||   /|   /         /|
129. +---------+ |  +---------+ |
130. |   {}  | |  |   {}  | |
131. |   BOX   | /  |   BOX   | /
132. +---------+/   +---------+/'''.format(firstBox, secondBox))
133.
134. else:
135.     print('''
136.    _________      ___VV____
137.   |         |    |   VV    |
138.   |         |    |   VV    |
139.   |_________|    |___||____|
140.  /         /|   /    ||   /|
141. +---------+ |  +---------+ |
142. |   {}  | |  |   {}  | |
143. |   BOX   | /  |   BOX   | /
144. +---------+/   +---------+/'''.format(firstBox, secondBox))
145.
146. print(playerNames)
147.
148. # This modification made possible through the 'turnipInFirstBox' variable
149. if turnipInFirstBox:
150.     print(p1Name + ' is the winner!')
151. else:
152.     print(p2Name + ' is the winner!')
153.
154. print('Thanks for playing!')

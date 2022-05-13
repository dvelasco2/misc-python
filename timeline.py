#Diego Velasco
#Create a timeline in a text file for MATH4353 timeline project.

f = open("myfile.txt", "w")

f.write("MATH-4353"
        + "\nDiego Velasco"
        + "\n3 May 2022"
        + "\nDr. Edmonds"
        + "\n"
        )

f.write("Please note that one newline on your computer screen is equivalent to one year.\n\n\n")

f.write("\nTIMELINE START\n")
f.write("1650 BCE - Rhind papyrus is written, containing several practical math problems of ancient Egypt.")

#Just a test. To print n lines, use range(1, n+1)
for i in range(1, 50):
    f.write("\n"+str(1650-i))

f.write("\n" +"1600 BCE - Base 60 fractions take off in Mesopotamia. Their influence can still be observed in measurements for angles and time.")

for i in range(1, 1150):
    if (1600-i)%100 == 0:
        f.write("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(1600-i) + " BCE ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        f.write("\n" + str(1600-i))

f.write("\nc. 450 BCE - Hippias of Elis introduces the trisectrix and quadratix, a curve that can be used to square the circle.")

for i in range(1, 150):
    f.write("\n" + str(450-i))

f.write("\n300 BCE - Euclid writes the Elements, containing postulates and proofs in geometry and number theory. The influence and popularity of this book is paralleled by only the Bible. Also around this time, Archimedes proves that 22/7 is an overestimate for pi.")

for i in range(1, 100):
    f.write("\n"+str(300-i))

f.write("\n200 BCE - Apollonius writes his work on conics.")

for i in range(1, 200):
    f.write("\n" + str(200-i))

f.write("~~~~~~~~~~~~~~~COMMON ERA ~~~~~~~~~~~~~~~~")

for i in range(1, 200):
    if i == 1:
        f.write("\n1 CE")
    else:
        f.write("\n" + str(i))

f.write("\n200 CE - Nine Chapters on the Mathematical Art, the most influential text of ancient Chinese mathematics, is complete. It contains 250 problems of a practical nature and even describes an early form of Gaussian elimination on matrices.")

for i in range(201, 250):
    f.write("\n" + str(i))

f.write("\n250 - Diophantus writes Arithmetica, a seminal text in number theory. It later influenced the development of algebra.")

for i in range(251, 500):
    f.write("\n" + str(i))

f.write("\n500 - Aryabhata writes his Siddhanta, an influential trigonometry text. It also describes some arithmetic series problems. Also around this time, the Pythagoreans discover that sqrt2 is irrational.")

for i in range(501, 630):
    f.write("\n" + str(i))

f.write("\nc. 630 - Brahmagupta generalizes Heron's formula to quadrailaterals.")

for i in range(631, 810):
    f.write("\n" + str(i))

f.write("\nc. 810 - Baghdad House of Wisdom is founded, focusing on translating Persian, Sanskrit, and Greek texts.")

for i in range(811, 820):
    f.write("\n" + str(i))

f.write("\n820 - al-Khwarizmi writes the Al-Jabr, describing solutions to equations (especially quadratics).")

for i in range(821, 876):
    f.write("\n" + str(i))

f.write("\n876 - First reference to the number zero in India.")

for i in range(877, 900):
    f.write("\n" + str(i))

f.write("\n900 - ibn-Qurra generalizes the Pythagorean Theorem to all rectangles.")

for i in range(901, 1100):
    f.write("\n" + str(i))

f.write("\n1100 - Khayyam continues on al-Khwarizmi's work, providing solutions to quadratic equations.")

for i in range(1101, 1200):
    f.write("\n" + str(i))

f.write("\nc. 1200 - Hindu-Arabic numerals spread to Europe.")

for i in range(1201, 1202):
    f.write("\n" + str(i))

f.write("\n1202 - Liber Abaci published by Fibonacci, describing the recurrence relation bearing his name.")

for i in range(1203, 1248):
    f.write("\n" + str(i))

f.write("\n1248 - Li Ye publishes Ceyuan Haijing, with 170 problems relating to circles inscribed in right triangles.")

for i in range(1249, 1303):
    f.write("\n" + str(i))

f.write("\n1303 - Earliest appearance of Pascal's triangle in Zhu Shijie's Jade Mirror of the Four Origins. This marks the end of the Golden Age of Chinese mathematics.")

for i in range(1304, 1350):
    f.write("\n" + str(i))

f.write("\n1350 - Richard Suiseth proves 1/2 + 2/4 + 3/8 + ... = 2, marking the beginning of mathematicians' maturity in working with infinite series.")

for i in range(1351, 1551):
    f.write("\n" + str(i))

f.write("\n1551 - Robert Recorde uses the modern equals sign (=) for the first time in The Whetstone of Witte.")

for i in range(1552, 1614):
    f.write("\n" + str(i))

f.write("\n1614 - Napier describes logarithms in Mifici Logarithmorum, forever simplifying calculations of large numbers.")

for i in range(1615, 1637):
    f.write("\n" + str(i))

f.write("\n1637 - Cartesian coordinates are developed, connecting algebra and plane geometry.")

for i in range(1638, 1666):
    f.write("\n" + str(i))

f.write("\n1666 - Newton begins working on calculus, referring to it as the method of fluxions.")

for i in range(1667, 1674):
    f.write("\n" + str(i))

f.write("\n1674 - Leibniz begins independently working on calculus.")

for i in range(1675, 1696):
    f.write("\n" + str(i))

f.write("\n1696 - The Bernoulli brothers solve the brachistochrone problem.")

for i in range(1697, 1719):
    f.write("\n" + str(i))

f.write("\n1719 - Brook Taylor discovers a way to use an infinite series as an approximation for various functions.")

for i in range(1720, 1736):
    f.write("\n" + str(i))

f.write("\n1736 - Seven bridges of Koenigsberg problem is solved by Euler. Initially regarded as a trivial geometry problem, this is now widely regarded as the birth of graph theory.")

for i in range(1737, 1747):
    f.write("\n" + str(i))

f.write("\n1747 - Euler develops his famous identity relating complex numbers, trigonometry, and exponentials: e^ix = cosx + isinx")

for i in range(1748, 1750):
    f.write("\n" + str(i))

f.write("\nc.1750 - The industrial revolution begins. While not a mathematical event, it has undoubtedly marked a new epoch in human history.")

for i in range(1751, 1799):
    f.write("\n" + str(i))

f.write("\n1799 - The Abel-Ruffini theorem is proved, stating that there can not exist general solutions to polynomials of degree five or greater.")

for i in range(1800, 1807):
    f.write("\n" + str(i))

f.write("\n1807 - Fourier presents his findings, providing an early description of Fourier series.")

for i in range(1808, 1847):
    f.write("\n" + str(i))

f.write("\n1847 - Boole defines Boolean algebra in The Mathematical Analysis of Logic.")

for i in range(1848, 1873):
    f.write("\n" + str(i))

f.write("\n1873 - e is proved to be a transcendental number.")

for i in range(1874, 1882):
    f.write("\n" + str(i))

f.write("\n1882 - pi is proved to be a transcendental number.")

for i in range(1883, 1891):
    f.write("\n" + str(i))

f.write("\n1891 - Cantor presents his diagonalization argument, proving the existence of sets are uncountably infinite.")

for i in range(1892, 1900):
    f.write("\n" + str(i))

f.write("\n1900 - Hilbert proposes his 23 questions, inspiring the future Millenium problems.")

for i in range(1901, 1912):
    f.write("\n" + str(i))

f.write("\n1912 - Alfred Whitehead and Bertrand Russell publish Principia Mathematica, a meta-mathematical treatise on set theory and formal logic.")

for i in range(1913, 1931):
    f.write("\n" + str(i))

f.write("\n1931 - Godel's incompleteness theorem is proved, with strong consequences regarding the consistency of mathematics itself.")
f.write("\n1932 - The Fields Medals awards are established by the ICM, to be gifted to outstanding mathematicians under the age of forty.")

for i in range(1933, 1936):
    f.write("\n" + str(i))

f.write("\n1936 - Alan Turing publishes a proof to the Entscheidungsproblem.")

for i in range(1937, 1944):
    f.write("\n" + str(i))

f.write("\n1944 - Von Neumann publishes Theory of Games and Economic Behavior.")

for i in range(1945, 1950):
    f.write("\n" + str(i))

f.write("\n1950 - John Nash publishes several papers on non-cooperative games and equilibrium points.")

for i in range(1951, 1960):
    f.write("\n" + str(i))

f.write("\n1960 - Tony Hoare develops quicksort, still the best general purpose sorting algorithm.")
f.write("\n1961 – Francis and Kublanovskaya independently develop the QR algorithm to calculate the eigenvalues and eigenvectors of a matrix.")

f.write("\n" + str(1962))
f.write("\n1963 – Lorenz develops solutions for a model of turbulence, pioneering chaos theory." )

for i in range(1964, 1975):
    f.write("\n" + str(i))

f.write("\n1975 – Benoît Mandelbrot publishes Les objets fractals, forme, hasard et dimension. ")
f.write("\n1976 - The proof of the four color theorem is the first proof assisted by a computer.")

for i in range(1977, 1983):
    f.write("\n" + str(i))

f.write("\n1983 - By now, almost all finite simple groups have been classified.")

for i in range(1984, 1995):
    f.write("\n" + str(i))

f.write("\n1995 - Sir Andrew Wiles proves Fermat's Last Theorem, closing the book on a 300 year mystery.")

for i in range(1996, 2000):
    f.write("\n" + str(i))

f.write("\n2000 - Seven Millenium prize problems are established by the Clay Institute.")

for i in range(2001, 2006):
    f.write("\n" + str(i))

f.write("\n2006 - Grigori Perelman publishes a proof of Poincare's conjecture, one of the Millenium problems.")

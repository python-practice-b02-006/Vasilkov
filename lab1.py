# import numpy as np
# z=int(input())
# y=np.log((1/(np.e*(np.sin(z)+1)))/(5/4+1/(z**15)))/np.log(z*z+1)
# print(y)

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(-3, 4,0.01 )
# y = x*x-x-6
# plt.figure(figsize=(5, 5))
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')
# plt.plot(x, x/x-1, label="r'r'")
# plt.plot(x, y, label="fe")
# plt.grid(True)
# plt.legend(loc='best', fontsize=12)
# plt.savefig('figure_with_legend.png')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(-3, 4, 0.01)
# y = np.log(((x**2+1))*np.exp(-np.abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x))))
# plt.plot(x, y, label="rg")
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(-5, 5, 0.01)
# with plt.xkcd():
#     plt.plot(x, eval(input()), label="gr")
#     plt.grid(True)
#     plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# x2=[12.86, 14.11, 16.15, 18.12, 20.1]
# y2=[0.028535, 0.029106, 0.031423, 0.035505, 0.044701]
# x = [#12.86, 14.11, 16.15, 18.12, 20.1,
#      22.09, 24.1, 26.1, 28.1, 30.09, 32.09, 34.08, 36.08, 38.07, 40.07]
# y = [#0.028535, 0.029106, 0.031423, 0.035505, 0.044701,
#      0.06776, 0.11007, 0.152282, 0.193714, 0.230229, 0.267955,0.307531, 0.342466, 0.375593, 0.404931]
#
# t=np.arange(5.54507699, 20.1, 0.01)
# plt.scatter(x2, y2, label='qge')
# r, u=np.polyfit(x2, y2, deg=3, cov=True)
# b=np.poly1d(r)
# print(b.r)
# plt.plot(t, r[0]*t**3+r[1]*t**2+r[2]*t**1+r[3], label='r')
# plt.scatter(x, y, label='re')
# p, v = np.polyfit(x, y, deg=1, cov=True)
# c=np.poly1d(p)
# print(c.r)
# print([v])
# z=np.arange(18.10411239, 50, 0.01)
# plt.plot(z, p[0]*z+p[1], label='erg')
# plt.errorbar(x, y, xerr=1, yerr=0.02)
# plt.errorbar(x2, y2, xerr=1, yerr=0.02)
# plt.xlabel(r'$T$', fontsize=14)
# plt.ylabel(r'$1\backslash \chi$', fontsize=14)
# plt.grid(True)
# plt.show()

# import numpy as np
# x = [1, 2, 3, 4, 5, 6]
# y = [1, 1.42, 1.76, 2, 2.24, 2.5]
# p, v = np.polyfit(x, y, deg=1, cov=True)
# print(p, v)
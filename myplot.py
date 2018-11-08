import matplotlib.pyplot as plt

def main(filename=None):
	fig = plt.figure(figsize=(4, 3))
	ax = fig.add_subplot(1,1,1)
	ax.plot([1, 2, 3], [1, 2, -1], color='red')
	ax.set_xlabel(r'$v(t) = \frac{\pi}{2}$')
	ax.set_ylabel('time')
	ax.set_xlim([0, 4])
	ax.set_title(r'$x = 2$')
	if filename is None:
		plt.show()
	else:
		fig.savefig(filename)

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
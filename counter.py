# counter.py - testing luigi
import luigi

class Counter(luigi.Task):
	x = luigi.IntParameter()
	y = luigi.IntParameter(default=4500000)

	def run(self):
		while (self.x < self.y):
			self.x = self.x + 1
			if (self.x % 100 == 0):
				print(self.x)

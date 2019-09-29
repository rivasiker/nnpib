from pyfasta import Fasta
import pyBigWig

f = Fasta('/home/iker/nnPib2019/data/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta', key_fn=lambda key: key.split()[0])
bw = pyBigWig.open("/home/iker/nnPib2019/data/training_data/C01M16.bigwig")


names = []
for i in range(1, 23):
	names.append('chr'+str(i))


for chrom in names:

	print(chrom)

	index = [f[chrom][i] != 'N' for i in range(bw.chroms(chrom))]
	data = bw.values(chrom, 0, bw.chroms(chrom))

	with open('data/'+chrom + '.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(zip(data, index))


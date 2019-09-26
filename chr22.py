from pyfasta import Fasta
import pyBigWig

f = Fasta('/home/iker/nnPib2019/data/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta', key_fn=lambda key: key.split()[0])
bw = pyBigWig.open("/home/iker/nnPib2019/data/training_data/C01M16.bigwig")

index = [f['chr22'][i] != 'N' for i in range(bw.chroms("chr22"))]

data = bw.values("chr22", 0, bw.chroms("chr22"))

with open('chr22.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(data, index))


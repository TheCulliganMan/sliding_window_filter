for I in *vcf; do vcftools --vcf $I --window-pi 100000; done

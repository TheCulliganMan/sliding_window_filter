X=$(pwd)
for I in *; do 
  cd $I;
  vcftools --vcf *vcf --window-pi 100000; 
  cd $X;
done

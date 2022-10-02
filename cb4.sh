echo -n "Masukkan angka : ";
read a;
echo "Angka ganjil kurang dari $a";


while [ $a -gt 0 ]
do
   echo $a
   a=$((a - 2))
done

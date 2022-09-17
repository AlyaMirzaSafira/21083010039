a=8
b=16
let c=2*a
if [ $b -lt $a ]
then 
   echo "b lebih kecil dari a"
elif [ $a == $c ]
then 
   echo "a =  2a"
elif [ $b == $c ]
then
   echo "b = 2a"
else
   echo "Tidak ada kondisi yang memenuhi"
fi

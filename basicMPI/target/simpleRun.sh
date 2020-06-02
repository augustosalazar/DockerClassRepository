#!/bin/bash
start=`date +%s.%N`
for (( core=3; core<=5; core++))
do
    for (( limit=100000; limit<=500000; limit=limit+100000 ))
    do
        echo "Vamos a verificar hasta ${limit} con n = ${core}"
        mpiexec -n $core python3 $1 $limit
    done
done
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo "Total time: $runtime seconds"

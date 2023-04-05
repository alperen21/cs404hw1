


for i in $(seq 1 5); 
    do 
    j=$((i + 1));
    python -m memory_profiler main.py --algorithm ucs --difficulty easy --start $i --end $j | tee ./logs/ucs_easy_$i.log;
    python -m memory_profiler main.py --algorithm ucs --difficulty medium --start $i --end $j | tee ./logs/ucs_medium_$i.log;
    python -m memory_profiler main.py --algorithm ucs --difficulty hard --start $i --end $j | tee ./logs/ucs_hard_$i.log;

done

for i in $(seq 1 5); 
    do 
    j=$((i + 1));
    python -m memory_profiler main.py --algorithm a_star --difficulty easy --start $i --end $j | tee ./logs/a-star_easy_$i.log;
    python -m memory_profiler main.py --algorithm a_star --difficulty medium --start $i --end $j | tee ./logs/a-star_medium_$i.log;
    python -m memory_profiler main.py --algorithm a_star --difficulty hard --start $i --end $j | tee ./logs/a-star_hard_$i.log;


done
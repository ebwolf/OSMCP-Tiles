#!/bin/bash -x
python tilecache_seed.py --bbox=-14000000,2820000,-10500000,4630000 idx 0 10 &
python tilecache_seed.py --bbox=-14000000,4630000,-10500000,6440000 idx 0 10 &
python tilecache_seed.py --bbox=-10500000,2820000, -7000000,4630000 idx 0 10 &
python tilecache_seed.py --bbox=-10500000,4630000, -7000000,6440000 idx 0 10 &

python tilecache_seed.py --bbox=-12500000,4000000,-11250000,5125000 idx 10 18 &
python tilecache_seed.py --bbox=-12500000,5125000,-11250000,6250000 idx 10 18 &
python tilecache_seed.py --bbox=-11250000,4000000,-10000000,5125000 idx 10 18 &
python tilecache_seed.py --bbox=-11250000,5125000,-10000000,6250000 idx 10 18 &


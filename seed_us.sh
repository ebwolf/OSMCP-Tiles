#!/bin/bash -x
python tilecache_seed.py --bbox=-14000000,2820000,-10500000,4630000 drg 0 10 &
python tilecache_seed.py --bbox=-14000000,4630000,-10500000,6440000 drg 0 10 &
python tilecache_seed.py --bbox=-10500000,2820000, -7000000,4630000 drg 0 10 &
python tilecache_seed.py --bbox=-10500000,4630000, -7000000,6440000 drg 0 10 &

python tilecache_seed.py --bbox=-14000000,2820000,-10500000,4630000 bnd 0 10 &
python tilecache_seed.py --bbox=-14000000,4630000,-10500000,6440000 bnd 0 10 &
python tilecache_seed.py --bbox=-10500000,2820000, -7000000,4630000 bnd 0 10 &
python tilecache_seed.py --bbox=-10500000,4630000, -7000000,6440000 bnd 0 10 &

python tilecache_seed.py --bbox=-14000000,2820000,-10500000,4630000 idx 0 10 &
python tilecache_seed.py --bbox=-14000000,4630000,-10500000,6440000 idx 0 10 &
python tilecache_seed.py --bbox=-10500000,2820000, -7000000,4630000 idx 0 10 &
python tilecache_seed.py --bbox=-10500000,4630000, -7000000,6440000 idx 0 10 &

python tilecache_seed.py --bbox=-14000000,2820000,-10500000,4630000 naip 0 10 &
python tilecache_seed.py --bbox=-14000000,4630000,-10500000,6440000 naip 0 10 &
python tilecache_seed.py --bbox=-10500000,2820000, -7000000,4630000 naip 0 10 &
python tilecache_seed.py --bbox=-10500000,4630000, -7000000,6440000 naip 0 10 &

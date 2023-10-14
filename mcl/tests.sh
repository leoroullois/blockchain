#/bin/bash

cd /lib/mcl/bin/
cmake .. -DBUILD_TESTING=ON
make -j4

cd /lib/mcl/
make bin/bn_c384_256_test.exe && bin/bn_c384_256_test.exe
make bin/bls12_test.exe && bin/bls12_test.exe

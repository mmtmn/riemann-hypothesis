# rimann-hypothesis
This repository explores a couple of experiments with prime numbers. It uses a RNN to attempt to predict the riemann hypothesis using scripts written in C.

with 10 examples for the training the data the error was 200.
with 100 the error was very similar.
with 10k, total error jumped to 19.

![image](https://github.com/user-attachments/assets/3c39475d-403a-47f7-9986-e6aabce136a2)

more data can be generated using the training script.

to compile the training data: gcc -o training training.c -lm;./training

make sure to than copy and paste the training data into the rnn script

to run the rnn: gcc -o rnn_riemann rnn_riemann.c -lm;./rnn_riemann



### 8TB_training.c

Warning, compiling and running this script will results in generating and storing one trillion zeros of the Riemann zeta function.
Might be something cool to do if the means to do so :)




in the bin folder you'll find everything that is detailed bellow, which was part of exploring different ideas until landing on the reccurent neural networks in c.

inside the bin folder you'll find all scripts that were used during this saturday morning exploration of the prime numbers and the riemann hypothesis.

everything that is bellow is the documentation on how this repository evolved and the different experiments that were binned but were intereting none of the less.


# spiral.py

A spiral of numbers where non-prime numbers are represented as gray dots and prime numbers as black dots

![image](https://github.com/user-attachments/assets/9a2be51e-7ecc-47f2-a21e-00b0769492f6)

n_points = 1000000

# 3d_spiral.py

A 3 dimnesional spiral of numbers where non-prime numbers are represented as gray dots and prime numbers as black dots

![image](https://github.com/user-attachments/assets/52ef5316-e93f-402e-9dfd-7a43b72ab07b)

n_points = 1000


![image](https://github.com/user-attachments/assets/f5fae944-6ed3-4eab-890f-2b90699e6117)

n_points = 10000


![image](https://github.com/user-attachments/assets/ebf9a691-ec32-41e0-a595-0a392590e2c4)

n_points = 100000

![image](https://github.com/user-attachments/assets/412de059-209f-48c0-977c-96ef05894316)

n_points = 100000

# dual_3d_spirals.py

A 3 dimnesional dual spiral of alternating numbers where non-prime numbers are represented as gray dots and prime numbers as black dots

![image](https://github.com/user-attachments/assets/e80d3084-f0bc-407a-aeaa-45ba7f7256a9)

n_points = 1000

![image](https://github.com/user-attachments/assets/224ecfaf-7809-489f-a534-381cc388fff5)

n_points = 10000

![image](https://github.com/user-attachments/assets/017de729-1389-4cae-9938-854a3fa09c8f)

n_points = 10000

![image](https://github.com/user-attachments/assets/c99f0b08-e4e6-417e-8f55-94ca5994ccb1)

n_points = 100000


view from the bottom of the 10k dual spiral:

![image](https://github.com/user-attachments/assets/d93dee5b-e74d-4ba4-baa8-0be0576b61ca)



# quadra_3d_spirals.py

A 3 dimnesional quadra spiral of alternating numbers where non-prime numbers are represented as gray dots and prime numbers as black dots

![image](https://github.com/user-attachments/assets/c121062f-03d9-422e-bf71-d6393d0aa448)

n_points = 1000

![image](https://github.com/user-attachments/assets/3b6f7503-3c6e-40ad-b1f6-a1fa9760133f)

n_points = 10000

![image](https://github.com/user-attachments/assets/7858a54f-b6f0-49ad-bd98-422015e99f71)

n_points = 100000

![image](https://github.com/user-attachments/assets/1a65596e-6475-4e9d-95d1-07d6bec1c62b)

n_points = 100000


# outwards_quadra_3d_spirals.py

A 3 dimnesional outwards quadra spiral of alternating numbers where non-prime numbers are represented as gray dots and prime numbers as black dots

![image](https://github.com/user-attachments/assets/cdfc6646-b459-43a9-a2a1-7884dedb7a44)

n_points = 1000

![image](https://github.com/user-attachments/assets/0c9f8a37-079e-4888-8263-fd16580546b0)

n_points = 10000

![image](https://github.com/user-attachments/assets/a41b1029-bc21-4a3b-84cd-e7c0e0a92901)

n_points = 100000

![image](https://github.com/user-attachments/assets/8bc9a2f3-f7fc-4316-a43d-fcd359f18dae)

n_points = 100000


if you increase the outwards variable (z_step):

![image](https://github.com/user-attachments/assets/fe8a9e0a-ee98-48f5-be22-0a9fffbef010)
![image](https://github.com/user-attachments/assets/19794021-c766-4dd2-a910-cfb15598eca2)
![image](https://github.com/user-attachments/assets/96ee9ad6-70fe-4574-9c43-11d6a9112f34)
![image](https://github.com/user-attachments/assets/367972ed-8c2a-4940-883d-88baf526a500)


# octa_3d_spirals.py

![image](https://github.com/user-attachments/assets/af0adfb1-f9de-4cd0-8e90-951a1f9043db)
![image](https://github.com/user-attachments/assets/cea1fe5c-9aa9-4d95-a5d2-c5e626a40c1f)

# sexdeca_3d_spirals.py (bugged)

![image](https://github.com/user-attachments/assets/fa4c1dc1-65b5-4281-af0f-67df3e0389c1)


# buckets.py
This script outputs the prime and non-prime counts for each bucket in the specified format, iterating from 1 bucket to 16 buckets.

# buckets_checker.py

This code stops as soon as it finds a bucket that contains all primes and no non-primes. If no such bucket is found in any configuration from 1 to 16 buckets, it will print a message stating so.


numbers: 1000

Found a bucket with all primes in 150 bucket experiment. Bucket7 has all the primes.


numbers: 10000

Found a bucket with all primes in 1470 bucket experiment. Bucket1279 has all the primes.



# single_buckets_checker.py

This code stops as soon as it finds an amount of buckets where only one bucket contains all the prime numbers and no other buckets have any prime numbers.

### No experiment found where only one bucket contains all primes and no non-primes.


# prime_buckets.c

This code stops as soon as it finds an amount of buckets where only one bucket contains all the prime numbers and no other buckets have any prime numbers.

### No experiment found where only one bucket contains all primes and no non-primes.


# riemann.py
This script combines high-precision numerical exploration, machine learning prediction, and visualization for the Riemann Hypothesis.

### Zeros on the critical line between 0 and 100: []
### Predicted next zero: 49.10204728571429

![image](https://github.com/user-attachments/assets/2ed90841-31e2-4218-bd49-12c37f481c3d)
![image](https://github.com/user-attachments/assets/63d79050-3b88-44de-a32a-da5682ada33c)

# riemann_buckets.py
This script visualizes and tests the alternating buckets and spirals approach numerically, which might offer some insights.

![image](https://github.com/user-attachments/assets/c42f517e-f399-4cef-bcc5-60480a2ea0b9)

![image](https://github.com/user-attachments/assets/b98876e6-d464-4e8e-bcf2-e4932a3f11a9)

results: No zeros detected in any bucket

# riemann2.py
This script combines high-precision numerical exploration, machine learning prediction, and visualization for the Riemann Hypothesis. Focusing on increasing the learning on it.

results: takes too long to train

# rnn_riemann.c

![image](https://github.com/user-attachments/assets/2473ecea-4204-4c29-81e8-3b861bf4836d)

results: not enough training data

# training.py

a script that generates the data for the rnn_riemann.c file

# rnn_rieman.c (1k zeros)

![image](https://github.com/user-attachments/assets/bf62d06c-4457-4abb-858b-b49b9ccbd7b1)

### results: improvment in trianing, but needs more training data, moving to a c file for training data

# training.c

a script that generates more data and faster data compared to training.py

# rnn_rieman.c (10k zeros)

much better perfomance, but much slower training

![image](https://github.com/user-attachments/assets/2903fc91-85a2-4148-a22f-45fb16f69f62)

![image](https://github.com/user-attachments/assets/a298fbe2-7e0b-412c-a6bd-85927aa46a5e)

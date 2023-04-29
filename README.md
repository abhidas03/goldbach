# goldbach

This program is part of my final project for Discrete Math (MATH 39) at Swarthmore College.
It is a "proof" of the Goldbach conjecture up to a limit of one billion.
>Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory and all of mathematics. It states that every even natural number greater than 2 is the sum of two prime numbers.

It utilizes the Sieve of Atkin to calculate the primes up to a billion, storing them 
in a dictionary. Then, for each even number up to a billion, it iterates through the dictionary of primes and
checks if the number's complement of each prime is in the dictionary. If so, then we know there are 
two primes which add up to the number.
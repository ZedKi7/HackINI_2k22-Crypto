As we can see from the source code, p and q are consecutive primes, as the function next_prime was used on p to find q. Since the values of p and q are pretty close together, we can thus use the Fermat’s Theorem to factorise out p and q

.

The Math

The fermat algorithm uses the fact that:


n=pq=(q−p2)2−(p+q2)2=x2−y2

where:
x=q−p2,y=p+q2

The algorithm works like this:

    a=n−−√

b=a2−n
While b is not a perfect square: increment a
Return p=a−b√
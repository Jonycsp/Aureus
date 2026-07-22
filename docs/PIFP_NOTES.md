# Prime-Indexed Fibonacci Primes (PIFPs)

## Introduction

Aureus is dedicated to the search and study of a particular subset of the
Fibonacci sequence.

Let:

- \(n\) denote a positive integer,
- \(p_n\) denote the \(n\)-th prime number,
- \(F_k\) denote the \(k\)-th Fibonacci number.

Since \(p_n\) is prime by definition, Aureus searches for those primes whose
position in the ordered sequence of primes is itself prime, and whose indexed
Fibonacci number is also prime.

Formally, Aureus searches the set

\[
\mathcal{A}
=
\left\{
p_n
\;\middle|\;
n\in\mathbb{P},
\;
F_{p_n}\in\mathbb{P}
\right\},
\]

where \(\mathbb{P}\) denotes the set of prime numbers.

In other words, Aureus searches for primes \(p_n\) satisfying:

- \(n\) is prime;
- \(F_{p_n}\) is prime.

### Terminology

Throughout the Aureus documentation, the term **Prime-Indexed Fibonacci Prime (PIFP)** refers to elements of the search set

\[
\mathcal{A}
=
\left\{
p_n
\;\middle|\;
n\in\mathbb{P},
\;
F_{p_n}\in\mathbb{P}
\right\}.
\]

This is the precise criterion implemented by the Aureus search engine. It is introduced here to provide a clear and consistent terminology throughout the project's documentation.

---

## Example

| \(n\) | \(p_n\) | \(F_{p_n}\) | Included? |
|------:|--------:|------------:|:---------:|
| 2 | 3 | 2 | ✓ |
| 3 | 5 | 5 | ✓ |
| 4 | 7 | 13 | ✗ (4 is not prime) |
| 5 | 11 | 89 | ✓ |
| 6 | 13 | 233 | ✗ (6 is not prime) |

---

## Why are these numbers interesting?

*(We'll expand this section later.)*

Possible topics include:

- Their rarity.
- Their relationship to Fibonacci primes.
- Their relationship to the sequence of prime numbers.
- Known computational results.
- Open questions.

---

## Notation

Throughout the Aureus documentation,

- \(F_n\) denotes the \(n\)-th Fibonacci number.
- \(p_n\) denotes the \(n\)-th prime.
- \(\mathbb{P}\) denotes the set of prime numbers.
- \(\mathcal{A}\) denotes the search set defined above.

---

*Ad astra per veritatem.*
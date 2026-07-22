# Aureus

*Ad astra per veritatem.*

**Aureus** is an open-source Python project dedicated to the search, discovery, and study of **Prime-Indexed Fibonacci Primes (PIFPs)**.

A PIFP is a prime (p_n) whose position (n) in the ordered sequence of prime numbers is itself prime, and whose corresponding Fibonacci number (F_{p_n}) is also prime. Because these numbers are extraordinarily rare, searching for them requires efficient algorithms, reliable long-running execution, and persistent progress tracking.

Aureus provides a modular command-line environment for conducting these searches while recording discoveries, preserving progress, and collecting runtime data for future analysis.

For the formal mathematical definition and notation, see **docs/PIFP_NOTES.md**.


---

## Features

- 🔍 Search for Prime-Indexed Fibonacci Primes (PIFPs)
- 📊 Live search dashboard
- 💾 Autosave and resumable searches
- 🗂️ Multiple named save slots
- 📈 Runtime history
- 📉 Performance telemetry
- 📚 Discovery logging
- ⚙️ Custom search ranges
- 🧩 Modular architecture

---

## Installation

### Requirements

- Python 3.13 or newer
- SymPy

Install SymPy with:

```bash
pip install sympy
```

Clone the repository:

```bash
git clone https://github.com/USERNAME/Aureus.git
cd Aureus
```

Run the application:

```bash
python src/Aureus.py
```

---

## Project Structure

```text
Aureus/
├── src/
├── data/
│   └── saves/
├── docs/
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Version History

| Version | Codename | Status |
|---------:|----------|--------|
| v0.1 | Genesis | Released |
| v0.2 | Analysis | Released |
| v0.3 | Horizon | Released |
| v0.4 | Momentum | Released |
| v0.5 | Atlas | Released |
| v0.6 | Voyager | Released |
| v0.7 | Insight | Released |
| v0.8 | Foundation | Released |
| v0.9 | Phoenix | Current |
| v1.0 | Aureus | Planned |

---

## Contributing

This project is currently developed as a personal research project. Suggestions, ideas, and discussions are always welcome.

---

## License

Licensed under the MIT License.

---

## Acknowledgements

Created by Jony_CSP.

Developed with assistance from ChatGPT.

---

> *Ad astra per veritatem.*
>
> **"To the stars through truth."**
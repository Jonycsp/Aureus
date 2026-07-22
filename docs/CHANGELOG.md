# CHANGELOG

All notable changes to Aureus are documented in this file.

Version codenames are used during development releases up to v0.9. Beginning with v1.0, Aureus enters its first stable release series.

## v0.1 — Genesis

### Added

* Initial Prime-Indexed Fibonacci Prime (PIFP) search engine.
* Prime-indexed prime generation.
* Fibonacci primality verification.
* Basic discovery reporting.

---

## v0.2 — Analysis

### Added

* Runtime measurement.
* Gap analysis between consecutive PIFPs.
* Ratio analysis.
* Relative gap calculations.

### Changed

* Changed final output formatting.

---

## v0.3 — Horizon

### Added

* Live progress updates.
* Elapsed time display.
* ETA estimation.
* Automatic dashboard refresh.

### Changed

* More informative terminal output.

### Fixed

* Initial ETA calculation.
* Progress refresh stability.

---

## v0.4 — Momentum

### Added

* Checkpoint system.
* Seconds-per-iteration tracking.
* Rolling performance average.

### Changed

* ETA based on measured execution speed.
* Improved progress estimation.

### Fixed

* Division-by-zero edge cases.
* Progress completion accuracy.
* Dashboard update duplication.

---

## v0.5 — Atlas

### Added

* Full-screen dashboard.
* Progress bar.
* Success counter.
* Largest discovery display.
* Live discovery list.
* Runtime history.
* Automatic runtime recording.

### Changed

* Cleaner dashboard layout.
* Improved readability.

### Fixed

* Dashboard refresh behaviour.
* Duplicate rendering.
* Various display issues.

---

## v0.6 — Voyager

### Added

* User-selectable workloads.
* Custom search ranges.
* Workload-aware runtime history.
* Global and local index tracking.

### Changed

* Improved workload estimation.
* Greater search flexibility.

### Fixed

* Incorrect indexing in ranged searches.
* Runtime history separation.
* Workload calculation issues.

---

## v0.7 — Insight

### Added

* Telemetry logging.
* Performance sampling.
* Seconds-per-iteration history.
* Framework for future runtime prediction.

### Changed

* Improved internal performance monitoring.

### Fixed

* CSV parsing edge cases.
* Empty-row handling.
* Telemetry reliability improvements.

---

## v0.8 — Foundation

### Added

* utils.py
* dashboard.py
* history.py
* Reusable helper functions.
* Modular runtime history management.

### Changed

* Refactured project architecture.
* Improved maintainability.
* Better separation of responsibilities.

### Fixed

* Import issues.
* Runtime history loading.
* General code organization.

---

## v0.9 — Phoenix

> **Phoenix** marks the transition of Aureus from an experimental prototype into a resilient, modular research application. This release introduces persistent save management, resumable searches, comprehensive project documentation, and a redesigned terminal interface, all built upon a significantly improved architecture. Following an extensive quality assurance and stress-testing phase, Phoenix establishes the foundation for the upcoming stable **v1.0** release.

### Release Summary

- Largest release to date.
- Introduces persistent save management and resumable searches.
- Completes the transition to a fully modular architecture.
- Adds comprehensive documentation and GitHub preparation.
- Final development release before the stable v1.0 series.

### Added

* Interactive main menu.
* Search menu with preset and custom search modes.
* Statistics menu.
* Dedicated pages for Runtime History, Discoveries, and Telemetry.
* Persistent save system with manual save slots and autosave recovery.
* Back and Quit navigation throughout the interface.
* Search interruption handling with automatic session recovery.
* Utility functions for terminal navigation and formatting.
* Multi-slot save system architecture.
* Dedicated save manager module.
* Save slot browser interface.
* Save slot overwrite confirmation.
* Save slot metadata (progress, elapsed time, discoveries).
* About page.
* Startup splash screen.
* ASCII application branding.
* Version and codename system.
* Project documentation.
* Save slot sorting (date, name, progress, etc.)
* Save slot renaming.
* Save slot deletion.
* Save slot creation timestamps.
* Save slot modification timestamps.
* Save slot progress display.
* Autosave recovery prompt at startup.
* Goodbye screen.

### Changed

* Moved the search engine into search.py.
* Redesigned the dashboard.
* Reorganized the project into dedicated modules.
* Improved terminal interface consistency.
* Improved resume workflow.
* Improved interruption workflow.
* Improved runtime history presentation.
* Improved overall menu architecture.
* Reorganized the project into a structured directory layout (src/, data/, docs/)
* Unified project branding across the application.
* Centralized version management.
* Improved save workflow.
* Simplified application startup.
* Refactored menu system into a dedicated module.
* Refactored save management into dedicated components.
* Improved terminal navigation consistency.
* Improved progress reporting during resumed searches.
* Improved save slot browsing interface.
* Improved project documentation.
* Improved repository organization.
* Significantly improved overall application stability through comprehensive testing and bug fixing.

### Fixed
* Resume state restoration.
* Runtime history loading.
* Dashboard formatting inconsistencies.
* Progress calculation edge cases.
* Navigation bugs.
* Session persistence issues.
* Multiple UI and stability issues.
* Save slot completion cleanup.
* Autosave cleanup after successful searches.
* Progress calculation after resumed searches.
* Resume index synchronization.
* Save slot overwrite behavior.
* Autosave path handling.
* Interrupt handling stability.
* Keyboard interrupt edge cases.
* Temporary file handling.
* Windows file replacement issues.
* Multiple save/resume edge cases.

### Developer

* Introduced persistent CSV-based storage.
* Simplified menu control flow.
* Expanded reusable utility functions.
* Reduced coupling between project modules.
* Prepared the architecture for save slots, confidence-based ETA, and future GUI support.
* Introduced project-wide constants for versioning.
* Separated branding into dedicated modules.
* Introduced comprehensive stress testing before release.
* Standardized project directory layout.
* Prepared repository for Git version control.
* Expanded documentation.
* Improved code readability and maintainability.

---

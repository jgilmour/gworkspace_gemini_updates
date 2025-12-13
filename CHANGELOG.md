# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-13

### Added
- Type hints throughout codebase for better IDE support and type checking
  - Added typing imports: `List`, `Dict`, `Any`, `Optional`
  - Added type annotations to `fetch_workspace_updates()` and `main()` functions
- Input validation for `--days` parameter (must be between 1-365)
  - Raises `ValueError` with clear message for invalid inputs
  - Updated help text to show valid range
- Network timeout (10 seconds) on HTTP requests
  - Prevents script from hanging on network issues
  - Improves reliability and security
- Comprehensive test suite (`test_script.py`)
  - Verifies date filtering logic
  - Tests XML parsing and category filtering
  - Validates 30-day lookback functionality

### Changed
- Updated README to specify minimum Python version (3.7+)
  - Required for `datetime.fromisoformat()` support
- Improved `--days` argument help text to show valid range (1-365)

### Fixed
- Potential hanging on network failures (now times out after 10 seconds)
- Script could accept invalid day values (negative, zero, or excessively large)

## [1.0.0] - 2025-12-13

### Added
- Initial release
- Fetch Google Workspace updates from Feedburner RSS feed
- Filter updates by "Gemini" category
- Configurable time range (default: 7 days)
- Display post details: title, link, publication date, categories
- Feed statistics: total entries, recent entries, Gemini-related entries
- Command-line interface with argparse
- Error handling for network and XML parsing errors
- MIT License

### Features
- Parses Atom feed format with proper namespace handling
- UTC timezone support for accurate date filtering
- Reverse chronological sorting of results
- Clear error messages for common failure scenarios

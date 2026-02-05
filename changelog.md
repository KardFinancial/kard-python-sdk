## 2.2.0 - 2026-02-05
* feat: add support for core transaction type with new models and attributes
* This update introduces support for core banking system transactions through a new `coreTransaction` type, expanding the API's capabilities to handle transactions with limited card-level data from core banking systems.
* Key changes:
* Added `CoreTransaction`, `CoreMerchant`, `CoreTransactionAttributes`, and `FinancialInstitution` models
* Extended transaction discriminated union to include `Transactions_CoreTransaction`
* Updated API documentation to include `coreTransaction` as third supported transaction type
* Enhanced transaction creation endpoints to support core banking system data flow
* Updated datetime format descriptions to use ISO 8601 standard terminology
* Refined API documentation for location-based endpoints
* 🌿 Generated with Fern

## 2.1.0 - 2026-02-04
* feat: add UI component support for rewards API
* Add support for customizable UI components in rewards offers and locations to enable
* flexible frontend rendering. This enhancement allows clients to specify which UI
* components they need in the response, reducing payload size and improving performance
* for different UI contexts.
* Key changes:
* Add `supported_components` parameter to offers() and locations() methods
* Introduce ComponentType enum with values: shortDescription, longDescription, cta, tags, detailTags
* Add OfferComponents data structure with optional UI component fields
* Add CtaComponent with button text and style configuration
* Add ButtonStyle enum for button styling options
* Update method signatures and documentation for both sync and async clients
* 🌿 Generated with Fern

## 2.0.0 - 2026-01-29
* refactor: rename webview to WebView for consistency
* Standardize the naming convention by changing "webview" to "WebView" throughout
* the codebase to follow proper camelCase naming for improved readability and
* consistency with common naming patterns.
* Key changes:
* Rename WebviewTokenResponse to WebViewTokenResponse class
* Update get_webview_token method to get_web_view_token
* Rename webview_token_response.py to web_view_token_response.py
* Update all import statements and references to use new naming
* Update documentation and examples to reflect new names
* 🌿 Generated with Fern

## 1.0.1 - 2026-01-29
* docs: update section heading from "Webview Authentication" to "Webview"
* Simplified the section heading in the API documentation to make it more concise
* and better reflect the content scope. This change improves the documentation
* structure and readability.
* Key changes:
* Shortened section heading from "Webview Authentication" to "Webview"
* Maintains all existing functionality and API references
* Improves documentation clarity and navigation
* 🌿 Generated with Fern

## 1.0.0 - 2026-01-29
* Initial release of the Python SDK.
* Provides core client functionality, authentication support, and documented usage examples to help you get started quickly.

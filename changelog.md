## 2.2.0 - 2026-02-05
* feat: add core transaction support for core banking systems
* Add new coreTransaction type alongside existing transaction and matchedTransaction types to support transactions from core banking systems with limited card-level data. This enhancement provides a more streamlined transaction processing path for financial institutions using core banking systems.
* Key changes:
* Add CoreTransactionAttributes with required fields: transaction_id, amount, currency, description, direction, settled_date, authorization_date, financial_institution, and merchant
* Add CoreMerchant type with addr_zipcode field for simplified merchant data
* Add FinancialInstitution type with rssd_id and name for bank identification
* Add Transactions_CoreTransaction discriminated union variant
* Update transaction creation endpoints to support coreTransaction type
* Update API documentation to describe all three transaction types
* Fix ISO format references to specify ISO 8601 standard
* Remove includeLocal parameter references from rewards documentation
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

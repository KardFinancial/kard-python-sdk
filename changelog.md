## 2.1.0 - 2026-02-04
* feat: add supported_components parameter to rewards endpoints
* Adds a new optional supported_components parameter to both offers() and locations() methods in the rewards client. This parameter allows callers to specify which UI component types to include in API responses, enabling more granular control over returned data.
* The parameter accepts ComponentType enum values including shortDescription, longDescription, cta, tags, and detailTags. When provided, the API returns structured component data through new OfferComponents, CtaComponent, and ButtonStyle types.
* Key changes:
* Add supported_components parameter to offers() and locations() endpoints
* Create new ComponentType enum with UI component type options
* Add OfferComponents model with optional UI component fields
* Add CtaComponent model for call-to-action button data
* Add ButtonStyle enum for button styling options
* Update method signatures in sync/async client and raw client classes
* Add comprehensive parameter documentation and type hints
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

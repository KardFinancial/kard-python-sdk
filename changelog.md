## 3.3.1 - 2026-02-26
* chore: update CLI version to 3.90.4
* Update the Fern CLI version used for code generation from 3.88.1 to 3.90.4 to incorporate the latest improvements and bug fixes in the development toolchain.
* Key changes:
* Update cliVersion from 3.88.1 to 3.90.4 in metadata configuration
* Maintain compatibility with existing generator versions
* Ensure access to latest CLI features and stability improvements
* 🌿 Generated with Fern

## 3.3.0 - 2026-02-25
* feat: add boost method for offer attribution tracking
* Add new boost method to the attributions client to track when users boost offers. This creates an attribution event with eventCode=BOOST and medium=CTA, complementing the existing activate functionality.
* Key changes:
* Add boost() method to both sync and async AttributionsClient classes
* Implement boost endpoint in RawAttributionsClient with proper error handling
* Create BoostOfferResponse types and include options for response serialization
* Extend EventCode enum to support "BOOST" event type
* Update all module exports to include new boost-related types
* 🌿 Generated with Fern

## 3.2.1 - 2026-02-25
* chore: update dependencies and CLI version
* Update Fern CLI from version 3.76.0 to 3.88.1 and refresh dependency lock file to include latest package versions. This maintenance update ensures the SDK generation tooling is current with the latest improvements and security patches.
* Key changes:
* Update Fern CLI version from 3.76.0 to 3.88.1 in metadata
* Refresh certifi package from 2026.1.4 to 2026.2.25 in lock file
* Maintain compatibility with existing generator version 4.45.3
* 🌿 Generated with Fern

## 3.2.0 - 2026-02-23
* feat: add baseReward component to offer components
* Add a new baseReward component to the OfferComponents model to support displaying formatted reward information in offers. This component provides a string field for presenting reward details to users.
* Key changes:
* Add "baseReward" to ComponentType literal union
* Add base_reward field to OfferComponents model with string type
* Include proper field metadata and documentation for the new component
* 🌿 Generated with Fern

## 3.1.3 - 2026-02-20
* chore: downgrade CLI version in metadata
* Updates the Fern CLI version from 3.79.2 to 3.76.0 in the metadata configuration file. This version change may be related to compatibility requirements or rollback to a more stable version.
* Key changes:
* Downgrade cliVersion from 3.79.2 to 3.76.0 in .fern/metadata.json
* Generator name and version remain unchanged
* 🌿 Generated with Fern

## 3.1.2 - 2026-02-18
* chore: update Fern CLI version to 3.79.2
* This change updates the Fern CLI version from 3.29.0 to 3.79.2 in the metadata configuration. This is a maintenance update to use a newer version of the Fern tooling for SDK generation.
* Key changes:
* Update cliVersion from 3.29.0 to 3.79.2 in .fern/metadata.json
* Maintain existing generator name and version configurations
* Ensures compatibility with latest Fern CLI features and improvements
* 🌿 Generated with Fern

## 3.1.1 - 2026-02-17
* refactor: remove custom function examples and skill documentation
* Clean up repository by removing example custom function implementations and associated skill documentation that were no longer needed.
* Key changes:
* Remove .agents/skills/add-custom-function.md skill documentation file
* Remove .claude/skills/add-custom-function.md symlink
* Remove tests/custom/test_hem.py example test file
* Remove tests/custom/test_vectors.json example test vectors
* Clean up .gitignore to remove .claude directory exclusions
* 🌿 Generated with Fern

## 3.0.0 - 2026-02-17
* refactor: simplify transaction attributes by flattening nested structures
* Replace complex nested objects with simplified string fields in transaction attributes to improve API usability and reduce complexity.
* Key changes:
* Remove CoreMerchant and FinancialInstitution complex types
* Replace financial_institution object with financial_institution_name string field
* Remove merchant object dependency from CoreTransactionAttributes
* Update all imports and exports across modules to remove deleted types
* Simplify example usage in documentation
* 🌿 Generated with Fern

## 2.3.0 - 2026-02-06
* feat: add CtaAction type for enhanced CTA button functionality
* Introduce a new CtaAction class to provide action configuration capabilities
* for CTA buttons. This enhancement allows buttons to specify both URL endpoints
* and HTTP methods when clicked, enabling more sophisticated interaction patterns
* within the rewards system.
* Key changes:
* Add new CtaAction type with url and method fields for button configuration
* Update CtaComponent to include optional action field for enhanced functionality
* Register CtaAction in all necessary import hierarchies (users, rewards, types modules)
* 🌿 Generated with Fern

## 2.2.2 - 2026-02-06
* fix: correct API endpoint path for offer activation
* Fixed the URL path structure for activating offers by removing the redundant
* /attributions/ segment from the endpoint. This corrects the API route to properly
* target the offers resource directly under users.
* Key changes:
* Update sync client endpoint from /users/{user_id}/attributions/offers/{offer_id}/activate to /users/{user_id}/offers/{offer_id}/activate
* Update async client endpoint with same path correction
* Align endpoint structure with expected API routing pattern
* 🌿 Generated with Fern

## 2.2.1 - 2026-02-05
* fix: correct API endpoint path for offer activation
* Fixed the URL path for activating offers to include the missing 'attributions' segment in both synchronous and asynchronous client methods. This ensures requests are sent to the correct endpoint structure.
* Key changes:
* Update synchronous client offer activation endpoint from 'users/{user_id}/offers/{offer_id}/activate' to 'users/{user_id}/attributions/offers/{offer_id}/activate'
* Update asynchronous client offer activation endpoint to match the corrected path structure
* Maintain consistency between sync and async API client implementations
* 🌿 Generated with Fern

## 2.2.0 - 2026-02-05
* feat: add core transaction support and user offer activation endpoint
* Expand transaction processing capabilities by introducing support for core banking transactions with limited card-level data. Add new user offer activation endpoint to enable tracking of user interactions with offers via CTA medium.
* Key changes:
* Add coreTransaction type for core banking systems with limited card data
* Create CoreTransactionAttributes, CoreMerchant, and FinancialInstitution types
* Add users.attributions.activate endpoint for offer activation tracking
* Update documentation to clarify location endpoint functionality
* Standardize timestamp format descriptions to ISO 8601 across transaction types
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

## 8.2.0 - 2026-04-14
* ### Breaking Changes
* **Minimum Python version** — raised from 3.8 to 3.10; projects on Python 3.8 or 3.9 must upgrade before updating this SDK.
* ### Added
* **`KardApi` / `AsyncKardApi`** — new optional constructor parameters `logging` (`LogConfig | Logger`) and `headers` (`Dict[str, str]`) for structured request/response logging and per-client custom HTTP headers.
* **`ParsingError`** — new exception (available at `kard.core.parse_error.ParsingError`, re-exported from `kard.core`) raised when a response cannot be deserialized into the expected schema; exposes `headers`, `status_code`, `body`, and `cause` attributes.
* **Logging framework** — `ILogger`, `ConsoleLogger`, `LogConfig`, `LogLevel`, `Logger`, and `create_logger` are now available from `kard.core` for configuring structured logging with automatic redaction of sensitive headers.
* **`BaseHttpResponse.status_code`** — new property for inspecting the HTTP status code without accessing the underlying httpx object.
* **`DefaultAioHttpClient` / `DefaultAsyncHttpxClient`** — pre-configured async HTTP client classes now exported from the top-level `kard` package; `DefaultAioHttpClient` requires the optional `aiohttp` extra.
* **`aiohttp` transport extra** — install with `pip install kard-financial-sdk[aiohttp]` to use an aiohttp-backed httpx transport.
* **`Rfc2822DateTime` / `parse_rfc2822_datetime`** — new type and helper in `kard.core.datetime_utils` for deserializing RFC 2822 (email/HTTP header) date strings.
* ### Changed
* **Retry behavior** — the HTTP client now retries on connection-level errors (`ConnectError`, `RemoteProtocolError`) in addition to retryable HTTP status codes, using exponential backoff driven by a central `base_max_retries` setting (default: 2).
* ### Fixed
* **Base-URL path prefix preservation** — URL construction now uses string joining instead of `urllib.parse.urljoin`, correctly preserving path prefixes (e.g., `https://host/org/tenant/api`) when appending request paths.
* **Empty query parameter injection** — `HttpClient` and `AsyncHttpClient` no longer forward an empty `params` list or dict to httpx, preventing inadvertent stripping of query parameters already embedded in a URL.
* **`ParsingError` on deserialization failure** — Pydantic `ValidationError` raised during response parsing in the uploads and auth clients is now caught and re-raised as a structured `ParsingError` instead of bubbling up unhandled.

## 8.1.0 - 2026-04-10
* The `get_earned_rewards` method on `TransactionsClient` and `AsyncTransactionsClient` now accepts an optional `include` parameter. Pass a comma-separated string of related resources (supported values: `"merchant"` and `"offer"`) to embed those resources directly in the response. Existing code that omits `include` continues to work without changes.

## 8.0.0 - 2026-04-10
* `CardNetwork` has been moved from `kard.transactions` / `kard.transactions.types` to `kard.commons` / `kard.commons.types`. The top-level import `from kard import CardNetwork` continues to work without changes. If your code imports `CardNetwork` directly from `kard.transactions` or `kard.transactions.types`, update those imports to use `kard.commons` or `kard.commons.types` instead.

## 7.2.0 - 2026-04-07
* The SDK now exposes two new types, `AttributionFilter` and `AttributionState` (available at `kard.AttributionFilter` and `kard.AttributionState`), that represent placement context for attribution events. An optional `state` field of type `AttributionState` has been added to both `NotificationAttributionAttributes` and `OfferAttributionAttributes`, providing access to the offer's rank and the active filters at the time the user viewed it. Existing code is unaffected as the new field defaults to `None`.

## 7.1.0 - 2026-04-07
* The SDK now exposes a new `FileUploadType` type (available at `kard.FileUploadType`) that supports both `"incomingTransactionsFile"` and `"historicalTransactionsFile"` values. The `type` field on `CreateFileUploadData` and `FileUploadUrlData` has been widened from a hard-coded literal to this new union type, allowing consumers to create file upload URLs for historical transaction files in addition to incoming transaction files. Existing code that omits or hard-codes `type="incomingTransactionsFile"` continues to work without changes.

## 7.0.0 - 2026-04-06
* Several notification-related types have been removed from the SDK as they are no longer part of the API. The following public symbols are no longer available and must be removed from your code: `BrokerAmount`, `BrokerAmountType`, `BrokerAsset`, `BrokerAssetType`, `BrokerOperationHours`, `BrokerOperationPeriod`, `BrokerPurchaseChannel`, `BrokerReward`, `BrokerRewardType`, `LocationAddress`, `LocationCoordinates`, `LocationStatus`, `MerchantSource`, `OfferStatus`, `OfferType`, `TimePeriod`, `UserOfferStatus`, `NotificationDataUnion_Offer`, `NotificationDataUnion_Merchant`, `NotificationDataUnion_Location`, `NotificationDataUnion_UserOffer`, and all associated `WebhookOffer*`, `WebhookMerchant*`, `WebhookLocations*`, and `WebhookUserOffer*` types. The `"offer"`, `"merchant"`, `"location"`, and `"userOffer"` variants have also been removed from the `NotificationType` union and `NotificationDataUnion` discriminated union.
* Several public webhook notification types have been removed from the `kard.notifications.types` module: `OfferType`, `TimePeriod`, `UserOfferStatus`, `WebhookLocationsAttributes`, `WebhookLocationsData`, `WebhookLocationsRelationships`, `WebhookMerchantAttributes`, `WebhookMerchantData`, `WebhookMerchantRelationships`, `WebhookOfferAttributes`, `WebhookOfferData`, `WebhookOfferRelationships`, `WebhookUserOfferAttributes`, `WebhookUserOfferData`, and `WebhookUserOfferRelationships`. Any code that imports or references these classes will break and must be updated accordingly.

## 6.2.0 - 2026-04-03
* The deprecated `financial_institution_name` field in `CoreTransactionAttributes` is now optional (defaults to `None`), reflecting its deprecated status in favor of `financial_institution_id`. Existing code that reads this field continues to work without changes.

## 6.1.0 - 2026-04-02
* The SDK now exposes a unique identifier for the financial institution on transaction data. The new optional `financial_institution_id` field is available in `CoreTransactionAttributes` to replace the deprecated `financial_institution` name field. Existing code using `financial_institution` continues to work without changes.

## 6.0.0 - 2026-03-30
* The `card_last_four` field in `CoreTransactionAttributes` has been replaced with `card_last_fours` (now a list of strings) to support transactions where multiple cards may have been used. Update your code to handle the new list format when accessing card information from transaction data.

## 5.0.0 - 2026-03-27
* The SDK now supports issuer-specific authentication tokens. The `x_kard_target_issuer` parameter has moved from the global client configuration to the `get_token()` method, enabling partners managing multiple issuers to scope auth tokens to specific issuers on a per-request basis. Update your authentication code to pass the issuer ID when calling `get_token()` instead of during client initialization.

## 4.2.0 - 2026-03-25
* The SDK now includes the last four digits of the card used for transactions. The new `card_last_four` field is available in `CoreTransactionAttributes` to provide additional transaction context.

## 4.1.0 - 2026-03-18
* The SDK now provides specialized types for user update operations. New `UpdateUserRequestAttributes` includes additional fields for email, hashed_email, phone_number, and birth_year. User update and fetch methods now return `UserResponseObject` for improved type consistency.

## 4.0.0 - 2026-03-18
* The progress bar API has been restructured with breaking changes. The `ProgressBarLabel` and `ProgressBarLabelPosition` types have been removed and replaced with `ProgressBarLabelPair` which uses explicit `left` and `right` fields. The `segment_icon` field has been replaced with a new `segments` configuration using `ProgressBarSegments` type. Update imports and field references to use the new structure.

## 3.15.0 - 2026-03-17
* The SDK now supports progress bar label configuration with new types for customizing label text and positioning in different layouts.

## 3.14.0 - 2026-03-17
* The ProgressBar model now includes an optional `segment_icon` field that allows specifying SVG icons for segmented progress bars.

## 3.13.0 - 2026-03-16
* The SDK now supports multi-tenant configurations through the new optional `x_kard_target_issuer` parameter on `KardApi` and `AsyncKardApi` clients. When provided, this parameter adds the `X-Kard-Target-Issuer` header to API requests, enabling proper tenant context specification.

## 3.12.0 - 2026-03-16
* New ProgressBar component available in OfferComponents to track offer redemption progress. The progress bar includes fields for total redemptions allowed, current user progress, display label, and segmentation options.

## 3.11.0 - 2026-03-13
* The `financial_institution_name` field in `CoreTransactionAttributes` now accepts any string value instead of being limited to a predefined set of financial institution names. This change provides greater flexibility when working with financial institution data.

## 3.10.0 - 2026-03-13
* New `OffersMeta` type available for accessing metadata about paginated offers results. The `OffersResponseObject` now includes an optional `meta` field containing all distinct categories available across the entire filtered result set.

## 3.9.0 - 2026-03-09
* New optional `filter_search` parameter added to rewards offers methods, allowing case-insensitive filtering by merchant name.

## 3.8.1 - 2026-03-09
* fix: correct API endpoint path for transaction file uploads
* This change fixes an incorrect API endpoint path that was causing transaction
* file upload requests to fail. The endpoint path was corrected from
* 'transactions/upload' to 'transactions/uploads' to match the expected server
* API specification.
* Key changes:
* Updated endpoint path from /v2/issuers/{id}/transactions/upload to /v2/issuers/{id}/transactions/uploads
* Fixed both synchronous and asynchronous client implementations
* Ensures proper routing to the correct server endpoint for file uploads
* 🌿 Generated with Fern

## 3.8.0 - 2026-03-04
* feat: add logo flare support and expand UI components
* Add support for logo flare configuration to enhance offer display with customizable badges and border colors. This update introduces new logo flare types and expands the existing ComponentType enum to include boosted rewards and logo flare components.
* Key changes:
* Add LogoFlare, LogoFlareBadge, LogoFlareBadgePosition, and LogoFlareBorderColor types
* Expand ComponentType to include "boostedReward" and "logoFlare" options
* Add SECONDARY option to ButtonStyle enum
* Add boosted_reward and logo_flare fields to OfferComponents
* Update documentation to remove hardcoded component type examples
* 🌿 Generated with Fern

## 3.7.0 - 2026-03-03
* feat: add bulk transaction file upload functionality
* Introduce new endpoint for generating presigned URLs to enable bulk transaction file uploads directly to storage. This feature allows uploading up to 10 JSONL transaction files (up to 5GB each) with presigned URLs valid for 15 minutes.
* Key changes:
* Add create_bulk_transactions_upload_url method to TransactionsClient and AsyncTransactionsClient
* Add new data models: CreateFileUploadAttributes, CreateFileUploadData, CreateFileUploadUrlResponse, FileUploadUrlAttributes, FileUploadUrlData
* Move ForbiddenError from files.errors to commons.errors for shared usage
* Update API documentation with comprehensive usage examples and parameter descriptions
* Support both plain JSONL and gzip-compressed file uploads
* Require transaction:write scope for bulk upload operations
* 🌿 Generated with Fern

## 3.6.0 - 2026-03-03
* feat: add file processing result notifications support
* This change introduces comprehensive support for file processing result notifications in the SDK. The new notification type enables clients to receive structured feedback about file processing operations, including status updates and metadata.
* Key changes:
* Add FileResultData type to represent file processing results in notifications
* Introduce NotificationDataUnion_FileProcessingResult variant for the new notification type
* Add "fileProcessingResult" to the NotificationType enum to support the new notification category
* Include optional errors field in NotificationPayload for enhanced error reporting
* Update all module exports and dynamic imports to expose the new types
* 🌿 Generated with Fern

## 3.5.0 - 2026-03-03
* feat: add FinancialInstitutionName union type for transactions
* Add a new union type to define valid financial institution names for transaction processing. This provides type safety and validation for financial institution names while maintaining backward compatibility.
* Key changes:
* Add FinancialInstitutionName union type with predefined valid institution names
* Update CoreTransactionAttributes to use the new union type instead of generic string
* Export FinancialInstitutionName across all relevant module init files
* Update reference documentation example to use valid institution name
* 🌿 Generated with Fern

## 3.4.0 - 2026-03-02
* feat: add start_icon field to CtaComponent
* Add support for displaying icons on CTA buttons by introducing a new optional start_icon field to the CtaComponent class. This enhancement allows developers to specify an icon identifier that will be rendered alongside the button text, improving the visual presentation and user experience of call-to-action elements.
* Key changes:
* Add optional start_icon field with "startIcon" alias to CtaComponent
* Include comprehensive docstring documenting the icon identifier functionality
* Maintain backward compatibility with existing implementations
* 🌿 Generated with Fern

## 3.3.2 - 2026-02-27
* chore: update CLI version in Fern metadata
* Update the Fern CLI version from 3.90.4 to 3.93.2 in the metadata configuration. This change maintains the existing generator settings while incorporating the latest CLI improvements and fixes.
* Key changes:
* Update cliVersion from 3.90.4 to 3.93.2
* Maintain existing generator name and version
* Preserve metadata configuration structure
* 🌿 Generated with Fern

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

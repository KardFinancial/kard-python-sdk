## 20.6.0 - 2026-07-10
### Added
* **`ContentStrategySort`** — new `"OFFERS_NEAR_YOU"` literal value added to the union, representing a sort order that surfaces offers near the user's location.

## 20.5.0 - 2026-07-02
### Added
* **`ProgressBarSegmentProgress`** — new Pydantic model representing the fill state of a single progress bar segment node, with `completed` and `total` integer fields indicating units completed within and required for the current segment.
* **`ProgressBarSegments.progress`** — new field of type `List[ProgressBarSegmentProgress]` providing per-segment fill state, index-aligned with segment nodes; reached nodes report 1 of 1, unreached nodes 0 of 1, and in-progress punch-card nodes report qualifying-purchase progress toward the next reward.

## 20.4.1 - 2026-07-02
* chore: update filter_search docstring and version placeholder
* Clarify the behavior of the `filter_search` parameter across rewards
* clients and update the User-Agent version string to the Fern placeholder.
* Key changes:
* Updated `filter_search` docstring from "filter offers by merchant name"
* to "Case-insensitive substring search. Returns offers whose offer name
* or category name contains the search string." in all rewards clients
* Updated User-Agent header version string to the Fern SDK placeholder
* 🌿 Generated with Fern

## 20.4.0 - 2026-06-29
### Added
* **`OfferMedium`** — new `"PUSH"` literal value added to the union, representing a push-notification offer delivery channel.

## 20.3.0 - 2026-06-23
### Added
* **`BatchesMeta`** — new Pydantic model representing metadata about a placement, with an optional `placement_name` field containing the display name resolved server-side.
* **`BatchesResponseObject.meta`** — new optional field of type `BatchesMeta` carrying placement metadata.
* **`OffersMeta.placement_name`** — new optional string field populated only on the Get Placement Content endpoint.

## 20.2.1 - 2026-06-23
* SDK regeneration
* Unable to analyze changes with AI, incrementing PATCH version.

## 20.2.0 - 2026-06-22
### Added
* **`RewardsClient.placement_content()`** and **`AsyncRewardsClient.placement_content()`** — new method that retrieves content for any placement type via a single unified endpoint (`GET v2/issuers/{org}/users/{user}/placements/{id}/content`), with the server resolving whether to return `standardOffer` or `placementBatch` resources.
* **`PlacementContentResponse`** — new Pydantic model representing the JSON:API response document, carrying a `data` list, optional `links`, optional `included` categories, and optional `meta`.
* **`PlacementContentData`** — new type alias (`Union[OfferDataUnion, PlacementBatchData]`) describing the polymorphic per-resource payload returned by the placement content endpoint.

## 20.1.0 - 2026-06-17
### Added
* **`TransactionsAttributes.account_id`** — new optional string field (`accountId`) that carries an account identifier associated with a transaction.

## 20.0.0 - 2026-06-11
### Breaking Changes
* **`CreateMainPageAttributes`**, **`CreateMainPagePlacementData`**, **`UpdateMainPageAttributes`**, **`UpdateMainPagePlacementData`**, **`MainPagePlacementAttributes`**, and **`MainPagePlacementData`** — removed; migrate to the new `CreateStandardAttributes` / `CreateStandardPlacementData`, `UpdateStandardAttributes` / `UpdateStandardPlacementData`, and `PlacementAttributes` / `PlacementData` equivalents.
* **`BatchActivationPlacementRelationships`** — removed and replaced by `SlottedPlacementRelationships`; update any direct imports or type annotations.
* **`CreatePlacementDataUnion_PlacementMainPage`**, **`UpdatePlacementDataUnion_PlacementMainPage`**, **`PlacementFormatUnion_PlacementMainPage`**, and **`IncludedResource_PlacementMainPage`** — removed; use the new `_Placement`, `_PlacementEmail`, or `_PlacementGroup` union variants instead.
### Added
* **`CreateStandardAttributes`**, **`CreateStandardPlacementData`**, **`UpdateStandardAttributes`**, and **`UpdateStandardPlacementData`** — new models replacing the removed `MainPage` equivalents for standard placement create and update operations.
* **`CreateEmailAttributes`**, **`CreateEmailPlacementData`**, **`UpdateEmailAttributes`**, and **`UpdateEmailPlacementData`** — new models for creating and updating email placements with cadence scheduling and slot configuration.
* **`CreateGroupAttributes`**, **`CreateGroupPlacementData`**, **`GroupPlacementAttributes`**, **`GroupPlacementData`**, **`UpdateGroupAttributes`**, and **`UpdateGroupPlacementData`** — new models for group placements, which expose slot details via `relationships.slots` and accept slot lists on update.
* **`SlottedPlacementRelationships`** — new relationships model replacing `BatchActivationPlacementRelationships`, used by group placements.
* **`PlacementTypeFilter`**, **`PlacementFormatUnion`**, **`CreatePlacementDataUnion`**, and **`UpdatePlacementDataUnion`** — extended with `placement`, `placementEmail`, and `placementGroup` variants to support all three placement types.

## 19.2.0 - 2026-06-10
### Added
* **`PushNotificationPlacementFileAttributes`**, **`PushNotificationPlacementFileData`**, and **`PushNotificationPlacementFileRelationships`** — new models representing a push-notification placement file notification, carrying placement name, available slot count, delivery cadence, and a presigned download URL.
* **`EmailNotificationPlacementFileAttributes`**, **`EmailNotificationPlacementFileData`**, and **`EmailNotificationPlacementFileRelationships`** — new models representing an email-notification placement file notification with the same core fields as the push variant.
* **`NotificationDataUnion_PushNotificationPlacementFile`** and **`NotificationDataUnion_EmailNotificationPlacementFile`** — two new discriminated-union variants added to `NotificationDataUnion`, enabling typed handling of `pushNotificationPlacementFile` and `emailNotificationPlacementFile` webhook payloads.
* **`NotificationType`** — extended with `"pushNotificationPlacementFile"` and `"emailNotificationPlacementFile"` literal values.

## 19.1.0 - 2026-06-10
### Added
* **`UpdateUserRequestAttributes.historical_transactions_sent`** — new optional boolean field that confirms historical transactions have been sent for a user; once set to `true` it cannot be reverted to `false`.

## 19.0.0 - 2026-06-01
### Breaking Changes
* **`PlacementBatchAttributes.short_description`** — field removed; access activation copy via `PlacementBatchAttributes.components` instead (the `OfferComponents` model now carries `shortDescription` and `longDescription`).
* **`PlacementBatchAttributes.long_description`** — field removed; access activation copy via `PlacementBatchAttributes.components` instead.

## 18.1.0 - 2026-06-01
### Added
* **`PlacementBatchAttributes.short_description`** — new `shortDescription` field providing a short, human-readable summary of how long a slot stays activated after a user taps activate (e.g. `"Activated for 24 hours"`), derived from the parent placement's `refreshInterval`.
* **`PlacementBatchAttributes.long_description`** — new `longDescription` field providing a longer description of the slot's activation behavior, clarifying which offers are activated and how long they remain active.

## 18.0.0 - 2026-06-01
### Breaking Changes
* **`BatchSlotData`** — removed from all public exports; replace all references with the new `PlacementBatchData` type. The `slotId` field is now `PlacementBatchData.id`, and `alias` is replaced by `PlacementBatchAttributes.name`.
* **`BatchesResponseObject.data`** — field type changed from `List[BatchSlotData]` to `List[PlacementBatchData]`; update any code that unpacks or type-checks elements of this list.
### Added
* **`PlacementBatchData`** — new JSON:API resource model representing one slot in a batch-activation placement, carrying `id`, `type`, and an `attributes` payload.
* **`PlacementBatchAttributes`** — new model holding per-slot attributes (including the new `name` display field, `is_active`, `offers`, and related fields) previously spread across `BatchSlotData`.

## 17.0.0 - 2026-06-01
### Added
* **`PlacementRelationships`** — new model exposing the optional `contentStrategy` to-one JSON:API relationship on `MainPagePlacementData` and `PushNotificationPlacementData` (and their `PlacementFormatUnion` variants).
* **`BatchActivationPlacementRelationships`** — new model added as a required `relationships` field on `BatchActivationPlacementData` and `PlacementFormatUnion_PlacementBatchActivation`; exposes a `slots` to-many relationship listing the slot resource identifiers.
* **`BatchActivationSlotRelationships`** and **`BatchActivationSlotInclusion`** — new models representing a `batchActivationSlot` resource's relationship back to its parent placement and its full shape as it appears in the `included` array.
* **`IncludedResource`** — new discriminated union (`contentStrategy` | `batchActivationSlot` | `placementMainPage` | `placementPushNotification`) covering every resource type that can appear in the `included` array.
* **`ResourceIdentifier`**, **`ToOneRelationship`**, and **`ToManyRelationship`** — new primitive JSON:API relationship payload models used throughout the relationship graph.

## 16.1.0 - 2026-05-28
### Added
* **`BatchSlotData.components`** — new optional `OfferComponents` field exposing slot-level UI components; carries a `cta` when the slot has no active activation, or a `logoFlare` decoration when it does.
* **`BatchSlotData.assets`** — new optional `List[Asset]` field exposing slot-level visual assets, currently a single `IMG_VIEW` SVG showing the slot's initials themed via the `--icon-fill` CSS custom property.

## 16.0.0 - 2026-05-28
### Breaking Changes
* **`get_earned_rewards` (`filter_include_unpaid` parameter)** — the `filter_include_unpaid` parameter has been removed and replaced by `filter_paid_in_full_only` across `TransactionsClient`, `AsyncTransactionsClient`, `RawTransactionsClient`, and `AsyncRawTransactionsClient`. The default behavior is also inverted: all matched transactions are now returned by default; pass `filter_paid_in_full_only=True` to restrict results to transactions paid in full to the issuer. Migrate by replacing `filter_include_unpaid=True` with `filter_paid_in_full_only=False` (or simply omit the argument) and `filter_include_unpaid=False` with `filter_paid_in_full_only=True`.
### Changed
* **`GetEarnedRewardsMeta.lifetimeRewardsInCents`** — docstring updated to reflect that all matched transactions are included in the lifetime total by default; pass `filter[paidInFullOnly]=true` to restrict the total to transactions paid in full to the issuer.

## 15.6.0 - 2026-05-28
### Added
* **`filter_include_unpaid`** — new optional boolean parameter on `get_earned_rewards` (all client variants) that maps to `filter[includeUnpaid]`; when `true`, returns matched transactions regardless of payment status and includes them in `lifetimeRewardsInCents`.
### Changed
* **`GetEarnedRewardsMeta.lifetimeRewardsInCents`** — docstring updated to clarify that only transactions paid in full to the issuer are counted by default, and that passing `filter[includeUnpaid]=true` includes all matched transactions.

## 15.5.1 - 2026-05-28
* chore: update child organization name validation docs
* Update docstrings and inline examples across child organization types
* and client methods to reflect the relaxed name validation rule: names
* now require at least one letter and may contain letters and spaces,
* replacing the previous uppercase-only, no-spaces constraint.
* Key changes:
* Update `ChildOrganizationAttributes.name` field docstring from "uppercase, no spaces" to "at least one letter; letters and spaces only"
* Update `CreateChildAttributes.name` field docstring and inline example (`"ACMECHILDBANK"` → `"Acme Child Bank"`)
* Update `UpdateChildAttributes.name` field docstring and inline example (`"NEWCHILDNAME"` → `"New Child Name"`)
* Update `create` method docstrings in `ChildrenClient`, `AsyncChildrenClient`, `RawChildrenClient`, and `AsyncRawChildrenClient`
* 🌿 Generated with Fern

## 15.5.0 - 2026-05-27
### Added
* **`EarnedRewardRelationships.offer`** — new `RelationshipSingle` field that exposes the related offer directly on earned-reward notification payloads.

## 15.4.1 - 2026-05-27
* chore: update deprecated uploads endpoint doc links to versioned URLs
* Update inline docstring links in UploadsClient, AsyncUploadsClient,
* RawUploadsClient, and AsyncRawUploadsClient to point to the versioned
* 2024-10-01 API reference paths instead of the old unversioned paths.
* Key changes:
* Replace `/api/uploads/create-upload-part` with `/2024-10-01/api/transactions/uploads/create-part`
* Replace `/api/uploads/create-upload` with `/2024-10-01/api/transactions/uploads/create`
* Reflow multi-line link text into single lines for readability
* 🌿 Generated with Fern

## 15.4.0 - 2026-05-26
### Added
* **`activate_placement_slot()`** — new method on `AttributionsClient` and `AsyncAttributionsClient` that records a slot-level `placementSlotAttribution` ACTIVATE event and fans out per-offer `offerAttribution` ACTIVATE events for every offer resolved by the slot's content strategy, returning the slot-level event id and resolved `offerIds`.
* **`ActivatePlacementSlotResponse`**, **`ActivatePlacementSlotResponseAttributes`**, and **`ActivatePlacementSlotResponseData`** — new models representing the acknowledgement payload returned by `activate_placement_slot()`.
* **`PlacementSlotAttributionAttributes`**, **`PlacementSlotAttributionRequest`**, and **`PlacementSlotMedium`** — new models for constructing slot-level attribution events on batch-activation placements.
* **`CreateAttributionRequestUnion_PlacementSlotAttribution`** — new discriminated-union variant (discriminator `"placementSlotAttribution"`) added to `CreateAttributionRequestUnion`.
* **`AttributionState.placement_id`** and **`AttributionState.slot_id`** — two new optional fields carrying placement and slot context for attribution events.

## 15.3.0 - 2026-05-26
### Added
* **`placement_batches()`** — new method on `RewardsClient` and `AsyncRewardsClient` that retrieves all slots for a batch-activation placement, including per-slot offer sets, aliases, and freshness fields (`isActive`, `lastActivatedAt`, `expiresAt`).
* **`BatchSlotData`** — new model representing a single slot within a batch-activation placement, carrying `slot_id`, `alias`, `is_active`, `last_activated_at`, `expires_at`, and `offers`.
* **`BatchesResponseObject`** — new model wrapping an ordered list of `BatchSlotData` entries returned by `placement_batches()`.

## 15.2.0 - 2026-05-26
### Added
* **`BatchActivationPlacementAttributes`**, **`BatchActivationPlacementData`**, and **`BatchActivationSlot`** — new models for reading a batch-activation placement resource and its constituent slots.
* **`CreateBatchActivationAttributes/PlacementData/Slot`** and **`UpdateBatchActivationAttributes/PlacementData/Slot`** — new models for creating and updating batch-activation placements, including `name`, `refresh_interval` (ISO-8601 duration), `content_strategy_id`, and `alias` fields.
* **`CreatePlacementDataUnion_PlacementBatchActivation`**, **`UpdatePlacementDataUnion_PlacementBatchActivation`**, and **`PlacementFormatUnion_PlacementBatchActivation`** — new discriminated-union variants (discriminator `"placementBatchActivation"`) added to the existing placement unions.
* **`PlacementTypeFilter`** — extended with the `"placementBatchActivation"` literal to support filtering by the new placement type.

## 15.1.0 - 2026-05-22
### Added
* **`ProgressBarSegmentLabel`** — new model representing label configuration (title and description) for a single node within a progress bar segment.
* **`ProgressBarSegmentSelection`** — new type alias (`"CURRENT"` or `"CURRENT_AND_BELOW"`) indicating which segment nodes the UI should render as selected based on current progress.
* **`ProgressBarSegmentSeparator`** — new type alias (`"LINE"`) specifying the separator style rendered between segment nodes.
* **`ProgressBarSegment.separator`**, **`ProgressBarSegment.labels`**, and **`ProgressBarSegment.selection`** — three new optional fields on `ProgressBarSegment` for configuring separators, per-node labels, and selection state respectively.

## 15.0.0 - 2026-05-21
### Breaking Changes
* **`ContentStrategyFilter`** — removed and replaced by **`ContentStrategySort`**; update any imports from `kard.organizations.content_strategies` to use `ContentStrategySort` instead.
* **`ContentStrategyAttributes.filter`**, **`CreateContentStrategyAttributes.filter`**, and **`UpdateContentStrategyAttributes.filter`** — the optional `filter` field has been renamed to `sort`; migrate by replacing `filter=...` with `sort=...` when constructing or reading these models.

## 14.0.0 - 2026-05-20
### Breaking Changes
* **`PlacementsClient.get`** and **`AsyncPlacementsClient.get`** (and their raw counterparts) now return `PlacementResource` instead of `PlacementFormatUnion`; migrate by accessing `.data` on the returned object to retrieve the placement.
* **`MainPagePlacementAttributes`** and **`PushNotificationPlacementAttributes`** — the required `created_at` and `last_modified` fields have been removed; remove these fields from any model construction or pattern-matching code.
* **`ContentStrategyAttributes`** — the required `created_at` and `last_modified` fields have been removed; remove these fields from any model construction or pattern-matching code.
### Added
* **`PlacementResource`** — new model wrapping a single placement document with a `data: PlacementFormatUnion` field and an optional `included: List[ContentStrategyResponse]` array for embedded related resources.
* **`include`** — new optional parameter on `PlacementsClient.list`, `PlacementsClient.get`, `AsyncPlacementsClient.list`, and `AsyncPlacementsClient.get` (and raw counterparts) accepting a CSV string (e.g. `"contentStrategy"`) to embed related resources in the response.
* **`PlacementListResponse.included`** — new optional field containing embedded `ContentStrategyResponse` objects when `include=contentStrategy` is requested on the list endpoint.

## 13.0.0 - 2026-05-20
### Breaking Changes
* **`ContentStrategyAttributes.filters`**, **`CreateContentStrategyAttributes.filters`**, and **`UpdateContentStrategyAttributes.filters`** — the required `filters: List[ContentStrategyFilter]` field has been removed and replaced with a single optional `filter: Optional[ContentStrategyFilter]` field (default `None`); migrate by replacing `filters=[...]` with `filter=...` (a single value or `None`) when constructing these models.

## 12.2.0 - 2026-05-19
### Added
* **`filter_content_strategy_id`** — new optional parameter on `PlacementsClient.list` and `AsyncPlacementsClient.list` (and their raw counterparts) to filter placements by the ID of a linked content strategy.
* **`content_strategy_id`** — new optional field on `CreateMainPageAttributes`, `CreatePushNotificationAttributes`, `UpdateMainPageAttributes`, and `UpdatePushNotificationAttributes` to link a placement to a content strategy at creation or update time.
* **`content_strategy_id`** — new optional field on `MainPagePlacementAttributes` and `PushNotificationPlacementAttributes` response models exposing the ID of the content strategy linked to a placement, if any.

## 12.1.0 - 2026-05-19
### Added
* **`ContentStrategiesClient`** and **`AsyncContentStrategiesClient`** — new sub-clients accessible via `client.organizations.content_strategies` supporting `create`, `list`, `get`, `update`, and `delete` operations for content strategies scoped to an organization.
* **`RawContentStrategiesClient`** and **`AsyncRawContentStrategiesClient`** — new raw clients for the same content strategy operations against the `v2/issuers/{organizationId}/contentStrategies` endpoint.
* **`ContentStrategyAttributes`** and **`ContentStrategyFilter`** — new models representing content strategy attributes (`name`, `filters`, `categories`, `category_exclusions`, `merchant_exclusions`, `created_at`, `last_modified`) and a filter type alias (`NEWLY_LIVE`, `EXPIRING_SOON`, `HIGHEST_CASHBACK`, `PERSONALIZED`).
* **`ContentStrategyResponse`** and **`ContentStrategyListResponse`** — new response models for retrieving a single content strategy or a paginated list.
* **`CreateContentStrategyRequestBody`**, **`UpdateContentStrategyRequestBody`**, and related request data/attribute types — new request models for creating (name must be unique within the organization) and fully replacing (all fields required) a content strategy.

## 12.0.0 - 2026-05-14
### Breaking Changes
* **`LocationAttributes.partner_ids`** — field is now required (`List[LocationPartnerId]`) instead of optional (`Optional[List[LocationPartnerId]]`, defaulting to `None`); any code constructing `LocationAttributes` without providing `partner_ids` will now raise a Pydantic validation error — pass an explicit list (e.g. `partner_ids=[]`) to migrate.

## 11.0.0 - 2026-05-14
### Breaking Changes
* **`EarnedRewardAttributes`** — class has been removed from the public API; update any imports to use `RewardNotificationAttributes` instead, which is now the type of `EarnedRewardApprovedData.attributes` and `NotificationDataUnion_EarnedRewardApproved.attributes`.
* **`RewardNotificationAttributes`** — two new required fields, `transaction_id` (`str`) and `transaction_amount_in_cents` (`int`), have been added; any code constructing this model (or subclasses) must now supply these values.
* **`EarnedRewardSettledAttributes`** — the `transaction_timestamp` field has been removed from this class; it is now inherited from the base `RewardNotificationAttributes`.

## 10.2.0 - 2026-05-12
### Added
* **`LocationPartnerId`** — new model representing a third-party partner identifier (e.g. Google) associated with a LOCAL location, with `type` and `id` fields.
* **`LocationPartnerIdType`** — new type alias for the partner identifier kind; currently supports `"google"` with an open union for future values.
* **`LocationAttributes.partner_ids`** — new optional field (`List[LocationPartnerId] | None`) exposing third-party partner IDs on LOCAL locations; absent on non-LOCAL locations.

## 10.1.3 - 2026-05-07
* chore: correct required scope in bulk upload URL docstrings
* Update the documented required OAuth scope for the
* `create_bulk_transactions_upload_url` endpoint from `transaction:write`
* to `files:write` across all client variants. This is a documentation-only
* fix — no public API signatures, types, or runtime behavior are changed.
* Key changes:
* Replace `transaction:write` with `files:write` in the `create_bulk_transactions_upload_url` docstring in `TransactionsClient`
* Apply the same correction to `AsyncTransactionsClient`
* Mirror both fixes in `RawTransactionsClient` and `AsyncRawTransactionsClient`
* 🌿 Generated with Fern

## 10.1.2 - 2026-04-30
* chore: update bulk upload docstrings and deprecate legacy upload endpoints
* Refresh documentation across the transactions and uploads clients to
* reflect expanded bulk upload support and guide users toward the
* recommended historical transaction ingestion flow.
* Key changes:
* Update `create_bulk_transactions_upload_url` docstring to document support for both `incomingTransactionsFile` and `historicalTransactionsFile` types, replacing the outdated `coreTransaction`-only note
* Add deprecation notices to all `UploadsClient` and `RawUploadsClient` methods (`create_upload`, `create_upload_part`, `update_upload`) directing users to the bulk transactions upload URL endpoint
* Apply deprecation notices consistently across sync and async variants in both `client.py` and `raw_client.py`
* 🌿 Generated with Fern

## 10.1.1 - 2026-04-28
* chore: update test fixture asset URLs and alt text in rewards response objects
* Refresh the example asset data used in `LocationsResponseObject` and
* `OffersResponseObject` type docstring/test fixtures. The placeholder
* URLs and alt text strings are replaced with more realistic attribution
* URLs and empty alt strings that better reflect real API responses.
* Key changes:
* Replace `http://assets.getkard.com/logo/img?attribution-tokens` with a realistic attribution URL in both `LocationsResponseObject` and `OffersResponseObject` fixtures
* Replace `http://assets.getkard.com/banner/img?attribution-tokens` with a realistic banner attribution URL in both fixtures
* Replace placeholder alt text ("Worlds Greatest Chicken Logo Image" / "Worlds Greatest Chicken Banner Image") with empty strings
* 🌿 Generated with Fern

## 10.1.0 - 2026-04-23
### Added
* **`EarnedRewardAttributes.transaction_timestamp`** — new optional `datetime` field that surfaces the ISO-formatted timestamp of the originating transaction in earned-reward notification payloads.
* **`EarnedRewardSettledAttributes.transaction_timestamp`** — new optional `datetime` field that surfaces the ISO-formatted timestamp of the originating transaction in settled earned-reward notification payloads.

## 10.0.0 - 2026-04-17
### Breaking Changes
* **`CommissionEarnedDetails`** — the required `issuer: CommissionValue` field is removed; callers that read `.issuer` will receive an `AttributeError`. Remove any access to `.issuer` from your code.
* **`RewardedTransactionAttributes`** — the optional fields `card_bin` and `card_last_four` are removed; any code that reads these fields must be updated.
* **`RewardedTransactionAttributes.status`** — the type is narrowed from the open `RewardedTransactionStatus` enum to `Literal["SETTLED"]`; code that sets or compares this field to non-`"SETTLED"` values must migrate to the new `ApprovedTransactionAttributes` model for APPROVED transactions.
* **`RewardedTransactionUnion`** — changed from a simple alias for `RewardedTransactionUnion_RewardedTransaction` to a discriminated `Union` keyed on a `type` field; code that assumed a single concrete type must handle both variants.
### Added
* **`ApprovedTransaction`** — new Pydantic model representing a transaction in the `APPROVED` state, with `id`, `attributes`, and `relationships` fields; exported from `kard`, `kard.transactions`, and `kard.transactions.types`.
* **`ApprovedTransactionAttributes`** — new Pydantic model carrying `status` (always `"APPROVED"`), `transaction_id`, `transaction_amount_in_cents`, and `transaction_timestamp` for approved transactions.
* **`RewardedTransactionUnion_ApprovedTransaction`** — new tagged-union variant (discriminator `type="approvedTransaction"`) added alongside the existing `RewardedTransactionUnion_RewardedTransaction`.

## 9.0.0 - 2026-04-17
* feat!: remove MerchantNetwork/MerchantNetworkName, add ChildOrganizationResponse, change OrganizationsClient.get signature
* Significant API surface changes across the organizations and internal_organizations modules.
* The `MerchantNetwork` and `MerchantNetworkName` types are removed from
* `kard.internal_organizations` and no longer exported from the top-level
* `kard` package. `ExternalOrganizationAttributes` loses several fields
* (`external_id`, `parent_organization_id`, `merchant_networks`,
* `national_offers`, `local_offers`, `use_attribution`, `created_at`,
* `updated_at`) and gains new required commission-split fields
* (`affiliate_commission_split`, `cardlinked_commission_split`,
* `cardlinked_user_commission_split`).
* The `organization_id` required parameter is removed from
* `OrganizationsClient.get` / `AsyncOrganizationsClient.get` and their
* raw variants; the endpoint now calls `v2/issuer` (no path parameter).
* Two new types — `ChildOrganizationAttributes` and
* `ChildOrganizationResponse` — replace `ExternalOrganizationResponse` as
* the return type for all `ChildrenClient` create/get/update methods.
* Key changes:
* Remove `MerchantNetwork`, `MerchantNetworkName` public types from `kard.internal_organizations` and top-level `kard` exports
* Remove `organization_id` required positional parameter from `OrganizationsClient.get` / `AsyncOrganizationsClient.get` (and raw variants); URL changed from `v2/issuers/{id}` to `v2/issuer`
* Add `ChildOrganizationAttributes` and `ChildOrganizationResponse` Pydantic models; all `ChildrenClient` methods now return `ChildOrganizationResponse` instead of `ExternalOrganizationResponse`
* Remove multiple fields from `ExternalOrganizationAttributes` (`external_id`, `parent_organization_id`, `merchant_networks`, `national_offers`, `local_offers`, `use_attribution`, `created_at`, `updated_at`) and add new required commission-split fields
* 🌿 Generated with Fern

## 8.7.0 - 2026-04-16
### Added
* **`MerchantAsset`** — new Pydantic model representing an attribution-signed asset image (logo, banner, etc.) for a merchant, with `type`, `url`, and optional `alt` fields; exported from `kard`, `kard.transactions`, and `kard.transactions.types`.
* **`MerchantAssetType`** — new type alias for the supported asset kinds (`"IMG_VIEW"`, `"BANNER_VIEW"`); exported from the same modules as `MerchantAsset`.
* **`assets` field on `TransactionMerchantAttributes`** — new optional `List[MerchantAsset]` field that surfaces attribution-signed merchant images directly within transaction responses.

## 8.6.0 - 2026-04-16
### Added
* **`PlacementTypeFilter`** — new type representing the two supported placement kinds (`placementMainPage`, `placementPushNotification`); exported from `kard.organizations`, `kard.organizations.placements`, and `kard.organizations.placements.types`.
* **`filter_type` and `filter_name` parameters on `PlacementsClient.list` / `AsyncPlacementsClient.list`** — optional parameters to filter the placements list by type or exact name, reducing the need for client-side filtering.
* **`filter_type` and `filter_name` parameters on `RawPlacementsClient.list` / `AsyncRawPlacementsClient.list`** — same filtering capability exposed on the raw HTTP client variants.
### Changed
* **`RawPlacementsClient.list` / `AsyncRawPlacementsClient.list`** — now raises `InvalidRequest` on HTTP 400 responses from the placements list endpoint.

## 8.5.0 - 2026-04-16
### Added
* **`RewardsClient.placement_offers` / `AsyncRewardsClient.placement_offers`** — new method that retrieves cash-back offers for a placement slot, sorted by highest cash back and limited by the placement's available slots; requires the `rewards:read` scope.
* **`RawRewardsClient.placement_offers` / `AsyncRawRewardsClient.placement_offers`** — raw HTTP variants of the same endpoint, returning `HttpResponse[OffersResponseObject]` and `AsyncHttpResponse[OffersResponseObject]` respectively.
* **Placement offers filtering** — optional parameters `filter_search`, `filter_purchase_channel`, `filter_category`, `filter_is_targeted`, `include`, and `supported_components` allow fine-grained control over the offers returned.

## 8.4.0 - 2026-04-16
### Changed
* **`filter_status` on `get_earned_rewards`** — parameter type narrowed from `Optional[str]` to `Optional[RewardedTransactionStatus]` across all `TransactionsClient` variants; passing `APPROVED` now explicitly returns only approved transactions without a corresponding settled transaction.
### Added
* **`OrganizationsClient` / `AsyncOrganizationsClient`** — new top-level clients accessible via `client.organizations` with a `get(organization_id)` method to retrieve organization details for the authenticated issuer.
* **`ChildrenClient` / `AsyncChildrenClient`** — new sub-clients at `client.organizations.children` for full CRUD management of child organizations, including cursor-based pagination on `list` and supporting request/response types `CreateChildRequestData`, `UpdateChildRequestData`, and `ChildOrganizationListResponse`.
* **`PlacementsClient` / `AsyncPlacementsClient`** — new sub-clients at `client.organizations.placements` for full CRUD management of organization placements, supporting `placementMainPage` and `placementPushNotification` kinds with scheduling types `Cadence`, `CadenceFrequency`, and `DayOfWeek`.
* **`ExternalOrganizationAttributes` / `ExternalOrganizationResponse`** — new Pydantic models available from `kard.organizations` describing organization resources including enrolled rewards, card networks, BINs, and optional merchant networks.

## 8.3.0 - 2026-04-15
### Added
* **`GetEarnedRewardsMeta`** — new type (available from `kard`, `kard.transactions`, and `kard.transactions.types`) containing `lifetime_rewards_in_cents`, the user's total lifetime rewards in cents across all matched transactions.
* **`filter_status` parameter on `get_earned_rewards`** — optional comma-separated string accepted by `TransactionsClient`, `AsyncTransactionsClient`, and their raw counterparts; supported values are `APPROVED` and `SETTLED` (defaults to `SETTLED` when omitted).
* **`meta` field on `GetEarnedRewardsResponse`** — every earned-rewards response now includes a `meta` object of type `GetEarnedRewardsMeta`.
### Changed
* **`RewardedTransactionStatus`** — now includes `"APPROVED"` as a recognized literal value in addition to `"SETTLED"`.

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

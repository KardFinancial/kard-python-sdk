# Reference
## Auth
<details><summary><code>client.auth.<a href="src/kard/auth/client.py">get_token</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.auth.get_token(
    client_id="client_id",
    client_secret="client_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**x_kard_target_issuer:** `typing.Optional[str]` — (Beta) Target issuer ID for partners managing multiple issuers on the Kard platform. When set, the auth token will be scoped to this specific issuer. Required if you manage more than one issuer; omit if you operate a single issuer integration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/kard/files/client.py">get_metadata</a>(...) -> GetFilesMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves metadata for files associated with a specific issuer/organization.
This endpoint supports pagination and sorting options to efficiently navigate 
through potentially large sets of file metadata.
<b>Required scopes:</b> `files.read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.files.get_metadata(
    organization_id="organization-123",
    page_size=5,
    filter_date_from="2025-02-20T21:56:23Z",
    filter_date_to="2025-03-20T21:56:23Z",
    filter_file_type="earnedRewardApprovedDailyReconciliationFile",
    sort=[
        "-sentDate"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**filter_date_from:** `typing.Optional[str]` — Start date for filtering files (format ISO8601). If not provided, defaults to current date minus 1 month.
    
</dd>
</dl>

<dl>
<dd>

**filter_date_to:** `typing.Optional[str]` — End date for filtering files (format ISO8601). If not provided, defaults to current date.
    
</dd>
</dl>

<dl>
<dd>

**filter_file_type:** `typing.Optional[FileType]` — The document file type.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page. Defaults to 10 if not specified and maximum value allowed 100 items per page.
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor for forward pagination (next page).
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` — Cursor for backward pagination (previous page).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[FilesMetadataSortOptions, typing.Sequence[FilesMetadataSortOptions]]]` — If provided, response will be sorted by the specified fields. Defaults to descending sentDate, equivalent to "-sentDate"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">get</a>(...) -> SubscriptionsResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to fetch the subscriptions of the provided issuer.<br/>
<b>Required scopes:</b> `notifications:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.notifications.subscriptions.get(
    organization_id="organization-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**filter_event_name:** `typing.Optional[NotificationType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">create</a>(...) -> CreateSubscriptionsResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to subscribe to notification events.<br/>
<b>Required scopes:</b> `notifications:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.notifications.subscriptions import SubscriptionRequestUnion_Subscription, SubscriptionRequestAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.notifications.subscriptions.create(
    organization_id="organization-123",
    data=[
        SubscriptionRequestUnion_Subscription(
            attributes=SubscriptionRequestAttributes(
                event_name="earnedRewardApproved",
                webhook_url="https://webhookUrl.com/post",
                enabled=True,
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SubscriptionRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.subscriptions.<a href="src/kard/notifications/subscriptions/client.py">update</a>(...) -> UpdateSubscriptionsResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update existing notification subscriptions.<br/>
<b>Required scopes:</b> `notifications:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.notifications.subscriptions import UpdateSubscriptionRequestUnion_Subscription, UpdateSubscriptionRequestAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.notifications.subscriptions.update(
    organization_id="organization-123",
    subscription_id="subscription-123",
    data=UpdateSubscriptionRequestUnion_Subscription(
        attributes=UpdateSubscriptionRequestAttributes(
            event_name="earnedRewardApproved",
            webhook_url="https://webhookUrl.com/post",
            enabled=True,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `SubscriptionId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSubscriptionRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/kard/organizations/client.py">get</a>(...) -> ExternalOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve organization details for the authenticated issuer
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.get(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization (must match the authenticated issuer)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Children
<details><summary><code>client.organizations.children.<a href="src/kard/organizations/children/client.py">list</a>(...) -> ChildOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List child organizations belonging to the authenticated issuer
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.children.list(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the parent organization
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor value for the next page of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Maximum number of records to return [1 - 200] (default = 200)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.children.<a href="src/kard/organizations/children/client.py">create</a>(...) -> ExternalOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a child organization by cloning the parent and overriding specified fields. An 8-digit numeric ID is generated automatically. The name is required, must be uppercase, and must not contain spaces.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.organizations.children import CreateChildRequestData, CreateChildAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.children.create(
    organization_id="organizationId",
    data=CreateChildRequestData(
        type="organization",
        attributes=CreateChildAttributes(
            name="name",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the parent organization
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateChildRequestBody` — Child organization data for creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.children.<a href="src/kard/organizations/children/client.py">get</a>(...) -> ExternalOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific child organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.children.get(
    organization_id="organizationId",
    child_id="childId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the parent organization
    
</dd>
</dl>

<dl>
<dd>

**child_id:** `str` — Unique identifier of the child organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.children.<a href="src/kard/organizations/children/client.py">update</a>(...) -> ExternalOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a child organization. Only the name can be changed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.organizations.children import UpdateChildRequestData, UpdateChildAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.children.update(
    organization_id="organizationId",
    child_id="childId",
    data=UpdateChildRequestData(
        type="organization",
        attributes=UpdateChildAttributes(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the parent organization
    
</dd>
</dl>

<dl>
<dd>

**child_id:** `str` — Unique identifier of the child organization
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateChildRequestBody` — Child organization data for update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.children.<a href="src/kard/organizations/children/client.py">delete</a>(...) -> DeleteResourceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a child organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.children.delete(
    organization_id="organizationId",
    child_id="childId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the parent organization
    
</dd>
</dl>

<dl>
<dd>

**child_id:** `str` — Unique identifier of the child organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Placements
<details><summary><code>client.organizations.placements.<a href="src/kard/organizations/placements/client.py">create</a>(...) -> PlacementFormatUnion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a placement for the organization. Use type "placementMainPage" for main-page placements (requires name and availableSlots) or "placementPushNotification" for push-notification placements (requires name and cadence; availableSlots is automatically set to 1).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.organizations.placements import CreatePlacementDataUnion_PlacementMainPage, CreateMainPageAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.placements.create(
    organization_id="org-123",
    data=CreatePlacementDataUnion_PlacementMainPage(
        attributes=CreateMainPageAttributes(
            name="Homepage Banner",
            available_slots=5,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreatePlacementRequestBody` — Placement data for creation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.placements.<a href="src/kard/organizations/placements/client.py">list</a>(...) -> PlacementListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List placements belonging to the authenticated organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.placements.list(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor value for the next page of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Maximum number of records to return [1 - 200] (default = 200)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.placements.<a href="src/kard/organizations/placements/client.py">get</a>(...) -> PlacementFormatUnion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific placement
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.placements.get(
    organization_id="organizationId",
    placement_id="placementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization
    
</dd>
</dl>

<dl>
<dd>

**placement_id:** `str` — Unique identifier of the placement (UUID v7)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.placements.<a href="src/kard/organizations/placements/client.py">update</a>(...) -> PlacementFormatUnion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a placement. All fields must be provided. Use type "placementMainPage" or "placementPushNotification" to set the placement kind. If the type is "placementPushNotification", availableSlots is automatically set to 1.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.organizations.placements import UpdatePlacementDataUnion_PlacementMainPage, UpdateMainPageAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.placements.update(
    organization_id="organizationId",
    placement_id="placementId",
    data=UpdatePlacementDataUnion_PlacementMainPage(
        attributes=UpdateMainPageAttributes(
            name="name",
            available_slots=1,
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization
    
</dd>
</dl>

<dl>
<dd>

**placement_id:** `str` — Unique identifier of the placement (UUID v7)
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdatePlacementRequestBody` — Placement data for update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.placements.<a href="src/kard/organizations/placements/client.py">delete</a>(...) -> DeleteResourceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a placement
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.organizations.placements.delete(
    organization_id="organizationId",
    placement_id="placementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Unique identifier of the organization
    
</dd>
</dl>

<dl>
<dd>

**placement_id:** `str` — Unique identifier of the placement (UUID v7)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ping
<details><summary><code>client.ping.<a href="src/kard/ping/client.py">ping</a>() -> PingResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to verify network connectivity and service availability.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.ping.ping()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create</a>(...) -> TransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to send all transactions made by all your enrolled users in your rewards program. The request body will depend on the transaction type.<br/>
Please use the correct type when calling the endpoint:
- `transaction`: These incoming transactions will be processed and matched by the Kard system. Learn more about the [Transaction CLO Matching](https://github.com/kard-financial/kard-postman#c-transaction-clo-matching) flow here.
- `matchedTransaction`: For pre-matched transactions that need validation on match by the Kard system.
- `coreTransaction`: For transactions from core banking systems with limited card-level data.<br/>

<b>Required scopes:</b> `transaction:write`<br/>
<b>Note:</b> `Maximum of 500 transactions can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.transactions import Transactions_Transaction, TransactionsAttributes, Merchant, ProcessorMid_Visa, VisaMidDetails
import datetime

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.transactions.create(
    organization_id="organization-123",
    data=[
        Transactions_Transaction(
            id="309rjfoincor3icno3rind093cdow3jciwjdwcm",
            attributes=TransactionsAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                status="APPROVED",
                amount=1000,
                subtotal=800,
                currency="USD",
                direction="DEBIT",
                payment_type="CARD",
                description="ADVANCEAUTO",
                description_2="ADVANCEAUTO",
                mcc="1234",
                card_bin="123456",
                card_last_four="4321",
                authorization_date=datetime.datetime.fromisoformat("2021-07-02T17:47:06+00:00"),
                merchant=Merchant(
                    id="12345678901234567",
                    name="ADVANCEAUTO",
                    addr_street="125 Main St",
                    addr_city="Philadelphia",
                    addr_state="PA",
                    addr_zipcode="19147",
                    addr_country="United States",
                    latitude="37.9419429",
                    longitude="-73.1446869",
                    store_id="12345",
                ),
                authorization_code="123456",
                retrieval_reference_number="100804333919",
                acquirer_reference_number="1234567890123456789012345678",
                system_trace_audit_number="333828",
                transaction_id="2467de37-cbdc-416d-a359-75de87bfffb0",
                card_product_id="1234567890123456789012345678",
                processor_mids=ProcessorMid_Visa(
                    mids=VisaMidDetails(
                        vmid="12345678901",
                        vsid="12345678",
                    ),
                ),
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TransactionsRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_fraud_markers</a>(...) -> FraudulentTransactionObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to flag a submitted transaction as fraudulent. This will prevent it from being rewarded.<br/>

<b>Required scopes:</b>&nbsp;&nbsp;`transaction:write`<br/>
<b>Note:</b> `Maximum of 500 fraudulent transactions can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.transactions import FraudulentTransactionData, FraudulentTransactionAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.transactions.create_fraud_markers(
    organization_id="organization-123",
    data=[
        FraudulentTransactionData(
            id="myTxnId12345",
            type="fraudulentTransaction",
            attributes=FraudulentTransactionAttributes(
                user_id="userId123",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `FraudulentTransactionRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_audits</a>(...) -> CreateAuditResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to request that a particular transaction be audited further by the Kard system, in the event of a missing cashback claim, incorrect cashback amount claim or other mis-match claims.<br/>
<b>Required scopes:</b> `audit:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.transactions import CreateAuditRequestDataUnion_Audit, AuditAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.transactions.create_audits(
    organization_id="organization-123",
    user_id="user-123",
    data=[
        CreateAuditRequestDataUnion_Audit(
            attributes=AuditAttributes(
                audit_code=8001,
                merchant_name="Caribbean Goodness",
                audit_description="duplicate transaction",
                transaction_id="issuerTransaction123",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateAuditRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">create_bulk_transactions_upload_url</a>(...) -> CreateFileUploadUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates up to 10 presigned PUT URLs for uploading JSONL transaction files (up to 5GB each) directly
to storage. Each URL is valid for 15 minutes. Use the returned URL to upload the file via an HTTP PUT request with the
binary file content as the body. If a URL expires before the upload completes, you must request a new one.
Files can be uploaded as plain JSONL or as a gzip-compressed file.
Only `coreTransaction` type is supported for bulk file uploads.
<b>Required scopes:</b> `transaction:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.transactions import CreateFileUploadData, CreateFileUploadAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.transactions.create_bulk_transactions_upload_url(
    organization_id="organization-123",
    data=[
        CreateFileUploadData(
            type="incomingTransactionsFile",
            attributes=CreateFileUploadAttributes(
                filename="transaction_12345.jsonl",
            ),
        ),
        CreateFileUploadData(
            type="incomingTransactionsFile",
            attributes=CreateFileUploadAttributes(
                filename="transaction_67890.jsonl",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateFileUploadRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/kard/transactions/client.py">get_earned_rewards</a>(...) -> GetEarnedRewardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve rewarded transaction history for a specific user. By default this returns only SETTLED transactions within the last 12 months.
<br/>
<b>Required scopes:</b> `transaction:read`
<br/>
<b>Query Limit:</b> Maximum of 12 months of transaction data can be queried.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.transactions.get_earned_rewards(
    organization_id="org-123",
    user_id="user-456",
    page_size=10,
    filter_status="APPROVED",
    include="merchant,offer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` — Cursor for next page (base64-encoded timestamp + transaction ID)
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` — Cursor for previous page (base64-encoded timestamp + transaction ID)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[RewardedTransactionStatus]` — Filter by transaction status. Supported values are `APPROVED` and `SETTLED`. Defaults to `SETTLED` when omitted. When `APPROVED` is specified, only approved transactions that do not yet have a corresponding settled transaction are returned.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Comma-separated list of related resources to include in the response. Supported values are `merchant` and `offer`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/kard/users/client.py">create</a>(...) -> CreateUsersObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to enroll a specified user into your rewards program.<br/>

<b>Required scopes:</b>&nbsp;&nbsp;`user:write`<br/>
<b>Note:</b> `Maximum of 100 users can be created per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users import UserRequestDataUnion_User, UserRequestAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.create(
    organization_id="organization-123",
    data=[
        UserRequestDataUnion_User(
            id="1234567890",
            attributes=UserRequestAttributes(
                zip_code="11238",
                enrolled_rewards=[
                    "CARDLINKED"
                ],
                email="user@example.com",
                hashed_email="a94a8fe5ccb19ba61c4c0873d391e987982fbbd3e2d8a5b76e45a1d4c4e2e3a1",
                phone_number="+14155552671",
                birth_year="1990",
                historical_transactions_sent=True,
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateUsersObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">update</a>(...) -> UserResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update the details on a specified user.<br/>

<b>Required scopes:</b> `user:update`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users import UpdateUserRequestDataUnion_User, UpdateUserRequestAttributes

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.update(
    organization_id="organization-123",
    user_id="user-123",
    data=UpdateUserRequestDataUnion_User(
        id="1234567890",
        attributes=UpdateUserRequestAttributes(
            zip_code="11238",
            enrolled_rewards=[
                "CARDLINKED"
            ],
            email="user@example.com",
            hashed_email="a94a8fe5ccb19ba61c4c0873d391e987982fbbd3e2d8a5b76e45a1d4c4e2e3a1",
            phone_number="+14155552671",
            birth_year="1990",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateUserObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">delete</a>(...) -> DeleteUserResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to delete a specified enrolled user from the rewards program and Kard's system. Users can be re-enrolled into rewards by calling the [Create User](/2024-10-01/api/users/create) endpoint using the same `id` from before.<br/>

<b>Required scopes:</b> `user:delete`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.delete(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/kard/users/client.py">get</a>(...) -> UserResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to fetch the details on a specified user.<br/>
<br/>
<b>Required scopes:</b>&nbsp;&nbsp;`user:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.get(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Attributions
<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">create</a>(...) -> CreateAttributionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to send attribution events made by a single enrolled user for processing. A maximum of 100 events can be included in a single request.

<b>Required scopes:</b> `attributions:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users.attributions import CreateAttributionRequestUnion_OfferAttribution, OfferAttributionAttributes, CreateAttributionRequestUnion_NotificationAttribution, NotificationAttributionAttributes
import datetime

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.attributions.create(
    organization_id="organization-123",
    user_id="user-123",
    data=[
        CreateAttributionRequestUnion_OfferAttribution(
            attributes=OfferAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c075",
                event_code="VIEW",
                medium="SEARCH",
                event_date=datetime.datetime.fromisoformat("2025-01-01T00:00:00+00:00"),
            ),
        ),
        CreateAttributionRequestUnion_OfferAttribution(
            attributes=OfferAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c077",
                event_code="IMPRESSION",
                medium="EMAIL",
                event_date=datetime.datetime.fromisoformat("2025-01-01T00:00:00+00:00"),
            ),
        ),
        CreateAttributionRequestUnion_NotificationAttribution(
            attributes=NotificationAttributionAttributes(
                entity_id="60e4ba1da31c5a22a144c076",
                event_code="IMPRESSION",
                medium="PUSH",
                event_date=datetime.datetime.fromisoformat("2025-01-01T00:00:00+00:00"),
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateAttributionRequestObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">activate</a>(...) -> ActivateOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record when a user activates an offer. Creates an attribution event with eventCode=ACTIVATE and medium=CTA.
Optionally include the offer data by passing `include=offer`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.attributions.activate(
    organization_id="organization-123",
    user_id="user-123",
    offer_id="offer-456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**offer_id:** `str` — The unique identifier of the offer being activated
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the offer response (when include=offer).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[ActivateOfferIncludeOption, typing.Sequence[ActivateOfferIncludeOption]]]` — Related resources to include in the response. Allowed value is `offer`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.attributions.<a href="src/kard/users/attributions/client.py">boost</a>(...) -> BoostOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record when a user boosts an offer. Creates an attribution event with eventCode=BOOST and medium=CTA.
Optionally include the offer data by passing `include=offer`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.attributions.boost(
    organization_id="organization-123",
    user_id="user-123",
    offer_id="offer-456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**offer_id:** `str` — The unique identifier of the offer being boosted
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the offer response (when include=offer).
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[BoostOfferIncludeOption, typing.Sequence[BoostOfferIncludeOption]]]` — Related resources to include in the response. Allowed value is `offer`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WebView
<details><summary><code>client.users.auth.<a href="src/kard/users/auth/client.py">get_web_view_token</a>(...) -> WebViewTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an OAuth token for webview authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.auth.get_web_view_token(
    organization_id="organization-123",
    user_id="user-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Rewards
<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">offers</a>(...) -> OffersResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national brand offers that a specified user is eligible for. Call this endpoint to build out your
[targeted offers UX experience](/2024-10-01/api/getting-started#b-discover-a-lapsed-customer-clo). Local offers details
can be found by calling the [Get Eligible Locations](/2024-10-01/api/rewards/locations).<br/>
<b>Required scopes:</b> `rewards:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.rewards.offers(
    organization_id="organization-123",
    user_id="user-123",
    page_size=1,
    filter_is_targeted=True,
    sort=[
        "-startDate"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search:** `typing.Optional[str]` — Case-insensitive search string to filter offers by merchant name
    
</dd>
</dl>

<dl>
<dd>

**filter_purchase_channel:** `typing.Optional[typing.List[PurchaseChannel]]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[CategoryOption]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_is_targeted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[OfferSortOptions, typing.Sequence[OfferSortOptions]]]` — If provided, response will be sorted by the specified fields
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — CSV list of included resources in the response (e.g "categories"). Allowed value is `categories`.
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">placement_offers</a>(...) -> OffersResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve offers for a placement slot. Returns offers sorted by highest cash back,
limited by the placement's available slots.<br/>
<b>Required scopes:</b> `rewards:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.rewards.placement_offers(
    organization_id="organizationId",
    user_id="userId",
    placement_id="placementId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**placement_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search:** `typing.Optional[str]` — Case-insensitive search string to filter offers by merchant name
    
</dd>
</dl>

<dl>
<dd>

**filter_purchase_channel:** `typing.Optional[typing.List[PurchaseChannel]]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[CategoryOption]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_is_targeted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — CSV list of included resources in the response (e.g "categories"). Allowed value is `categories`.
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.rewards.<a href="src/kard/users/rewards/client.py">locations</a>(...) -> LocationsResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve national and local geographic locations that a specified user has eligible in-store offers at. Use this endpoint to build
out your [map-specific UX experiences](/2024-10-01/api/getting-started#c-discover-clos-near-you-map-view). Please note
that Longitude and Latitude fields are prioritized over State, City and Zipcode and are the recommended search
pattern.<br/>
<br/>
<b>Required scopes:</b> `rewards:read`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.rewards.locations(
    organization_id="organization-123",
    user_id="user-123",
    page_size=1,
    filter_latitude=39.9419429,
    filter_longitude=-75.1446869,
    filter_radius=10,
    include=[
        "offers,categories"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserId` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_zip_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_state:** `typing.Optional[State]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_category:** `typing.Optional[CategoryOption]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[LocationSortOptions, typing.Sequence[LocationSortOptions]]]` — If provided, response will be sorted by the specified fields
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — CSV list of included resources in the response (e.g "offers,categories"). Allowed values are `offers` and `categories`.
    
</dd>
</dl>

<dl>
<dd>

**supported_components:** `typing.Optional[typing.Union[ComponentType, typing.Sequence[ComponentType]]]` — UI component types to include in included offers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users Uploads
<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create</a>(...) -> CreateUploadResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to create an upload session and retrieve an upload ID. Using the upload ID in the [Add Upload 
Part](/api/uploads/create-upload-part) endpoint, historical transactions can be sent in batches for further processing.
<b>Required scopes:</b> `transaction:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users.uploads import CreateUploadRequestDataUnion_HistoricalTransactionStart
from kard.commons import EmptyObject

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.uploads.create(
    organization_id="organization-123",
    user_id="user-123",
    data=CreateUploadRequestDataUnion_HistoricalTransactionStart(
        attributes=EmptyObject(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateUploadRequestObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">create_part</a>(...) -> CreateUploadPartResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint using the upload ID provided in the [Create Upload](/api/uploads/create-upload) endpoint to add parts to your upload. Currently, this endpoint supports adding historical transactions.
<b>Required scopes:</b> `transaction:write`
<b>Note:</b> `Maximum of 500 transactions can be uploaded per request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users.uploads import CreateUploadPartDataUnion_HistoricalTransaction
from kard.transactions import TransactionsAttributes, Merchant
import datetime

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.uploads.create_part(
    organization_id="organization-123",
    user_id="user-123",
    upload_id="upload-123",
    data=[
        CreateUploadPartDataUnion_HistoricalTransaction(
            id="309rjfoincor3icno3rind093cdow3jciwjdwcm",
            attributes=TransactionsAttributes(
                user_id="6FHt5b6Fnp0qdomMEy5AN6PXcSJIeX69",
                status="APPROVED",
                amount=1000,
                subtotal=800,
                currency="USD",
                direction="DEBIT",
                payment_type="CARD",
                description="ADVANCEAUTO",
                description_2="ADVANCEAUTO",
                mcc="1234",
                card_bin="123456",
                card_last_four="4321",
                authorization_date=datetime.datetime.fromisoformat("2021-07-02T17:47:06+00:00"),
                merchant=Merchant(
                    id="12345678901234567",
                    name="ADVANCEAUTO",
                    addr_street="125 Main St",
                    addr_city="Philadelphia",
                    addr_state="PA",
                    addr_zipcode="19147",
                    addr_country="United States",
                    latitude="37.9419429",
                    longitude="-73.1446869",
                    store_id="12345",
                ),
                authorization_code="123456",
                retrieval_reference_number="100804333919",
                acquirer_reference_number="1234567890123456789012345678",
                system_trace_audit_number="333828",
                transaction_id="2467de37-cbdc-416d-a359-75de87bfffb0",
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload ID identifying the upload session to add parts
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateUploadPartRequestObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.uploads.<a href="src/kard/users/uploads/client.py">update</a>(...) -> UpdateUploadResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this endpoint to update your upload session. Currently, you can signal completing a historical transactions upload.
<b>Required scopes:</b> `transaction:write`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from kard import KardApi
from kard.environment import KardApiEnvironment
from kard.users.uploads import UpdateUploadRequestDataUnion_HistoricalTransactionComplete
from kard.commons import EmptyObject

client = KardApi(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=KardApiEnvironment.PRODUCTION,
)

client.users.uploads.update(
    organization_id="organization-123",
    user_id="user-123",
    upload_id="upload-123",
    data=UpdateUploadRequestDataUnion_HistoricalTransactionComplete(
        id="7e382223-b9a5-4825-91fb-436c8957a2e7",
        attributes=EmptyObject(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationId` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The ID of the user as defined on the issuers system
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `str` — The upload ID identifying the upload session to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateUploadRequestObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

